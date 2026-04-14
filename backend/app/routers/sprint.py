import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.services import trophy_service

router = APIRouter(prefix="/api/sprints", tags=["sprints"])


class AwardTrophyRequest(BaseModel):
    action: str
    metadata: dict | None = None


@router.get("/active")
async def get_active_sprint(db: AsyncSession = Depends(get_db)):
    sprint = await trophy_service.get_active_sprint(db)
    if not sprint:
        return {"sprint": None}
    return {
        "sprint": {
            "id": str(sprint.id),
            "title": sprint.title,
            "start_date": sprint.start_date.isoformat(),
            "end_date": sprint.end_date.isoformat(),
            "status": sprint.status,
            "prizes": sprint.prizes,
        }
    }


@router.get("/active/leaderboard")
async def get_leaderboard(db: AsyncSession = Depends(get_db)):
    sprint = await trophy_service.get_active_sprint(db)
    if not sprint:
        return {"leaderboard": [], "sprint": None}
    leaderboard = await trophy_service.get_sprint_leaderboard(db, sprint.id)
    return {
        "leaderboard": leaderboard,
        "sprint": {
            "id": str(sprint.id),
            "title": sprint.title,
            "end_date": sprint.end_date.isoformat(),
        },
    }


@router.get("/my-trophies")
async def get_my_trophies(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    sprint = await trophy_service.get_active_sprint(db)
    sprint_id = sprint.id if sprint else None
    trophies = await trophy_service.get_user_trophies(db, user_id, sprint_id)
    return trophies


@router.get("/history")
async def get_sprint_history(db: AsyncSession = Depends(get_db)):
    from app.models.sprint import Sprint

    result = await db.execute(
        select(Sprint).where(Sprint.status.in_(["completed", "cancelled"])).order_by(Sprint.end_date.desc())
    )
    sprints = result.scalars().all()
    return [
        {
            "id": str(s.id),
            "title": s.title,
            "start_date": s.start_date.isoformat(),
            "end_date": s.end_date.isoformat(),
            "status": s.status,
            "prizes": s.prizes,
            "winners": s.winners,
        }
        for s in sprints
    ]


@router.post("/trophy")
async def award_trophy(
    body: AwardTrophyRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    allowed_actions = {"battle_win", "pose_check_90", "daily_quest"}
    if body.action not in allowed_actions:
        raise HTTPException(status_code=400, detail=f"Action must be one of: {', '.join(allowed_actions)}")
    trophies = await trophy_service.award_trophies(db, user_id, body.action, body.metadata)
    await db.commit()
    return {"awarded": trophies, "action": body.action}
