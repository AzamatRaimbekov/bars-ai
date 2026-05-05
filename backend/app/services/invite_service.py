import uuid
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.invite import InviteLink
from app.models.organization import Organization, UserDepartment
from app.models.role import Role, UserRole
from app.models.user import User
from app.utils.security import hash_password, create_access_token, create_refresh_token
from app.models.progress import Progress
from app.models.refresh_token import RefreshToken


async def create_invite(
    db: AsyncSession, org_id: uuid.UUID, created_by: uuid.UUID,
    department_id: uuid.UUID | None, role_id: uuid.UUID | None,
    max_uses: int | None, expires_in_days: int | None,
) -> InviteLink:
    code = secrets.token_urlsafe(16)
    expires_at = None
    if expires_in_days:
        expires_at = datetime.now(timezone.utc) + timedelta(days=expires_in_days)

    invite = InviteLink(
        organization_id=org_id,
        code=code,
        department_id=department_id,
        role_id=role_id,
        max_uses=max_uses,
        expires_at=expires_at,
        created_by=created_by,
    )
    db.add(invite)
    await db.commit()
    await db.refresh(invite)
    return invite


async def list_invites(db: AsyncSession, org_id: uuid.UUID) -> list[InviteLink]:
    result = await db.execute(
        select(InviteLink)
        .where(InviteLink.organization_id == org_id, InviteLink.is_active == True)
        .order_by(InviteLink.created_at.desc())
    )
    return list(result.scalars().all())


async def deactivate_invite(db: AsyncSession, org_id: uuid.UUID, invite_id: uuid.UUID) -> None:
    invite = await db.get(InviteLink, invite_id)
    if not invite or invite.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Invite not found")
    invite.is_active = False
    await db.commit()


async def accept_invite(
    db: AsyncSession, code: str, email: str, password: str, name: str,
) -> tuple[User, str, str]:
    """Accept invite: register user + assign to org/dept/role. Returns (user, access_token, refresh_raw)."""
    result = await db.execute(select(InviteLink).where(InviteLink.code == code, InviteLink.is_active == True))
    invite = result.scalar_one_or_none()
    if not invite:
        raise HTTPException(status_code=404, detail="Invalid or expired invite")

    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=410, detail="Invite has expired")

    if invite.max_uses and invite.used_count >= invite.max_uses:
        raise HTTPException(status_code=410, detail="Invite usage limit reached")

    org = await db.get(Organization, invite.organization_id)
    if not org or not org.is_active:
        raise HTTPException(status_code=400, detail="Organization is inactive")

    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(
        email=email,
        password=hash_password(password),
        name=name,
        direction="",
        organization_id=invite.organization_id,
    )
    db.add(user)
    await db.flush()

    db.add(Progress(user_id=user.id))

    if invite.department_id:
        db.add(UserDepartment(user_id=user.id, department_id=invite.department_id))

    if invite.role_id:
        db.add(UserRole(user_id=user.id, role_id=invite.role_id))
    else:
        emp_role = await db.execute(
            select(Role).where(
                Role.organization_id == invite.organization_id,
                Role.slug == "employee",
            )
        )
        emp = emp_role.scalar_one_or_none()
        if emp:
            db.add(UserRole(user_id=user.id, role_id=emp.id))

    invite.used_count += 1

    access_token = create_access_token(
        str(user.id),
        org_id=str(invite.organization_id),
        is_superadmin=False,
    )
    raw_refresh, token_hash = create_refresh_token()
    from app.config import settings
    refresh_expires = datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS)
    db.add(RefreshToken(user_id=user.id, token_hash=token_hash, expires_at=refresh_expires))

    await db.commit()
    await db.refresh(user)
    return user, access_token, raw_refresh
