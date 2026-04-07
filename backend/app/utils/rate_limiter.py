from fastapi import HTTPException, Request

from app.redis import get_redis_client


async def rate_limit(request: Request, max_requests: int = 20, window_seconds: int = 60):
    """Rate limit by user. Call after authentication so request.state.user_id exists."""
    user_id = getattr(request.state, "user_id", "anon")
    r = get_redis_client()
    key = f"rate:{user_id}:{request.url.path}"
    try:
        count = await r.incr(key)
        if count == 1:
            await r.expire(key, window_seconds)
        if count > max_requests:
            raise HTTPException(status_code=429, detail="Too many requests")
    finally:
        await r.aclose()
