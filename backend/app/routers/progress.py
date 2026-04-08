import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.progress import (
    AddXPRequest, AddXPResponse,
    CompleteNodeRequest, CompleteLessonRequest,
    EarnBadgeRequest, EarnBadgeResponse,
    StreakResponse, StatsResponse,
)
from app.services import progress_service

router = APIRouter(prefix="/api/progress", tags=["progress"])


@router.post("/xp", response_model=AddXPResponse)
async def add_xp(body: AddXPRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.add_xp(db, user_id, body.amount, body.source)


@router.post("/node")
async def complete_node(body: CompleteNodeRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.complete_node(db, user_id, body.node_id)


@router.post("/lesson")
async def complete_lesson(body: CompleteLessonRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.complete_lesson(db, user_id, body.lesson_id)


@router.post("/badge", response_model=EarnBadgeResponse)
async def earn_badge(body: EarnBadgeRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.earn_badge(db, user_id, body.badge_id)


@router.post("/streak", response_model=StreakResponse)
async def update_streak(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.update_streak(db, user_id)


@router.get("/stats", response_model=StatsResponse)
async def get_stats(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.get_stats(db, user_id)
