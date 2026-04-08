from datetime import datetime

from pydantic import BaseModel, Field


class AddXPRequest(BaseModel):
    amount: int = Field(gt=0, le=1000)
    source: str = Field(min_length=1, max_length=50)


class AddXPResponse(BaseModel):
    xp: int
    level: str
    leveled_up: bool


class CompleteNodeRequest(BaseModel):
    node_id: str = Field(min_length=1, max_length=100)


class CompleteLessonRequest(BaseModel):
    lesson_id: str = Field(min_length=1, max_length=100)


class EarnBadgeRequest(BaseModel):
    badge_id: str = Field(min_length=1, max_length=50)


class EarnBadgeResponse(BaseModel):
    badge_id: str
    earned_at: datetime


class StreakResponse(BaseModel):
    streak: int
    longest_streak: int


class StatsResponse(BaseModel):
    xp: int
    level: str
    streak: int
    longest_streak: int
    completed_nodes: list[str]
    completed_lessons: list[str]
    earned_badges: list[str]
