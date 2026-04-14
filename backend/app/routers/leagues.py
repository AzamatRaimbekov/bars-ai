import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.leagues import LeagueInfo, LeagueMember
from app.services import progress_service

router = APIRouter(prefix="/api/leagues", tags=["leagues"])


@router.get("/me", response_model=LeagueInfo)
async def get_my_league(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await progress_service.get_league_info(db, user_id)


@router.get("/members", response_model=List[LeagueMember])
async def get_league_members(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    return await progress_service.get_league_members(db, user_id)
