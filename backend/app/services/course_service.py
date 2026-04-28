import math
import random
import re
import string
import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.course import (
    Course, CourseSection, CourseLesson,
    CourseEnrollment, CourseLessonProgress, CourseReview,
)
from app.models.progress import Progress
from app.models.user import User


# ── Helpers ───────────────────────────────────────────────

def _generate_slug(title: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{base}-{suffix}"


async def _get_course(db: AsyncSession, course_id: uuid.UUID) -> Course:
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


async def _assert_author(db: AsyncSession, course_id: uuid.UUID, user_id: uuid.UUID) -> Course:
    course = await _get_course(db, course_id)
    if course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")
    return course


async def _get_enrollment(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID) -> CourseEnrollment:
    result = await db.execute(
        select(CourseEnrollment).where(
            CourseEnrollment.user_id == user_id,
            CourseEnrollment.course_id == course_id,
        )
    )
    enrollment = result.scalar_one_or_none()
    if not enrollment:
        raise HTTPException(status_code=403, detail="You must be enrolled in this course")
    return enrollment


async def _get_progress(db: AsyncSession, user_id: uuid.UUID) -> Progress:
    result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    return result.scalar_one_or_none()


# ── Course CRUD ───────────────────────────────────────────

async def create_course(db: AsyncSession, user_id: uuid.UUID, data) -> dict:
    # Check if user is admin — admins publish instantly, others go to review
    user_result = await db.execute(select(User).where(User.id == user_id))
    author_obj = user_result.scalar_one()
    is_admin = author_obj.role == "admin"

    slug = _generate_slug(data.title)
    course = Course(
        title=data.title,
        slug=slug,
        description=data.description,
        thumbnail_url=data.thumbnail_url,
        author_id=user_id,
        category=data.category,
        difficulty=data.difficulty,
        price=data.price,
        currency=data.currency,
        tags=data.tags,
        status="draft" if is_admin else "pending_review",
    )
    db.add(course)
    await db.commit()
    await db.refresh(course)

    return {
        **_course_to_dict(course),
        "author_name": author_obj.name,
    }


async def update_course(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID, data) -> dict:
    course = await _assert_author(db, course_id, user_id)

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(course, field, value)

    # Regenerate slug if title changed
    if "title" in update_data:
        course.slug = _generate_slug(update_data["title"])

    await db.commit()
    await db.refresh(course)

    author = await db.execute(select(User).where(User.id == user_id))
    author_obj = author.scalar_one()

    return {
        **_course_to_dict(course),
        "author_name": author_obj.name,
    }


async def list_courses(
    db: AsyncSession,
    search: str | None = None,
    category: str | None = None,
    difficulty: str | None = None,
    min_price: int | None = None,
    max_price: int | None = None,
    tags: list[str] | None = None,
    sort: str = "newest",
    page: int = 1,
    per_page: int = 50,
) -> dict:
    from sqlalchemy import cast, String

    query = (
        select(Course, User.name.label("author_name"))
        .join(User, Course.author_id == User.id)
        .where(Course.status == "published")
    )

    if search:
        query = query.where(Course.title.ilike(f"%{search}%"))
    if category:
        query = query.where(Course.category == category)
    if difficulty:
        query = query.where(Course.difficulty == difficulty)
    if min_price is not None:
        query = query.where(Course.price >= min_price)
    if max_price is not None:
        query = query.where(Course.price <= max_price)
    if tags:
        from sqlalchemy import text
        for tag in tags:
            query = query.where(text("tags::text LIKE :tag").bindparams(tag=f'%"{tag}"%'))

    # Count total
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar()

    # Sorting
    if sort == "popular":
        query = query.order_by(Course.total_enrolled.desc())
    elif sort == "rating":
        query = query.order_by(Course.rating_avg.desc())
    elif sort == "price_asc":
        query = query.order_by(Course.price.asc())
    elif sort == "price_desc":
        query = query.order_by(Course.price.desc())
    else:  # newest
        query = query.order_by(Course.created_at.desc())

    # Pagination
    offset = (page - 1) * per_page
    query = query.offset(offset).limit(per_page)

    result = await db.execute(query)
    rows = result.all()

    items = []
    for course, author_name in rows:
        items.append({**_course_to_dict(course), "author_name": author_name})

    return {
        "items": items,
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": math.ceil(total / per_page) if per_page else 0,
    }


async def get_course(db: AsyncSession, course_id: uuid.UUID, user_id: uuid.UUID | None = None) -> dict:
    result = await db.execute(
        select(Course)
        .options(
            selectinload(Course.sections).selectinload(CourseSection.lessons),
        )
        .where(Course.id == course_id)
    )
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    author = await db.execute(select(User).where(User.id == course.author_id))
    author_obj = author.scalar_one()

    # Check enrollment and authorship
    is_enrolled = False
    is_author = False
    if user_id:
        is_author = (course.author_id == user_id)
        enrollment = await db.execute(
            select(CourseEnrollment).where(
                CourseEnrollment.user_id == user_id,
                CourseEnrollment.course_id == course_id,
            )
        )
        is_enrolled = enrollment.scalar_one_or_none() is not None

    # Fetch reviews
    reviews_result = await db.execute(
        select(CourseReview)
        .where(CourseReview.course_id == course_id)
        .order_by(CourseReview.created_at.desc())
    )
    reviews = reviews_result.scalars().all()

    # Get reviewer names
    reviewer_ids = [r.user_id for r in reviews]
    reviewer_names = {}
    if reviewer_ids:
        users_result = await db.execute(
            select(User).where(User.id.in_(reviewer_ids))
        )
        for u in users_result.scalars().all():
            reviewer_names[u.id] = u.name

    return {
        **_course_to_dict(course),
        "author_name": author_obj.name,
        "is_enrolled": is_enrolled,
        "is_author": is_author,
        "sections": [
            {
                "id": s.id,
                "title": s.title,
                "position": s.position,
                "lessons": [
                    {
                        "id": l.id,
                        "title": l.title,
                        "position": l.position,
                        "content_type": l.content_type,
                        "content_markdown": l.content_markdown,
                        "xp_reward": l.xp_reward,
                        "steps": l.steps,
                    }
                    for l in s.lessons
                ],
            }
            for s in course.sections
        ],
        "reviews": [
            {
                "id": r.id,
                "user_name": reviewer_names.get(r.user_id, "Unknown"),
                "rating": r.rating,
                "comment": r.comment,
                "created_at": r.created_at.isoformat() if r.created_at else None,
            }
            for r in reviews
        ],
    }


async def get_my_courses(db: AsyncSession, user_id: uuid.UUID) -> list[dict]:
    result = await db.execute(
        select(Course, User.name.label("author_name"))
        .join(User, Course.author_id == User.id)
        .where(Course.author_id == user_id)
        .order_by(Course.created_at.desc())
    )
    rows = result.all()
    return [{**_course_to_dict(c), "author_name": name} for c, name in rows]


async def get_enrolled_courses(db: AsyncSession, user_id: uuid.UUID) -> list[dict]:
    result = await db.execute(
        select(Course, User.name.label("author_name"))
        .join(CourseEnrollment, CourseEnrollment.course_id == Course.id)
        .join(User, Course.author_id == User.id)
        .where(CourseEnrollment.user_id == user_id)
        .order_by(CourseEnrollment.enrolled_at.desc())
    )
    rows = result.all()
    return [{**_course_to_dict(c), "author_name": name} for c, name in rows]


# ── Sections & Lessons ────────────────────────────────────

async def add_section(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID, data) -> dict:
    await _assert_author(db, course_id, user_id)

    section = CourseSection(
        course_id=course_id,
        title=data.title,
        position=data.position,
    )
    db.add(section)
    await db.commit()
    await db.refresh(section)
    return {"id": section.id, "title": section.title, "position": section.position, "lessons": []}


async def add_lesson(db: AsyncSession, user_id: uuid.UUID, section_id: uuid.UUID, data) -> dict:
    # Verify the section exists and user is the course author
    result = await db.execute(
        select(CourseSection).options(selectinload(CourseSection.course)).where(CourseSection.id == section_id)
    )
    section = result.scalar_one_or_none()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    if section.course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")

    lesson = CourseLesson(
        section_id=section_id,
        title=data.title,
        position=data.position,
        content_type=data.content_type,
        content_markdown=data.content_markdown,
        xp_reward=data.xp_reward,
        steps=data.steps,
    )
    db.add(lesson)
    await db.commit()
    await db.refresh(lesson)
    return {
        "id": lesson.id,
        "title": lesson.title,
        "position": lesson.position,
        "content_type": lesson.content_type,
        "content_markdown": lesson.content_markdown,
        "xp_reward": lesson.xp_reward,
        "steps": lesson.steps,
    }


async def update_section(db: AsyncSession, user_id: uuid.UUID, section_id: uuid.UUID, data) -> dict:
    """Update a section's title and/or position."""
    result = await db.execute(
        select(CourseSection).options(selectinload(CourseSection.course)).where(CourseSection.id == section_id)
    )
    section = result.scalar_one_or_none()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    if section.course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(section, field, value)

    await db.commit()
    await db.refresh(section)
    return {"id": section.id, "title": section.title, "position": section.position, "lessons": []}


async def delete_section(db: AsyncSession, user_id: uuid.UUID, section_id: uuid.UUID) -> None:
    """Delete a section and all its lessons (cascade)."""
    result = await db.execute(
        select(CourseSection).options(selectinload(CourseSection.course)).where(CourseSection.id == section_id)
    )
    section = result.scalar_one_or_none()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    if section.course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")

    await db.delete(section)
    await db.commit()


async def get_lesson(db: AsyncSession, lesson_id: uuid.UUID) -> dict:
    """Get a single lesson by id."""
    result = await db.execute(select(CourseLesson).where(CourseLesson.id == lesson_id))
    lesson = result.scalar_one_or_none()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {
        "id": lesson.id,
        "title": lesson.title,
        "position": lesson.position,
        "content_type": lesson.content_type,
        "content_markdown": lesson.content_markdown,
        "xp_reward": lesson.xp_reward,
        "steps": lesson.steps,
    }


async def update_lesson(db: AsyncSession, user_id: uuid.UUID, lesson_id: uuid.UUID, data) -> dict:
    """Update a lesson's fields (title, steps, xp_reward, content, position)."""
    result = await db.execute(
        select(CourseLesson)
        .options(selectinload(CourseLesson.section).selectinload(CourseSection.course))
        .where(CourseLesson.id == lesson_id)
    )
    lesson = result.scalar_one_or_none()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    if lesson.section.course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(lesson, field, value)

    await db.commit()
    await db.refresh(lesson)
    return {
        "id": lesson.id,
        "title": lesson.title,
        "position": lesson.position,
        "content_type": lesson.content_type,
        "content_markdown": lesson.content_markdown,
        "xp_reward": lesson.xp_reward,
        "steps": lesson.steps,
    }


async def delete_lesson(db: AsyncSession, user_id: uuid.UUID, lesson_id: uuid.UUID) -> None:
    """Delete a lesson."""
    result = await db.execute(
        select(CourseLesson)
        .options(selectinload(CourseLesson.section).selectinload(CourseSection.course))
        .where(CourseLesson.id == lesson_id)
    )
    lesson = result.scalar_one_or_none()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    if lesson.section.course.author_id != user_id:
        raise HTTPException(status_code=403, detail="Only the course author can perform this action")

    await db.delete(lesson)
    await db.commit()


# ── Enrollment ────────────────────────────────────────────

async def enroll(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID) -> dict:
    course = await _get_course(db, course_id)

    # Check not already enrolled
    existing = await db.execute(
        select(CourseEnrollment).where(
            CourseEnrollment.user_id == user_id,
            CourseEnrollment.course_id == course_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Already enrolled in this course")

    enrollment = CourseEnrollment(
        user_id=user_id,
        course_id=course_id,
        paid_amount=course.price,
    )
    db.add(enrollment)
    course.total_enrolled += 1
    await db.commit()
    await db.refresh(enrollment)
    return {"id": enrollment.id, "course_id": enrollment.course_id, "enrolled_at": enrollment.enrolled_at}


# ── Lesson Completion ─────────────────────────────────────

async def complete_lesson(db: AsyncSession, user_id: uuid.UUID, lesson_id: uuid.UUID) -> dict:
    # Get the lesson and its course
    result = await db.execute(
        select(CourseLesson)
        .options(selectinload(CourseLesson.section).selectinload(CourseSection.course))
        .where(CourseLesson.id == lesson_id)
    )
    lesson = result.scalar_one_or_none()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    course = lesson.section.course
    await _get_enrollment(db, user_id, course.id)

    # Check if already completed
    existing = await db.execute(
        select(CourseLessonProgress).where(
            CourseLessonProgress.user_id == user_id,
            CourseLessonProgress.lesson_id == lesson_id,
        )
    )
    if existing.scalar_one_or_none():
        return {"lesson_id": lesson_id, "xp_awarded": 0, "course_completed": False}

    # Mark completed
    progress_entry = CourseLessonProgress(user_id=user_id, lesson_id=lesson_id)
    db.add(progress_entry)

    # Award XP
    xp_awarded = lesson.xp_reward
    user_progress = await _get_progress(db, user_id)
    if user_progress:
        user_progress.xp += xp_awarded
        user_progress.xp_this_week += xp_awarded

    # Check if course is fully completed
    all_lessons_result = await db.execute(
        select(CourseLesson.id)
        .join(CourseSection, CourseLesson.section_id == CourseSection.id)
        .where(CourseSection.course_id == course.id)
    )
    all_lesson_ids = {row[0] for row in all_lessons_result.all()}

    completed_result = await db.execute(
        select(CourseLessonProgress.lesson_id).where(
            CourseLessonProgress.user_id == user_id,
            CourseLessonProgress.lesson_id.in_(all_lesson_ids),
        )
    )
    completed_ids = {row[0] for row in completed_result.all()}
    completed_ids.add(lesson_id)  # include current

    course_completed = completed_ids >= all_lesson_ids

    if course_completed:
        enroll_result = await db.execute(
            select(CourseEnrollment).where(
                CourseEnrollment.user_id == user_id,
                CourseEnrollment.course_id == course.id,
            )
        )
        enrollment = enroll_result.scalar_one_or_none()
        if enrollment and not enrollment.completed_at:
            enrollment.completed_at = datetime.now(timezone.utc)

    await db.commit()
    return {"lesson_id": lesson_id, "xp_awarded": xp_awarded, "course_completed": course_completed}


# ── Reviews ───────────────────────────────────────────────

async def add_review(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID, rating: int, comment: str) -> dict:
    await _get_enrollment(db, user_id, course_id)

    # Check for existing review
    existing = await db.execute(
        select(CourseReview).where(
            CourseReview.user_id == user_id,
            CourseReview.course_id == course_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="You have already reviewed this course")

    review = CourseReview(user_id=user_id, course_id=course_id, rating=rating, comment=comment)
    db.add(review)

    # Update course rating
    course = await _get_course(db, course_id)
    total_rating = course.rating_avg * course.rating_count + rating
    course.rating_count += 1
    course.rating_avg = round(total_rating / course.rating_count, 2)

    await db.commit()
    await db.refresh(review)
    return {
        "id": review.id,
        "user_id": review.user_id,
        "course_id": review.course_id,
        "rating": review.rating,
        "comment": review.comment,
        "created_at": review.created_at,
    }


# ── Progress ──────────────────────────────────────────────

async def get_dashboard_stats(db: AsyncSession, user_id: uuid.UUID) -> dict:
    """Aggregate stats across ALL enrolled courses for dashboard."""
    # Get all enrolled courses
    enrolled_result = await db.execute(
        select(Course.id, Course.title, Course.thumbnail_url, Course.category)
        .join(CourseEnrollment, CourseEnrollment.course_id == Course.id)
        .where(CourseEnrollment.user_id == user_id)
    )
    enrolled_courses = enrolled_result.all()

    total_lessons = 0
    total_completed = 0
    total_xp_earned = 0
    course_stats = []

    for course_id, course_title, thumbnail, category in enrolled_courses:
        # Count all lessons in course
        lessons_result = await db.execute(
            select(CourseLesson.id, CourseLesson.xp_reward)
            .join(CourseSection, CourseLesson.section_id == CourseSection.id)
            .where(CourseSection.course_id == course_id)
        )
        all_lessons = lessons_result.all()
        lesson_ids = [row[0] for row in all_lessons]
        xp_map = {row[0]: row[1] for row in all_lessons}

        # Count completed lessons
        if lesson_ids:
            completed_result = await db.execute(
                select(CourseLessonProgress.lesson_id).where(
                    CourseLessonProgress.user_id == user_id,
                    CourseLessonProgress.lesson_id.in_(lesson_ids),
                )
            )
            completed_ids = [row[0] for row in completed_result.all()]
        else:
            completed_ids = []

        course_xp = sum(xp_map.get(lid, 0) for lid in completed_ids)
        course_total = len(all_lessons)
        course_done = len(completed_ids)
        pct = round(course_done / max(course_total, 1) * 100)

        total_lessons += course_total
        total_completed += course_done
        total_xp_earned += course_xp

        course_stats.append({
            "course_id": str(course_id),
            "title": course_title,
            "thumbnail_url": thumbnail,
            "category": category or "Other",
            "total_lessons": course_total,
            "completed_lessons": course_done,
            "progress_percent": pct,
            "xp_earned": course_xp,
        })

    # Sort: in-progress first, then by progress desc
    course_stats.sort(key=lambda c: (
        0 if 0 < c["progress_percent"] < 100 else 1,
        -c["progress_percent"],
    ))

    overall_pct = round(total_completed / max(total_lessons, 1) * 100)

    return {
        "total_courses": len(enrolled_courses),
        "total_lessons": total_lessons,
        "total_completed": total_completed,
        "total_xp": total_xp_earned,
        "overall_progress": overall_pct,
        "courses": course_stats,
    }


async def get_course_progress(db: AsyncSession, user_id: uuid.UUID, course_id: uuid.UUID) -> dict:
    await _get_enrollment(db, user_id, course_id)

    # Get all lesson IDs for the course
    all_lessons_result = await db.execute(
        select(CourseLesson.id)
        .join(CourseSection, CourseLesson.section_id == CourseSection.id)
        .where(CourseSection.course_id == course_id)
    )
    all_lesson_ids = [row[0] for row in all_lessons_result.all()]

    # Get completed lesson IDs
    completed_result = await db.execute(
        select(CourseLessonProgress.lesson_id).where(
            CourseLessonProgress.user_id == user_id,
            CourseLessonProgress.lesson_id.in_(all_lesson_ids) if all_lesson_ids else False,
        )
    )
    completed_ids = [row[0] for row in completed_result.all()]

    return {
        "course_id": course_id,
        "completed_lesson_ids": completed_ids,
        "total_lessons": len(all_lesson_ids),
        "completed_count": len(completed_ids),
        "is_completed": len(completed_ids) == len(all_lesson_ids) and len(all_lesson_ids) > 0,
    }


# ── All Steps (for Tower Defense) ─────────────────────────

async def get_all_steps(db: AsyncSession, course_id: uuid.UUID) -> dict:
    """Return all steps from all lessons in a course as a flat array."""
    result = await db.execute(
        select(CourseLesson.steps)
        .join(CourseSection, CourseSection.id == CourseLesson.section_id)
        .where(CourseSection.course_id == course_id)
        .order_by(CourseSection.position, CourseLesson.position)
    )
    all_steps = []
    for (steps,) in result.all():
        if steps:
            all_steps.extend(steps)
    return {"steps": all_steps}


# ── Utility ───────────────────────────────────────────────

async def get_course_tags(db: AsyncSession) -> list[str]:
    """Return unique tags from all published courses."""
    result = await db.execute(
        select(Course.tags).where(Course.status == "published", Course.tags.isnot(None))
    )
    all_tags: set[str] = set()
    for (tags,) in result:
        if tags:
            all_tags.update(tags)
    return sorted(all_tags)


async def recommend_by_tags(db: AsyncSession, tags: list[str], limit: int = 20) -> list[dict]:
    """Return published courses that have at least one matching tag."""
    result = await db.execute(
        select(Course)
        .where(Course.status == "published")
        .order_by(Course.total_enrolled.desc())
        .limit(100)
    )
    courses = result.scalars().all()

    tag_set = set(t.lower() for t in tags)
    matched = []
    for course in courses:
        course_tags = set(t.lower() for t in (course.tags or []))
        if course_tags & tag_set:
            matched.append(course)
        if len(matched) >= limit:
            break

    return [
        {
            "id": c.id,
            "title": c.title,
            "slug": c.slug,
            "description": c.description,
            "thumbnail_url": c.thumbnail_url,
            "category": c.category,
            "tags": c.tags or [],
            "difficulty": c.difficulty,
            "price": c.price,
            "currency": c.currency,
            "total_enrolled": c.total_enrolled,
            "rating_avg": c.rating_avg,
            "rating_count": c.rating_count,
        }
        for c in matched
    ]


async def approve_course(db: AsyncSession, admin_id: uuid.UUID, course_id: uuid.UUID) -> dict:
    """Admin approves a pending course — sets status to published."""
    # Check admin
    admin_result = await db.execute(select(User).where(User.id == admin_id))
    admin = admin_result.scalar_one_or_none()
    if not admin or admin.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    course.status = "published"
    await db.commit()
    await db.refresh(course)
    return _course_to_dict(course)


def _course_to_dict(course: Course) -> dict:
    return {
        "id": course.id,
        "title": course.title,
        "slug": course.slug,
        "description": course.description,
        "thumbnail_url": course.thumbnail_url,
        "author_id": course.author_id,
        "category": course.category,
        "difficulty": course.difficulty,
        "price": course.price,
        "currency": course.currency,
        "status": course.status,
        "total_enrolled": course.total_enrolled,
        "rating_avg": course.rating_avg,
        "rating_count": course.rating_count,
        "tags": course.tags,
        "roadmap_nodes": course.roadmap_nodes,
        "roadmap_edges": course.roadmap_edges,
        "created_at": course.created_at,
    }
