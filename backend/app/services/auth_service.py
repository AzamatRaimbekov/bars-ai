from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.user import User, PasswordResetToken
from app.models.progress import Progress
from app.models.refresh_token import RefreshToken
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_token,
)
from app.services import email_service


async def register(db: AsyncSession, email: str, password: str, name: str, direction: str, assessment_level: str, language: str) -> tuple[User, str, str]:
    """Register user. Returns (user, access_token, raw_refresh_token)."""
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(
        email=email,
        password=hash_password(password),
        name=name,
        direction=direction,
        assessment_level=assessment_level,
        language=language,
    )
    db.add(user)
    await db.flush()

    progress = Progress(user_id=user.id)
    db.add(progress)

    access_token = create_access_token(str(user.id))
    raw_refresh, token_hash = create_refresh_token()
    rt = RefreshToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(rt)
    await db.commit()
    await db.refresh(user)

    return user, access_token, raw_refresh


async def login(db: AsyncSession, email: str, password: str) -> tuple[User, str, str]:
    """Login user. Returns (user, access_token, raw_refresh_token)."""
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(str(user.id))
    raw_refresh, token_hash = create_refresh_token()
    rt = RefreshToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(rt)
    await db.commit()

    return user, access_token, raw_refresh


async def refresh(db: AsyncSession, raw_token: str) -> tuple[str, str]:
    """Refresh tokens. Returns (new_access_token, new_raw_refresh_token)."""
    token_hash = hash_token(raw_token)
    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == token_hash,
            RefreshToken.revoked == False,
            RefreshToken.expires_at > datetime.now(timezone.utc),
        )
    )
    rt = result.scalar_one_or_none()
    if not rt:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    rt.revoked = True

    access_token = create_access_token(str(rt.user_id))
    new_raw, new_hash = create_refresh_token()
    new_rt = RefreshToken(
        user_id=rt.user_id,
        token_hash=new_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(new_rt)
    await db.commit()

    return access_token, new_raw


async def logout(db: AsyncSession, raw_token: str) -> None:
    """Revoke all refresh tokens for the user (not just the current one)."""
    token_hash = hash_token(raw_token)
    result = await db.execute(select(RefreshToken).where(RefreshToken.token_hash == token_hash))
    rt = result.scalar_one_or_none()
    if rt:
        # Revoke ALL tokens for this user
        all_tokens_result = await db.execute(
            select(RefreshToken).where(
                RefreshToken.user_id == rt.user_id,
                RefreshToken.revoked == False,
            )
        )
        for token in all_tokens_result.scalars():
            token.revoked = True
        await db.commit()


async def request_password_reset(db: AsyncSession, email: str) -> None:
    """Generate reset token and send email. Silent if email not found (security)."""
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        return  # Don't reveal if email exists

    # Invalidate previous tokens
    prev = await db.execute(
        select(PasswordResetToken).where(
            PasswordResetToken.user_id == user.id,
            PasswordResetToken.used == False,
        )
    )
    for t in prev.scalars():
        t.used = True

    # Create new token
    raw_token, token_hash_val = create_refresh_token()  # reuse the uuid-based generator
    reset_token = PasswordResetToken(
        user_id=user.id,
        token_hash=token_hash_val,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )
    db.add(reset_token)
    await db.commit()

    await email_service.send_reset_email(user.email, raw_token)


async def reset_password(db: AsyncSession, raw_token: str, new_password: str) -> None:
    """Verify token and set new password."""
    token_hash_val = hash_token(raw_token)
    result = await db.execute(
        select(PasswordResetToken).where(
            PasswordResetToken.token_hash == token_hash_val,
            PasswordResetToken.used == False,
            PasswordResetToken.expires_at > datetime.now(timezone.utc),
        )
    )
    rt = result.scalar_one_or_none()
    if not rt:
        raise HTTPException(status_code=400, detail="Invalid or expired reset token")

    rt.used = True

    user_result = await db.execute(select(User).where(User.id == rt.user_id))
    user = user_result.scalar_one()
    user.password = hash_password(new_password)
    await db.commit()
