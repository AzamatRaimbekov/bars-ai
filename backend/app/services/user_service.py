import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.user import User
from app.models.progress import Progress
from app.models.badge import UserBadge


async def get_me(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress = user.progress
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "direction": user.direction,
        "assessment_level": user.assessment_level,
        "language": user.language,
        "avatar_url": user.avatar_url,
        "created_at": user.created_at,
        "xp": progress.xp if progress else 0,
        "level": progress.level if progress else "Novice",
        "streak": progress.streak if progress else 0,
        "longest_streak": progress.longest_streak if progress else 0,
        "completed_nodes": progress.completed_nodes if progress else [],
        "completed_lessons": progress.completed_lessons if progress else [],
        "earned_badges": [b.badge_id for b in user.badges],
    }


async def update_me(db: AsyncSession, user_id: uuid.UUID, name: str | None, language: str | None, avatar_url: str | None) -> dict:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        user.name = name
    if language is not None:
        user.language = language
    if avatar_url is not None:
        user.avatar_url = avatar_url

    await db.commit()
    return await get_me(db, user_id)


async def get_public_profile(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "name": user.name,
        "direction": user.direction,
        "level": user.progress.level if user.progress else "Novice",
        "earned_badges": [b.badge_id for b in user.badges],
    }
