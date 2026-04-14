import json
import uuid

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.progress import Progress
from app.redis import get_redis_client

CACHE_TTL_SECONDS = 300  # 5 minutes
LEADERBOARD_LIMIT = 50

CACHE_KEYS = {
    "weekly": "leaderboard:weekly",
    "monthly": "leaderboard:monthly",
    "alltime": "leaderboard:alltime",
}


async def _fetch_leaderboard(db: AsyncSession) -> list[dict]:
    """
    Fetch top users ordered by XP descending.
    Since we don't have XP transaction history with timestamps,
    all periods currently return the same data (total XP).
    """
    stmt = (
        select(
            User.id,
            User.name,
            User.avatar_url,
            User.direction,
            Progress.xp,
            Progress.level,
        )
        .join(Progress, Progress.user_id == User.id)
        .order_by(Progress.xp.desc())
        .limit(LEADERBOARD_LIMIT)
    )
    result = await db.execute(stmt)
    rows = result.all()

    entries = []
    for rank, row in enumerate(rows, start=1):
        entries.append({
            "rank": rank,
            "user_id": str(row.id),
            "name": row.name,
            "avatar_url": row.avatar_url,
            "xp": row.xp,
            "level": row.level,
            "direction": row.direction,
        })
    return entries


async def get_leaderboard(db: AsyncSession, period: str) -> dict:
    cache_key = CACHE_KEYS.get(period, CACHE_KEYS["alltime"])
    redis = get_redis_client()

    try:
        cached = await redis.get(cache_key)
        if cached:
            return {"period": period, "entries": json.loads(cached)}
    except Exception:
        pass  # Redis unavailable — fall through to DB

    entries = await _fetch_leaderboard(db)

    try:
        await redis.setex(cache_key, CACHE_TTL_SECONDS, json.dumps(entries))
    except Exception:
        pass  # Redis unavailable — ignore

    return {"period": period, "entries": entries}


async def get_my_rank(db: AsyncSession, user_id: uuid.UUID) -> dict:
    """Return the current user's rank in each period."""
    # Get total user count
    count_stmt = select(func.count()).select_from(Progress)
    count_result = await db.execute(count_stmt)
    total_users = count_result.scalar() or 0

    # Get user's XP
    user_stmt = select(Progress.xp).where(Progress.user_id == user_id)
    user_result = await db.execute(user_stmt)
    user_xp_row = user_result.scalar_one_or_none()

    if user_xp_row is None:
        no_rank = {"period": "", "rank": None, "total_users": total_users}
        return {
            "weekly": {**no_rank, "period": "weekly"},
            "monthly": {**no_rank, "period": "monthly"},
            "all_time": {**no_rank, "period": "alltime"},
        }

    user_xp = user_xp_row

    # Count how many users have more XP than current user
    rank_stmt = select(func.count()).select_from(Progress).where(Progress.xp > user_xp)
    rank_result = await db.execute(rank_stmt)
    rank = (rank_result.scalar() or 0) + 1

    # Since we don't have per-period XP history, all periods share the same rank
    return {
        "weekly": {"period": "weekly", "rank": rank, "total_users": total_users},
        "monthly": {"period": "monthly", "rank": rank, "total_users": total_users},
        "all_time": {"period": "alltime", "rank": rank, "total_users": total_users},
    }
