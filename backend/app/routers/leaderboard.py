import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.leaderboard import LeaderboardResponse, MyRankResponse
from app.services import leaderboard_service

router = APIRouter(prefix="/api/leaderboard", tags=["leaderboard"])


@router.get("/weekly", response_model=LeaderboardResponse)
async def weekly(db: AsyncSession = Depends(get_db)):
    return await leaderboard_service.get_leaderboard(db, "weekly")


@router.get("/monthly", response_model=LeaderboardResponse)
async def monthly(db: AsyncSession = Depends(get_db)):
    return await leaderboard_service.get_leaderboard(db, "monthly")


@router.get("/all-time", response_model=LeaderboardResponse)
async def all_time(db: AsyncSession = Depends(get_db)):
    return await leaderboard_service.get_leaderboard(db, "alltime")


@router.get("/my-rank", response_model=MyRankResponse)
async def my_rank(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await leaderboard_service.get_my_rank(db, user_id)
