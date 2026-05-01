import uuid
from dataclasses import dataclass
from typing import AsyncGenerator

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session
from app.utils.security import decode_access_token

security_scheme = HTTPBearer()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


@dataclass
class CurrentUser:
    id: uuid.UUID
    org_id: uuid.UUID | None
    is_superadmin: bool


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> CurrentUser:
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    org_id = uuid.UUID(payload["org_id"]) if payload.get("org_id") else None
    return CurrentUser(
        id=uuid.UUID(payload["sub"]),
        org_id=org_id,
        is_superadmin=payload.get("is_superadmin", False),
    )


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> uuid.UUID:
    """Backward-compatible dependency — returns just the user UUID."""
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return uuid.UUID(payload["sub"])


optional_security = HTTPBearer(auto_error=False)


async def get_optional_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(optional_security),
) -> uuid.UUID | None:
    if credentials is None:
        return None
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        return None
    return uuid.UUID(payload["sub"])


def require_superadmin():
    """Dependency that ensures the user is a superadmin."""
    async def _checker(user: CurrentUser = Depends(get_current_user)):
        if not user.is_superadmin:
            raise HTTPException(status_code=403, detail="Superadmin access required")
        return user
    return _checker
