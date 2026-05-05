import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class CreateRoleRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    slug: str = Field(min_length=1, max_length=100, pattern=r"^[a-z0-9\-]+$")
    description: str | None = None
    color: str | None = Field(None, pattern=r"^#[0-9a-fA-F]{6}$")
    permissions: list[str] = []


class UpdateRoleRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None
    color: str | None = Field(None, pattern=r"^#[0-9a-fA-F]{6}$")
    permissions: list[str] | None = None


class RoleResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    is_system: bool
    description: str | None
    color: str | None
    permissions: list[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class AssignRoleRequest(BaseModel):
    user_id: uuid.UUID
    role_id: uuid.UUID
