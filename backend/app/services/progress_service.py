import uuid
from datetime import date

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.progress import Progress
from app.models.badge import UserBadge
from app.models.user import User

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


async def add_xp(db: AsyncSession, user_id: uuid.UUID, amount: int, source: str) -> dict:
    progress = await _get_progress(db, user_id)
    old_level = progress.level
    progress.xp += amount
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
