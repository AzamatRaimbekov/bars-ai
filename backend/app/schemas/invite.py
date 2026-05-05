import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class CreateInviteRequest(BaseModel):
    department_id: uuid.UUID | None = None
    role_id: uuid.UUID | None = None
    max_uses: int | None = Field(None, ge=1)
    expires_in_days: int | None = Field(None, ge=1, le=365)


class InviteResponse(BaseModel):
    id: uuid.UUID
    code: str
    department_id: uuid.UUID | None
    role_id: uuid.UUID | None
    max_uses: int | None
    used_count: int
    expires_at: datetime | None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class AcceptInviteRequest(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=128)
    name: str = Field(min_length=1, max_length=100)
