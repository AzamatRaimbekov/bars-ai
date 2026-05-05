import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organization import Organization, Department, UserDepartment
from app.models.role import Role, RolePermission, UserRole
from app.models.user import User
from app.permissions import SYSTEM_ROLE_PERMISSIONS


async def create_organization(db: AsyncSession, owner_id: uuid.UUID, name: str, slug: str) -> Organization:
    existing = await db.execute(select(Organization).where(Organization.slug == slug))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Slug already taken")

    org = Organization(name=name, slug=slug, owner_id=owner_id)
    db.add(org)
    await db.flush()

    user = await db.get(User, owner_id)
    user.organization_id = org.id

    for role_slug, permissions in [
        ("owner", []),
        ("admin", SYSTEM_ROLE_PERMISSIONS["admin"]),
        ("manager", SYSTEM_ROLE_PERMISSIONS["manager"]),
        ("employee", SYSTEM_ROLE_PERMISSIONS["employee"]),
    ]:
        role = Role(
            organization_id=org.id,
            name=role_slug.capitalize(),
            slug=role_slug,
            is_system=True,
        )
        db.add(role)
        await db.flush()
        for perm in permissions:
            db.add(RolePermission(role_id=role.id, permission=perm))

    owner_role = await db.execute(
        select(Role).where(Role.organization_id == org.id, Role.slug == "owner")
    )
    owner_role = owner_role.scalar_one()
    db.add(UserRole(user_id=owner_id, role_id=owner_role.id, assigned_by=owner_id))

    await db.commit()
    await db.refresh(org)
    return org


async def get_organization(db: AsyncSession, org_id: uuid.UUID) -> Organization:
    org = await db.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


async def update_organization(db: AsyncSession, org_id: uuid.UUID, data: dict) -> Organization:
    org = await db.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    for key, value in data.items():
        setattr(org, key, value)
    await db.commit()
    await db.refresh(org)
    return org


# --- Departments ---

async def create_department(db: AsyncSession, org_id: uuid.UUID, name: str, parent_id: uuid.UUID | None, head_id: uuid.UUID | None) -> Department:
    if parent_id:
        depth = 1
        current_id = parent_id
        while current_id:
            parent = await db.get(Department, current_id)
            if not parent or parent.organization_id != org_id:
                raise HTTPException(status_code=400, detail="Invalid parent department")
            current_id = parent.parent_id
            depth += 1
            if depth > 3:
                raise HTTPException(status_code=400, detail="Maximum 3 levels of nesting")

    dept = Department(organization_id=org_id, name=name, parent_id=parent_id, head_id=head_id)
    db.add(dept)
    await db.commit()
    await db.refresh(dept)
    return dept


async def list_departments(db: AsyncSession, org_id: uuid.UUID) -> list[Department]:
    result = await db.execute(
        select(Department).where(Department.organization_id == org_id).order_by(Department.name)
    )
    return list(result.scalars().all())


async def update_department(db: AsyncSession, org_id: uuid.UUID, dept_id: uuid.UUID, data: dict) -> Department:
    dept = await db.get(Department, dept_id)
    if not dept or dept.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Department not found")
    for key, value in data.items():
        setattr(dept, key, value)
    await db.commit()
    await db.refresh(dept)
    return dept


async def delete_department(db: AsyncSession, org_id: uuid.UUID, dept_id: uuid.UUID) -> None:
    dept = await db.get(Department, dept_id)
    if not dept or dept.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Department not found")
    await db.delete(dept)
    await db.commit()


async def add_member(db: AsyncSession, org_id: uuid.UUID, dept_id: uuid.UUID, user_id: uuid.UUID) -> None:
    dept = await db.get(Department, dept_id)
    if not dept or dept.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Department not found")
    user = await db.get(User, user_id)
    if not user or user.organization_id != org_id:
        raise HTTPException(status_code=400, detail="User not in this organization")
    existing = await db.execute(
        select(UserDepartment).where(
            UserDepartment.user_id == user_id,
            UserDepartment.department_id == dept_id,
        )
    )
    if existing.scalar_one_or_none():
        return
    db.add(UserDepartment(user_id=user_id, department_id=dept_id))
    await db.commit()


async def remove_member(db: AsyncSession, org_id: uuid.UUID, dept_id: uuid.UUID, user_id: uuid.UUID) -> None:
    dept = await db.get(Department, dept_id)
    if not dept or dept.organization_id != org_id:
        raise HTTPException(status_code=404, detail="Department not found")
    result = await db.execute(
        select(UserDepartment).where(
            UserDepartment.user_id == user_id,
            UserDepartment.department_id == dept_id,
        )
    )
    membership = result.scalar_one_or_none()
    if membership:
        await db.delete(membership)
        await db.commit()
