from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser
from app.permissions import require_permission
from app.schemas.organization import (
    CreateOrganizationRequest, UpdateOrganizationRequest, OrganizationResponse,
)
from app.services import organization_service

router = APIRouter(prefix="/api/organizations", tags=["organizations"])


@router.post("/", response_model=OrganizationResponse)
async def create_organization(
    body: CreateOrganizationRequest,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await organization_service.create_organization(db, user.id, body.name, body.slug)


@router.get("/current", response_model=OrganizationResponse)
async def get_current_organization(
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if not user.org_id:
        raise HTTPException(status_code=404, detail="Not part of an organization")
    return await organization_service.get_organization(db, user.org_id)


@router.patch("/current", response_model=OrganizationResponse)
async def update_current_organization(
    body: UpdateOrganizationRequest,
    user_id=Depends(require_permission("org.settings.edit")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await organization_service.update_organization(db, user.org_id, body.model_dump(exclude_none=True))
