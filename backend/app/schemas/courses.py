import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# ── Requests ──────────────────────────────────────────────

class CreateCourseRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=5000)
    category: str = Field(default="other", max_length=50)
    tags: list[str] = Field(default_factory=list)
    difficulty: str = Field(default="beginner", max_length=20)
    price: int = Field(default=0, ge=0)
    currency: str = Field(default="USD", max_length=3)
    thumbnail_url: str | None = None


class UpdateCourseRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    description: str | None = Field(default=None, max_length=5000)
    category: str | None = Field(default=None, max_length=50)
    tags: list[str] | None = None
    difficulty: str | None = Field(default=None, max_length=20)
    price: int | None = Field(default=None, ge=0)
    currency: str | None = Field(default=None, max_length=3)
    thumbnail_url: str | None = None
    status: str | None = Field(default=None, pattern=r"^(draft|published)$")
    roadmap_nodes: Optional[list] = None
    roadmap_edges: Optional[list] = None


class CreateSectionRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    position: int = Field(default=0, ge=0)


class CreateLessonRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    position: int = Field(default=0, ge=0)
    content_type: str = Field(default="text", pattern=r"^(text|quiz|interactive)$")
    content_markdown: str = Field(default="", max_length=50000)
    xp_reward: int = Field(default=10, ge=0, le=500)
    steps: Optional[list] = None


class UpdateLessonRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    position: int | None = Field(default=None, ge=0)
    content_type: str | None = Field(default=None, pattern=r"^(text|quiz|interactive)$")
    content_markdown: str | None = Field(default=None, max_length=50000)
    xp_reward: int | None = Field(default=None, ge=0, le=500)
    steps: Optional[list] = None


class UpdateSectionRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    position: int | None = Field(default=None, ge=0)


class EnrollRequest(BaseModel):
    pass  # payment fields can be added later


class ReviewRequest(BaseModel):
    rating: int = Field(ge=1, le=5)
    comment: str = Field(default="", max_length=2000)


# ── Responses ─────────────────────────────────────────────

class AuthorBrief(BaseModel):
    id: uuid.UUID
    name: str

    model_config = {"from_attributes": True}


class CourseLessonResponse(BaseModel):
    id: uuid.UUID
    title: str
    position: int
    content_type: str
    content_markdown: str
    xp_reward: int
    steps: Optional[list] = None

    model_config = {"from_attributes": True}


class CourseSectionResponse(BaseModel):
    id: uuid.UUID
    title: str
    position: int
    lessons: list[CourseLessonResponse] = []

    model_config = {"from_attributes": True}


class CourseResponse(BaseModel):
    id: uuid.UUID
    title: str
    slug: str
    description: str
    thumbnail_url: str | None
    author_id: uuid.UUID
    author_name: str
    category: str
    difficulty: str
    price: int
    currency: str
    status: str
    total_enrolled: int
    rating_avg: float
    rating_count: int
    roadmap_nodes: Optional[list] = None
    roadmap_edges: Optional[list] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class CourseLessonsResponse(BaseModel):
    """Full course detail with curriculum."""
    id: uuid.UUID
    title: str
    slug: str
    description: str
    thumbnail_url: str | None
    author_id: uuid.UUID
    author_name: str
    category: str
    difficulty: str
    price: int
    currency: str
    status: str
    total_enrolled: int
    rating_avg: float
    rating_count: int
    roadmap_nodes: Optional[list] = None
    roadmap_edges: Optional[list] = None
    created_at: datetime
    sections: list[CourseSectionResponse] = []

    model_config = {"from_attributes": True}


class CourseListResponse(BaseModel):
    items: list[CourseResponse]
    total: int
    page: int
    per_page: int
    pages: int


class EnrollmentResponse(BaseModel):
    id: uuid.UUID
    course_id: uuid.UUID
    enrolled_at: datetime

    model_config = {"from_attributes": True}


class ReviewResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    course_id: uuid.UUID
    rating: int
    comment: str
    created_at: datetime

    model_config = {"from_attributes": True}


class CourseProgressResponse(BaseModel):
    course_id: uuid.UUID
    completed_lesson_ids: list[uuid.UUID]
    total_lessons: int
    completed_count: int
    is_completed: bool


class LessonCompleteResponse(BaseModel):
    lesson_id: uuid.UUID
    xp_awarded: int
    course_completed: bool
