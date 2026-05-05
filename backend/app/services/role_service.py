import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.role import Role, RolePermission, UserRole
from app.permissions import PERMISSIONS


async def create_role(
    db: AsyncSession, org_id: uuid.UUID, name: str, slug: str,
    description: str | None, color: str | None, permissions: list[str],
) -> dict:
    invalid = [p for p in permissions if p not in PERMISSIONS]
    if invalid:
        raise HTTPException(status_code=400, detail=f"Invalid permissions: {invalid}")

    existing = await db.execute(
        select(Role).where(Role.organization_id == org_id, Role.slug == slug)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Role slug already exists")

    role = Role(organization_id=org_id, name=name, slug=slug, description=description, color=color)
    db.add(role)
    await db.flush()

    for perm in permissions:
        db.add(RolePermission(role_id=role.id, permission=perm))

    await db.commit()
    await db.refresh(role)
    return _role_to_dict(role, permissions)


async def list_roles(db: AsyncSession, org_id: uuid.UUID) -> list[dict]:
    result = await db.execute(
        select(Role).where(Role.organization_id == org_id).order_by(Role.name)
    )
    roles = result.scalars().all()
    output = []
    for role in roles:
        perms_result = await db.execute(
            select(RolePermission.permission).where(RolePermission.role_id == role.id)
        )
        perms = list(perms_result.scalars().all())
        output.append(_role_to_dict(role, perms))
    return output


async def update_role(
    db: AsyncSession, org_id: uuid.UUID, role_id: uuid.UUID, data: dict,
) -> dict:
    role = await db.get(Role, role_id)
    if not role or role.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Role not found")
    if role.is_system and role.slug == "owner":
        raise HTTPException(status_code=400, detail="Cannot modify owner role")

    if "name" in data and data["name"] is not None:
        role.name = data["name"]
    if "description" in data:
        role.description = data["description"]
    if "color" in data:
        role.color = data["color"]

    permissions = data.get("permissions")
    if permissions is not None:
        invalid = [p for p in permissions if p not in PERMISSIONS]
        if invalid:
            raise HTTPException(status_code=400, detail=f"Invalid permissions: {invalid}")
        await db.execute(
            RolePermission.__table__.delete().where(RolePermission.role_id == role_id)
        )
        for perm in permissions:
            db.add(RolePermission(role_id=role_id, permission=perm))

    await db.commit()
    await db.refresh(role)

    perms_result = await db.execute(
        select(RolePermission.permission).where(RolePermission.role_id == role.id)
    )
    return _role_to_dict(role, list(perms_result.scalars().all()))


async def delete_role(db: AsyncSession, org_id: uuid.UUID, role_id: uuid.UUID) -> None:
    role = await db.get(Role, role_id)
    if not role or role.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Role not found")
    if role.is_system:
        raise HTTPException(status_code=400, detail="Cannot delete system role")
    await db.delete(role)
    await db.commit()


async def assign_role(db: AsyncSession, org_id: uuid.UUID, role_id: uuid.UUID, user_id: uuid.UUID, assigned_by: uuid.UUID) -> None:
    role = await db.get(Role, role_id)
    if not role or role.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Role not found")
    existing = await db.execute(
        select(UserRole).where(UserRole.user_id == user_id, UserRole.role_id == role_id)
    )
    if existing.scalar_one_or_none():
        return
    db.add(UserRole(user_id=user_id, role_id=role_id, assigned_by=assigned_by))
    await db.commit()


async def unassign_role(db: AsyncSession, org_id: uuid.UUID, role_id: uuid.UUID, user_id: uuid.UUID) -> None:
    role = await db.get(Role, role_id)
    if not role or role.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Role not found")
    if role.slug == "owner":
        raise HTTPException(status_code=400, detail="Cannot remove owner role")
    result = await db.execute(
        select(UserRole).where(UserRole.user_id == user_id, UserRole.role_id == role_id)
    )
    assignment = result.scalar_one_or_none()
    if assignment:
        await db.delete(assignment)
        await db.commit()


def _role_to_dict(role: Role, permissions: list[str]) -> dict:
    return {
        "id": role.id,
        "name": role.name,
        "slug": role.slug,
        "is_system": role.is_system,
        "description": role.description,
        "color": role.color,
        "permissions": permissions,
        "created_at": role.created_at,
    }
