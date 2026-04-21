import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.models.sprint import Sprint, TrophyEvent
from app.models.user import User
from app.models.course import Course
from app.models.notification import Notification
from app.services import trophy_service

router = APIRouter(prefix="/api/admin", tags=["admin"])


async def get_admin_user(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
) -> uuid.UUID:
    result = await db.execute(select(User.role).where(User.id == user_id))
    role = result.scalar_one_or_none()
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user_id


class CreateSprintRequest(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    prizes: list[dict] | None = None


# --- Sprints ---

@router.get("/sprints")
async def list_sprints(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Sprint).order_by(Sprint.created_at.desc()))
    sprints = result.scalars().all()
    return [
        {
            "id": str(s.id),
            "title": s.title,
            "start_date": s.start_date.isoformat(),
            "end_date": s.end_date.isoformat(),
            "status": s.status,
            "prizes": s.prizes,
            "winners": s.winners,
            "created_at": s.created_at.isoformat() if s.created_at else None,
        }
        for s in sprints
    ]


@router.post("/sprints")
async def create_sprint(
    body: CreateSprintRequest,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    sprint = Sprint(
        title=body.title,
        start_date=body.start_date,
        end_date=body.end_date,
        status="active",
        created_by=admin_id,
    )
    if body.prizes:
        sprint.prizes = body.prizes
    db.add(sprint)
    await db.commit()
    await db.refresh(sprint)
    return {"id": str(sprint.id), "title": sprint.title, "status": sprint.status}


@router.post("/sprints/{sprint_id}/close")
async def close_sprint(
    sprint_id: uuid.UUID,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await trophy_service.close_sprint(db, sprint_id, admin_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    await db.commit()
    return result


@router.post("/sprints/{sprint_id}/cancel")
async def cancel_sprint(
    sprint_id: uuid.UUID,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Sprint).where(Sprint.id == sprint_id))
    sprint = result.scalar_one_or_none()
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    sprint.status = "cancelled"
    sprint.closed_by = admin_id
    await db.commit()
    return {"status": "cancelled", "id": str(sprint_id)}


# --- Users ---

@router.get("/users")
async def list_users(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(
            User.id,
            User.email,
            User.name,
            User.role,
            User.direction,
            User.created_at,
            func.coalesce(func.sum(TrophyEvent.trophies), 0).label("total_trophies"),
        )
        .outerjoin(TrophyEvent, TrophyEvent.user_id == User.id)
        .group_by(User.id, User.email, User.name, User.role, User.direction, User.created_at)
        .order_by(User.created_at.desc())
    )
    rows = result.all()
    return [
        {
            "id": str(r[0]),
            "email": r[1],
            "name": r[2],
            "role": r[3],
            "direction": r[4],
            "created_at": r[5].isoformat() if r[5] else None,
            "total_trophies": r[6],
        }
        for r in rows
    ]


# --- Course Moderation ---

@router.get("/courses/pending")
async def list_pending_courses(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course, User.name.label("author_name"), User.email.label("author_email"))
        .join(User, Course.author_id == User.id)
        .where(Course.status == "pending_review")
        .order_by(Course.created_at.desc())
    )
    rows = result.all()
    return [
        {
            "id": str(course.id),
            "title": course.title,
            "description": course.description,
            "category": course.category,
            "difficulty": course.difficulty,
            "price": course.price,
            "currency": course.currency,
            "author_name": author_name,
            "author_email": author_email,
            "author_id": str(course.author_id),
            "created_at": course.created_at.isoformat() if course.created_at else None,
        }
        for course, author_name, author_email in rows
    ]


class CourseReviewRequest(BaseModel):
    action: str  # "approve" or "reject"
    note: str | None = None


@router.post("/courses/{course_id}/review")
async def review_course(
    course_id: uuid.UUID,
    body: CourseReviewRequest,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.status != "pending_review":
        raise HTTPException(status_code=400, detail="Course is not pending review")

    if body.action == "approve":
        course.status = "published"
        # Send congratulations notification
        notification = Notification(
            user_id=course.author_id,
            title="Ваш курс опубликован! 🎉",
            message=f"Поздравляем! Ваш курс «{course.title}» прошёл модерацию и теперь доступен всем пользователям. Спасибо, что создаёте крутой контент для обучения на Bars AI! Вы помогаете людям учиться и развиваться.",
            type="course_approved",
            link=f"/courses/{course.id}",
        )
        db.add(notification)
    elif body.action == "reject":
        course.status = "rejected"
        reason = body.note or "Курс не прошёл модерацию"
        notification = Notification(
            user_id=course.author_id,
            title="Курс отклонён",
            message=f"К сожалению, ваш курс «{course.title}» не прошёл модерацию. Причина: {reason}. Вы можете доработать курс и отправить на проверку повторно.",
            type="course_rejected",
            link=f"/teach/{course.id}",
        )
        db.add(notification)
    else:
        raise HTTPException(status_code=400, detail="Action must be 'approve' or 'reject'")

    await db.commit()
    return {"id": str(course.id), "status": course.status}


# --- Stats ---

@router.get("/stats")
async def platform_stats(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    users_count = (await db.execute(select(func.count()).select_from(User))).scalar()
    courses_count = (await db.execute(select(func.count()).select_from(Course))).scalar()
    total_trophies = (await db.execute(select(func.coalesce(func.sum(TrophyEvent.trophies), 0)))).scalar()

    active_sprint = await trophy_service.get_active_sprint(db)
    sprint_info = None
    if active_sprint:
        sprint_info = {
            "id": str(active_sprint.id),
            "title": active_sprint.title,
            "end_date": active_sprint.end_date.isoformat(),
        }

    return {
        "total_users": users_count,
        "total_courses": courses_count,
        "total_trophies": total_trophies,
        "active_sprint": sprint_info,
    }
