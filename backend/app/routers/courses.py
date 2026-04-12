import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id, get_optional_user_id
from app.schemas.courses import (
    CreateCourseRequest, UpdateCourseRequest,
    CourseResponse, CourseLessonsResponse, CourseListResponse,
    CreateSectionRequest, CreateLessonRequest,
    UpdateLessonRequest, UpdateSectionRequest,
    EnrollRequest, ReviewRequest,
    EnrollmentResponse, ReviewResponse,
    CourseProgressResponse, LessonCompleteResponse,
    CourseSectionResponse, CourseLessonResponse,
)
from app.services import course_service

router = APIRouter(prefix="/api/courses", tags=["courses"])


@router.get("", response_model=CourseListResponse)
async def list_courses(
    search: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    difficulty: Optional[str] = Query(None),
    min_price: Optional[int] = Query(None, ge=0),
    max_price: Optional[int] = Query(None, ge=0),
    sort: str = Query("newest", pattern=r"^(newest|popular|rating|price_asc|price_desc)$"),
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.list_courses(
        db, search=search, category=category, difficulty=difficulty,
        min_price=min_price, max_price=max_price, sort=sort,
        page=page, per_page=per_page,
    )


@router.get("/my", response_model=list[CourseResponse])
async def get_my_courses(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.get_my_courses(db, user_id)


@router.get("/enrolled", response_model=list[CourseResponse])
async def get_enrolled_courses(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.get_enrolled_courses(db, user_id)


@router.get("/{course_id}")
async def get_course(
    course_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user_id: uuid.UUID | None = Depends(get_optional_user_id),
):
    return await course_service.get_course(db, course_id, user_id=user_id)


@router.post("", response_model=CourseResponse, status_code=201)
async def create_course(
    body: CreateCourseRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.create_course(db, user_id, body)


@router.patch("/{course_id}", response_model=CourseResponse)
async def update_course(
    course_id: uuid.UUID,
    body: UpdateCourseRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.update_course(db, user_id, course_id, body)


@router.post("/{course_id}/sections", response_model=CourseSectionResponse, status_code=201)
async def add_section(
    course_id: uuid.UUID,
    body: CreateSectionRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.add_section(db, user_id, course_id, body)


@router.post("/sections/{section_id}/lessons", response_model=CourseLessonResponse, status_code=201)
async def add_lesson(
    section_id: uuid.UUID,
    body: CreateLessonRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.add_lesson(db, user_id, section_id, body)


@router.patch("/sections/{section_id}", response_model=CourseSectionResponse)
async def update_section(
    section_id: uuid.UUID,
    body: UpdateSectionRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.update_section(db, user_id, section_id, body)


@router.delete("/sections/{section_id}", status_code=204)
async def delete_section(
    section_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    await course_service.delete_section(db, user_id, section_id)


@router.get("/lessons/{lesson_id}", response_model=CourseLessonResponse)
async def get_lesson(
    lesson_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    return await course_service.get_lesson(db, lesson_id)


@router.patch("/lessons/{lesson_id}", response_model=CourseLessonResponse)
async def update_lesson(
    lesson_id: uuid.UUID,
    body: UpdateLessonRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.update_lesson(db, user_id, lesson_id, body)


@router.delete("/lessons/{lesson_id}", status_code=204)
async def delete_lesson(
    lesson_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    await course_service.delete_lesson(db, user_id, lesson_id)


@router.post("/{course_id}/enroll", response_model=EnrollmentResponse, status_code=201)
async def enroll(
    course_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.enroll(db, user_id, course_id)


@router.post("/{course_id}/review", response_model=ReviewResponse, status_code=201)
async def add_review(
    course_id: uuid.UUID,
    body: ReviewRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.add_review(db, user_id, course_id, body.rating, body.comment)


@router.post("/lessons/{lesson_id}/complete", response_model=LessonCompleteResponse)
async def complete_lesson(
    lesson_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.complete_lesson(db, user_id, lesson_id)


@router.get("/{course_id}/all-steps")
async def get_all_course_steps(
    course_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    """Return all steps from all lessons in a course (flat array)."""
    return await course_service.get_all_steps(db, course_id)


@router.get("/{course_id}/progress", response_model=CourseProgressResponse)
async def get_course_progress(
    course_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await course_service.get_course_progress(db, user_id, course_id)
