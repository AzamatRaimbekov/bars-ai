import uuid
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser, require_superadmin
from app.models.organization import Organization
from app.models.user import User
from app.models.course import Course

router = APIRouter(prefix="/api/platform-admin", tags=["platform-admin"])


class OrgListItem(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    plan: str
    is_active: bool
    user_count: int

    model_config = {"from_attributes": True}


class UpdateOrgStatusRequest(BaseModel):
    is_active: bool


class PlatformStats(BaseModel):
    total_organizations: int
    total_users: int
    total_courses: int


@router.get("/organizations")
async def list_all_organizations(
    admin: CurrentUser = Depends(require_superadmin()),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(
            Organization,
            func.count(User.id).label("user_count"),
        )
        .outerjoin(User, User.organization_id == Organization.id)
        .group_by(Organization.id)
        .order_by(Organization.created_at.desc())
    )
    orgs = []
    for org, user_count in result.all():
        orgs.append({
            "id": org.id,
            "name": org.name,
            "slug": org.slug,
            "plan": org.plan,
            "is_active": org.is_active,
            "user_count": user_count,
        })
    return orgs


@router.patch("/organizations/{org_id}/status")
async def update_org_status(
    org_id: uuid.UUID,
    body: UpdateOrgStatusRequest,
    admin: CurrentUser = Depends(require_superadmin()),
    db: AsyncSession = Depends(get_db),
):
    org = await db.get(Organization, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    org.is_active = body.is_active
    await db.commit()
    return {"id": org.id, "is_active": org.is_active}


@router.get("/stats")
async def platform_stats(
    admin: CurrentUser = Depends(require_superadmin()),
    db: AsyncSession = Depends(get_db),
):
    orgs = await db.execute(select(func.count(Organization.id)))
    users = await db.execute(select(func.count(User.id)))
    courses = await db.execute(select(func.count(Course.id)))
    return PlatformStats(
        total_organizations=orgs.scalar() or 0,
        total_users=users.scalar() or 0,
        total_courses=courses.scalar() or 0,
    )
