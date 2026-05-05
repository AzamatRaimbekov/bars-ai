import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser
from app.permissions import require_permission, PERMISSIONS
from app.schemas.role import CreateRoleRequest, UpdateRoleRequest, RoleResponse, AssignRoleRequest
from app.services import role_service

router = APIRouter(prefix="/api/roles", tags=["roles"])


@router.post("/", response_model=RoleResponse)
async def create_role(
    body: CreateRoleRequest,
    user_id=Depends(require_permission("users.edit_roles")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await role_service.create_role(db, user.org_id, body.name, body.slug, body.description, body.color, body.permissions)


@router.get("/", response_model=list[RoleResponse])
async def list_roles(
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if not user.org_id:
        return []
    return await role_service.list_roles(db, user.org_id)


@router.patch("/{role_id}", response_model=RoleResponse)
async def update_role(
    role_id: uuid.UUID,
    body: UpdateRoleRequest,
    user_id=Depends(require_permission("users.edit_roles")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await role_service.update_role(db, user.org_id, role_id, body.model_dump(exclude_none=True))


@router.delete("/{role_id}", status_code=204)
async def delete_role(
    role_id: uuid.UUID,
    user_id=Depends(require_permission("users.edit_roles")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await role_service.delete_role(db, user.org_id, role_id)


@router.get("/permissions")
async def list_permissions(
    user_id=Depends(require_permission("users.edit_roles")),
):
    return {"permissions": PERMISSIONS}


@router.post("/assign", status_code=204)
async def assign_role(
    body: AssignRoleRequest,
    user_id=Depends(require_permission("users.edit_roles")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await role_service.assign_role(db, user.org_id, body.role_id, body.user_id, user.id)


@router.delete("/{role_id}/assign/{target_user_id}", status_code=204)
async def unassign_role(
    role_id: uuid.UUID,
    target_user_id: uuid.UUID,
    user_id=Depends(require_permission("users.edit_roles")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await role_service.unassign_role(db, user.org_id, role_id, target_user_id)
