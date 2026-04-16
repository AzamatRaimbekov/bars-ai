import uuid
from datetime import date, datetime, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.progress import Progress
from app.models.badge import UserBadge
from app.models.user import User
from app.schemas.leagues import LEAGUE_THRESHOLDS, LEAGUE_ORDER

LEVEL_THRESHOLDS = [
    ("Novice", 0),
    ("Apprentice", 500),
    ("Practitioner", 1500),
    ("Expert", 4000),
    ("Master", 8000),
    ("Legend", 15000),
]


def _calculate_level(xp: int) -> str:
    current = "Novice"
    for name, threshold in LEVEL_THRESHOLDS:
        if xp >= threshold:
            current = name
        else:
            break
    return current


async def _get_progress(db: AsyncSession, user_id: uuid.UUID) -> Progress:
    result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    progress = result.scalar_one_or_none()
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress


def _reset_periods_if_needed(progress: Progress) -> None:
    """Reset weekly/monthly XP counters when the period changes."""
    now = datetime.now(timezone.utc)
    # Weekly reset: Monday 00:00 UTC
    current_week_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    current_week_start = current_week_start.replace(day=now.day - now.weekday())
    if progress.week_reset_at is None or progress.week_reset_at < current_week_start:
        progress.xp_this_week = 0
        progress.week_reset_at = now
    # Monthly reset: 1st of month 00:00 UTC
    current_month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if progress.month_reset_at is None or progress.month_reset_at < current_month_start:
        progress.xp_this_month = 0
        progress.month_reset_at = now


async def add_xp(db: AsyncSession, user_id: uuid.UUID, amount: int, source: str) -> dict:
    progress = await _get_progress(db, user_id)
    _reset_periods_if_needed(progress)
    old_level = progress.level
    progress.xp += amount
    progress.xp_this_week += amount
    progress.xp_this_month += amount
    progress.level = _calculate_level(progress.xp)
    await db.commit()
    return {"xp": progress.xp, "level": progress.level, "leveled_up": progress.level != old_level}


async def complete_node(db: AsyncSession, user_id: uuid.UUID, node_id: str) -> dict:
    progress = await _get_progress(db, user_id)
    if node_id not in progress.completed_nodes:
        progress.completed_nodes = [*progress.completed_nodes, node_id]
        await db.commit()
    return {"completed_nodes": progress.completed_nodes}


async def complete_lesson(db: AsyncSession, user_id: uuid.UUID, lesson_id: str) -> dict:
    progress = await _get_progress(db, user_id)
    if lesson_id not in progress.completed_lessons:
        progress.completed_lessons = [*progress.completed_lessons, lesson_id]
        await db.commit()
    return {"completed_lessons": progress.completed_lessons}


async def earn_badge(db: AsyncSession, user_id: uuid.UUID, badge_id: str) -> dict:
    existing = await db.execute(
        select(UserBadge).where(UserBadge.user_id == user_id, UserBadge.badge_id == badge_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Badge already earned")

    badge = UserBadge(user_id=user_id, badge_id=badge_id)
    db.add(badge)
    await db.commit()
    await db.refresh(badge)
    return {"badge_id": badge.badge_id, "earned_at": badge.earned_at}


async def update_streak(db: AsyncSession, user_id: uuid.UUID) -> dict:
    progress = await _get_progress(db, user_id)
    today = date.today()

    if progress.last_active_date == today:
        return {"streak": progress.streak, "longest_streak": progress.longest_streak}

    yesterday = date.fromordinal(today.toordinal() - 1)
    if progress.last_active_date == yesterday:
        progress.streak += 1
    else:
        progress.streak = 1

    if progress.streak > progress.longest_streak:
        progress.longest_streak = progress.streak

    progress.last_active_date = today
    await db.commit()
    return {"streak": progress.streak, "longest_streak": progress.longest_streak}


async def get_league_info(db: AsyncSession, user_id: uuid.UUID) -> dict:
    progress = await _get_progress(db, user_id)
    league = progress.league or "bronze"
    xp_this_week = progress.xp_this_week or 0

    # Determine next league
    idx = LEAGUE_ORDER.index(league) if league in LEAGUE_ORDER else 0
    next_league = LEAGUE_ORDER[idx + 1] if idx < len(LEAGUE_ORDER) - 1 else None
    xp_to_next = LEAGUE_THRESHOLDS[next_league] - xp_this_week if next_league else 0

    # Calculate rank within league
    result = await db.execute(
        select(Progress)
        .where(Progress.league == league)
        .order_by(Progress.xp_this_week.desc())
    )
    members = result.scalars().all()
    rank = 1
    for i, m in enumerate(members):
        if m.user_id == user_id:
            rank = i + 1
            break

    return {
        "league": league,
        "xp_this_week": xp_this_week,
        "next_league": next_league,
        "xp_to_next": max(xp_to_next, 0),
        "rank_in_league": rank,
    }


async def get_league_members(db: AsyncSession, user_id: uuid.UUID) -> list[dict]:
    progress = await _get_progress(db, user_id)
    league = progress.league or "bronze"

    result = await db.execute(
        select(Progress, User)
        .join(User, Progress.user_id == User.id)
        .where(Progress.league == league)
        .order_by(Progress.xp_this_week.desc())
        .limit(30)
    )
    rows = result.all()

    members = []
    for rank, (prog, user) in enumerate(rows, 1):
        members.append({
            "user_id": prog.user_id,
            "name": user.name,
            "avatar_url": user.avatar_url,
            "xp_this_week": prog.xp_this_week or 0,
            "rank": rank,
        })
    return members


async def get_stats(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress = user.progress
    return {
        "xp": progress.xp if progress else 0,
        "level": progress.level if progress else "Novice",
        "streak": progress.streak if progress else 0,
        "longest_streak": progress.longest_streak if progress else 0,
        "completed_nodes": progress.completed_nodes if progress else [],
        "completed_lessons": progress.completed_lessons if progress else [],
        "earned_badges": [b.badge_id for b in user.badges],
    }
