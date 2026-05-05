import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser
from app.permissions import require_permission
from app.schemas.organization import (
    CreateDepartmentRequest, UpdateDepartmentRequest, DepartmentResponse, AddMemberRequest,
)
from app.services import organization_service

router = APIRouter(prefix="/api/departments", tags=["departments"])


@router.post("/", response_model=DepartmentResponse)
async def create_department(
    body: CreateDepartmentRequest,
    user_id=Depends(require_permission("departments.create")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await organization_service.create_department(db, user.org_id, body.name, body.parent_id, body.head_id)


@router.get("/", response_model=list[DepartmentResponse])
async def list_departments(
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if not user.org_id:
        return []
    return await organization_service.list_departments(db, user.org_id)


@router.patch("/{dept_id}", response_model=DepartmentResponse)
async def update_department(
    dept_id: uuid.UUID,
    body: UpdateDepartmentRequest,
    user_id=Depends(require_permission("departments.edit")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await organization_service.update_department(db, user.org_id, dept_id, body.model_dump(exclude_none=True))


@router.delete("/{dept_id}", status_code=204)
async def delete_department(
    dept_id: uuid.UUID,
    user_id=Depends(require_permission("departments.delete")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await organization_service.delete_department(db, user.org_id, dept_id)


@router.post("/{dept_id}/members", status_code=204)
async def add_member(
    dept_id: uuid.UUID,
    body: AddMemberRequest,
    user_id=Depends(require_permission("departments.manage_members")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await organization_service.add_member(db, user.org_id, dept_id, body.user_id)


@router.delete("/{dept_id}/members/{target_user_id}", status_code=204)
async def remove_member(
    dept_id: uuid.UUID,
    target_user_id: uuid.UUID,
    user_id=Depends(require_permission("departments.manage_members")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await organization_service.remove_member(db, user.org_id, dept_id, target_user_id)
