import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.models.sprint import Sprint, TrophyEvent
from app.models.user import User
from app.models.course import Course
from app.services import trophy_service

router = APIRouter(prefix="/api/admin", tags=["admin"])


async def get_admin_user(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
) -> uuid.UUID:
    result = await db.execute(select(User.role).where(User.id == user_id))
    role = result.scalar_one_or_none()
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user_id


class CreateSprintRequest(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    prizes: list[dict] | None = None


# --- Sprints ---

@router.get("/sprints")
async def list_sprints(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Sprint).order_by(Sprint.created_at.desc()))
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
            "created_at": s.created_at.isoformat() if s.created_at else None,
        }
        for s in sprints
    ]


@router.post("/sprints")
async def create_sprint(
    body: CreateSprintRequest,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    sprint = Sprint(
        title=body.title,
        start_date=body.start_date,
        end_date=body.end_date,
        status="active",
        created_by=admin_id,
    )
    if body.prizes:
        sprint.prizes = body.prizes
    db.add(sprint)
    await db.commit()
    await db.refresh(sprint)
    return {"id": str(sprint.id), "title": sprint.title, "status": sprint.status}


@router.post("/sprints/{sprint_id}/close")
async def close_sprint(
    sprint_id: uuid.UUID,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await trophy_service.close_sprint(db, sprint_id, admin_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    await db.commit()
    return result


@router.post("/sprints/{sprint_id}/cancel")
async def cancel_sprint(
    sprint_id: uuid.UUID,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Sprint).where(Sprint.id == sprint_id))
    sprint = result.scalar_one_or_none()
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    sprint.status = "cancelled"
    sprint.closed_by = admin_id
    await db.commit()
    return {"status": "cancelled", "id": str(sprint_id)}


# --- Users ---

@router.get("/users")
async def list_users(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(
            User.id,
            User.email,
            User.name,
            User.role,
            User.direction,
            User.created_at,
            func.coalesce(func.sum(TrophyEvent.trophies), 0).label("total_trophies"),
        )
        .outerjoin(TrophyEvent, TrophyEvent.user_id == User.id)
        .group_by(User.id, User.email, User.name, User.role, User.direction, User.created_at)
        .order_by(User.created_at.desc())
    )
    rows = result.all()
    return [
        {
            "id": str(r[0]),
            "email": r[1],
            "name": r[2],
            "role": r[3],
            "direction": r[4],
            "created_at": r[5].isoformat() if r[5] else None,
            "total_trophies": r[6],
        }
        for r in rows
    ]


# --- Stats ---

@router.get("/stats")
async def platform_stats(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    users_count = (await db.execute(select(func.count()).select_from(User))).scalar()
    courses_count = (await db.execute(select(func.count()).select_from(Course))).scalar()
    total_trophies = (await db.execute(select(func.coalesce(func.sum(TrophyEvent.trophies), 0)))).scalar()

    active_sprint = await trophy_service.get_active_sprint(db)
    sprint_info = None
    if active_sprint:
        sprint_info = {
            "id": str(active_sprint.id),
            "title": active_sprint.title,
            "end_date": active_sprint.end_date.isoformat(),
        }

    return {
        "total_users": users_count,
        "total_courses": courses_count,
        "total_trophies": total_trophies,
        "active_sprint": sprint_info,
    }
