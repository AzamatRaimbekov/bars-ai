import uuid
from datetime import datetime, timezone, timedelta

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sprint import Sprint, TrophyEvent
from app.models.user import User

TROPHY_VALUES = {
    "lesson_complete": 1,
    "section_complete": 3,
    "course_complete": 10,
    "battle_win": 5,
    "pose_check_90": 2,
    "streak_7": 3,
    "streak_30": 10,
    "first_enroll": 1,
    "daily_quest": 1,
}


async def get_active_sprint(db: AsyncSession) -> Sprint | None:
    now = datetime.now(timezone.utc)
    result = await db.execute(
        select(Sprint).where(Sprint.status == "active", Sprint.start_date <= now, Sprint.end_date >= now)
    )
    return result.scalar_one_or_none()


async def auto_create_sprint(db: AsyncSession) -> Sprint:
    """Create a new sprint if none is active."""
    now = datetime.now(timezone.utc)
    sprint_num_result = await db.execute(select(func.count()).select_from(Sprint))
    num = (sprint_num_result.scalar() or 0) + 1

    sprint = Sprint(
        title=f"Спринт #{num}",
        start_date=now,
        end_date=now + timedelta(days=21),
        status="active",
    )
    db.add(sprint)
    await db.flush()
    return sprint


async def ensure_active_sprint(db: AsyncSession) -> Sprint:
    sprint = await get_active_sprint(db)
    if not sprint:
        sprint = await auto_create_sprint(db)
    return sprint


async def award_trophies(db: AsyncSession, user_id: uuid.UUID, action: str, metadata: dict | None = None) -> int:
    trophies = TROPHY_VALUES.get(action, 0)
    if trophies == 0:
        return 0

    sprint = await get_active_sprint(db)

    event = TrophyEvent(
        user_id=user_id,
        sprint_id=sprint.id if sprint else None,
        action=action,
        trophies=trophies,
        metadata_json=metadata,
    )
    db.add(event)
    return trophies


async def get_user_trophies(db: AsyncSession, user_id: uuid.UUID, sprint_id: uuid.UUID | None = None) -> dict:
    # Total trophies all time
    total_q = select(func.coalesce(func.sum(TrophyEvent.trophies), 0)).where(TrophyEvent.user_id == user_id)
    total_result = await db.execute(total_q)
    total = total_result.scalar()

    # Sprint trophies
    sprint_total = 0
    if sprint_id:
        sprint_q = select(func.coalesce(func.sum(TrophyEvent.trophies), 0)).where(
            TrophyEvent.user_id == user_id, TrophyEvent.sprint_id == sprint_id
        )
        sprint_result = await db.execute(sprint_q)
        sprint_total = sprint_result.scalar()

    return {"total": total, "sprint": sprint_total}


async def get_sprint_leaderboard(db: AsyncSession, sprint_id: uuid.UUID, limit: int = 50) -> list[dict]:
    result = await db.execute(
        select(
            TrophyEvent.user_id,
            func.sum(TrophyEvent.trophies).label("total"),
            User.name,
            User.avatar_url,
        )
        .join(User, TrophyEvent.user_id == User.id)
        .where(TrophyEvent.sprint_id == sprint_id)
        .group_by(TrophyEvent.user_id, User.name, User.avatar_url)
        .order_by(func.sum(TrophyEvent.trophies).desc())
        .limit(limit)
    )
    rows = result.all()
    return [
        {"user_id": str(r[0]), "trophies": r[1], "name": r[2], "avatar_url": r[3], "place": i + 1}
        for i, r in enumerate(rows)
    ]


async def close_sprint(db: AsyncSession, sprint_id: uuid.UUID, closed_by: uuid.UUID) -> dict:
    result = await db.execute(select(Sprint).where(Sprint.id == sprint_id))
    sprint = result.scalar_one_or_none()
    if not sprint:
        return {"error": "Sprint not found"}

    leaderboard = await get_sprint_leaderboard(db, sprint_id, limit=3)
    winners = []
    for entry in leaderboard:
        prize = next((p for p in (sprint.prizes or []) if p["place"] == entry["place"]), None)
        winners.append({
            "user_id": entry["user_id"],
            "name": entry["name"],
            "place": entry["place"],
            "trophies": entry["trophies"],
            "prize": prize,
        })

    sprint.status = "completed"
    sprint.closed_by = closed_by
    sprint.winners = winners
    return {"winners": winners}
