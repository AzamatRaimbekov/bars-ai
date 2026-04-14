from pydantic import BaseModel, Field
from datetime import datetime


class MentorChatRequest(BaseModel):
    session_id: str | None = None
    content: str = Field(min_length=1)


class MentorChatResponse(BaseModel):
    content: str
    session_id: str
    message_id: str


class SessionCreate(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    title: str | None = None


class SessionOut(BaseModel):
    id: str
    direction: str
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MessageOut(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class KnowledgeProfileOut(BaseModel):
    direction: str
    strengths: list
    weaknesses: list
    notes: list
    updated_at: datetime

    class Config:
        from_attributes = True


class RecommendationItem(BaseModel):
    lesson_id: str
    lesson_title: str
    course_title: str
    reason: str
    priority: str


class RecommendationsResponse(BaseModel):
    weekly_plan: list[RecommendationItem]
    stats: dict


class VoiceLessonRequest(BaseModel):
    session_id: str
    action: str = Field(pattern=r"^(start|next|repeat|answer)$")
    topic: str | None = None
    content: str | None = None


class VoiceLessonResponse(BaseModel):
    phase: str
    content: str
    exercise: dict | None = None
    progress: float
    is_complete: bool
