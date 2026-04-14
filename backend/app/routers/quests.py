import uuid

from fastapi import APIRouter, Depends

from app.dependencies import get_current_user_id
from app.redis import get_redis_client
from app.schemas.quests import DailyQuestsResponse
from app.services import quest_service

router = APIRouter(prefix="/api/quests", tags=["quests"])


@router.get("/daily", response_model=DailyQuestsResponse)
async def get_daily_quests(user_id: uuid.UUID = Depends(get_current_user_id)):
    r = get_redis_client()
    try:
        return await quest_service.get_daily_quests(r, str(user_id))
    finally:
        await r.aclose()


@router.post("/daily/check", response_model=DailyQuestsResponse)
async def check_quest_progress(user_id: uuid.UUID = Depends(get_current_user_id)):
    r = get_redis_client()
    try:
        return await quest_service.check_quest_progress(r, str(user_id))
    finally:
        await r.aclose()
