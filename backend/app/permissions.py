import uuid
from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user_id
from app.models.user import User
from app.models.role import Role, RolePermission, UserRole

PERMISSIONS = [
    "org.settings.edit", "org.branding.edit", "org.billing.manage",
    "users.invite", "users.remove", "users.view_all", "users.edit_roles",
    "departments.create", "departments.edit", "departments.delete", "departments.manage_members",
    "courses.create", "courses.edit", "courses.delete", "courses.publish", "courses.assign",
    "paths.create", "paths.edit", "paths.assign",
    "progress.view_own", "progress.view_department", "progress.view_all", "progress.export",
    "analytics.view_department", "analytics.view_all",
]

SYSTEM_ROLE_PERMISSIONS = {
    "admin": [p for p in PERMISSIONS if p != "org.billing.manage"],
    "manager": [
        "departments.manage_members", "courses.assign",
        "progress.view_own", "progress.view_department",
        "analytics.view_department", "users.view_all",
    ],
    "employee": ["progress.view_own"],
}

async def get_user_permissions(db: AsyncSession, user_id: uuid.UUID) -> set[str]:
    result = await db.execute(
        select(RolePermission.permission)
        .join(UserRole, UserRole.role_id == RolePermission.role_id)
        .where(UserRole.user_id == user_id)
    )
    return set(result.scalars().all())

async def get_user_roles(db: AsyncSession, user_id: uuid.UUID) -> list[Role]:
    result = await db.execute(
        select(Role).join(UserRole, UserRole.role_id == Role.id).where(UserRole.user_id == user_id)
    )
    return list(result.scalars().all())

async def check_permission(db: AsyncSession, user_id: uuid.UUID, permission: str) -> None:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    if user.is_superadmin:
        return
    roles = await get_user_roles(db, user_id)
    if any(r.slug == "owner" for r in roles):
        return
    perms = await get_user_permissions(db, user_id)
    if permission not in perms:
        raise HTTPException(status_code=403, detail="Insufficient permissions")

def require_permission(permission: str):
    async def _checker(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
        await check_permission(db, user_id, permission)
        return user_id
    return _checker
