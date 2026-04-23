import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    direction: str
    assessment_level: str
    language: str
    avatar_url: str | None
    interests: list[str] = []
    onboarding_complete: bool = False
    created_at: datetime

    model_config = {"from_attributes": True}


class UserWithProgressResponse(UserResponse):
    xp: int = 0
    level: str = "Novice"
    streak: int = 0
    longest_streak: int = 0
    completed_nodes: list[str] = []
    completed_lessons: list[str] = []
    earned_badges: list[str] = []


class UserUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    language: str | None = Field(None, pattern=r"^(ru|en)$")
    avatar_url: str | None = None
    interests: list[str] | None = None
    onboarding_complete: bool | None = None
    assessment_context: str | None = None
    direction: str | None = None
    assessment_level: str | None = None


class PublicUserResponse(BaseModel):
    id: uuid.UUID
    name: str
    direction: str
    level: str
    earned_badges: list[str]

    model_config = {"from_attributes": True}
