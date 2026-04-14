import uuid

from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.mentor import (
    MentorChatRequest, MentorChatResponse,
    SessionCreate, SessionOut, MessageOut,
    KnowledgeProfileOut, RecommendationsResponse,
    VoiceLessonRequest, VoiceLessonResponse,
)
from app.services import mentor_service
from app.utils.rate_limiter import rate_limit

router = APIRouter(prefix="/api/mentor", tags=["mentor"])


@router.get("/sessions", response_model=list[SessionOut])
async def list_sessions(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    sessions = await mentor_service.get_sessions(db, user_id)
    return [SessionOut(id=str(s.id), direction=s.direction, title=s.title, created_at=s.created_at, updated_at=s.updated_at) for s in sessions]


@router.post("/sessions", response_model=SessionOut)
async def create_session(body: SessionCreate, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    session = await mentor_service.create_session(db, user_id, body.direction, body.title)
    await db.commit()
    return SessionOut(id=str(session.id), direction=session.direction, title=session.title, created_at=session.created_at, updated_at=session.updated_at)


@router.get("/sessions/{session_id}/messages", response_model=list[MessageOut])
async def get_messages(
    session_id: uuid.UUID,
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0),
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    messages = await mentor_service.get_messages(db, session_id, user_id, limit, offset)
    return [MessageOut(id=str(m.id), role=m.role, content=m.content, created_at=m.created_at) for m in messages]


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: uuid.UUID, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    deleted = await mentor_service.delete_session(db, session_id, user_id)
    await db.commit()
    if not deleted:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Session not found")
    return {"ok": True}


@router.get("/profile", response_model=KnowledgeProfileOut)
async def get_profile(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    from app.models.user import User
    from sqlalchemy import select
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one()
    profile = await mentor_service.get_or_create_profile(db, user_id, user.direction or "frontend")
    await db.commit()
    return KnowledgeProfileOut(direction=profile.direction, strengths=profile.strengths, weaknesses=profile.weaknesses, notes=profile.notes, updated_at=profile.updated_at)


@router.post("/chat", response_model=MentorChatResponse)
async def chat(body: MentorChatRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await mentor_service.chat(db, user_id, body.session_id, body.content)
    return MentorChatResponse(**result)


@router.get("/recommendations", response_model=RecommendationsResponse)
async def recommendations(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    result = await mentor_service.get_recommendations(db, user_id)
    return RecommendationsResponse(**result)


@router.post("/voice-lesson", response_model=VoiceLessonResponse)
async def voice_lesson(body: VoiceLessonRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await mentor_service.voice_lesson(db, user_id, body.session_id, body.action, body.topic, body.content)
    return VoiceLessonResponse(**result)
