# B2B SaaS Phase 1 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform Bars AI from B2C into multi-tenant B2B SaaS with organizations, departments, custom roles (RBAC), invite system, and adapted onboarding.

**Architecture:** Shared database with `organization_id` tenant isolation. RBAC via Role + RolePermission tables with union-based permission checking. Two admin levels: Platform Admin (superadmin) and Org Admin (company admin). Invite links with auto-assignment to department/role.

**Tech Stack:** FastAPI, SQLAlchemy 2.0 (async), Alembic, PostgreSQL, Pydantic v2, python-jose JWT

**Spec:** `docs/superpowers/specs/2026-05-01-b2b-saas-phase1-design.md`

---

## File Structure

### New files to create:

| File | Responsibility |
|------|---------------|
| `backend/app/models/organization.py` | Organization, Department, UserDepartment models |
| `backend/app/models/role.py` | Role, RolePermission, UserRole models |
| `backend/app/models/invite.py` | InviteLink model |
| `backend/app/schemas/organization.py` | Pydantic schemas for org/department endpoints |
| `backend/app/schemas/role.py` | Pydantic schemas for role endpoints |
| `backend/app/schemas/invite.py` | Pydantic schemas for invite endpoints |
| `backend/app/services/organization_service.py` | Org CRUD, department management |
| `backend/app/services/role_service.py` | Role CRUD, permission checking |
| `backend/app/services/invite_service.py` | Invite link creation, acceptance |
| `backend/app/routers/organizations.py` | /api/organizations endpoints |
| `backend/app/routers/departments.py` | /api/departments endpoints |
| `backend/app/routers/roles.py` | /api/roles endpoints |
| `backend/app/routers/invites.py` | /api/invites endpoints |
| `backend/app/routers/platform_admin.py` | /api/platform-admin endpoints |
| `backend/app/permissions.py` | PERMISSIONS list + require_permission dependency |
| `backend/alembic/versions/b2b_saas_phase1.py` | Migration for all new tables + columns |

### Existing files to modify:

| File | Changes |
|------|---------|
| `backend/app/models/user.py` | Add `organization_id`, `is_superadmin` columns |
| `backend/app/models/course.py` | Add `organization_id` column |
| `backend/app/models/__init__.py` | Import new models |
| `backend/app/utils/security.py` | Extend JWT payload with `org_id`, `is_superadmin` |
| `backend/app/dependencies.py` | Add `get_current_user` (full user), `get_org_id` dependencies |
| `backend/app/services/auth_service.py` | Pass org_id into JWT on login/register |
| `backend/app/main.py` | Register new routers |
| `backend/alembic/env.py` | Import new models for autogenerate |

---

## Task 1: Organization & Department Models

**Files:**
- Create: `backend/app/models/organization.py`
- Modify: `backend/app/models/user.py`
- Modify: `backend/app/models/course.py`
- Modify: `backend/app/models/__init__.py`

- [ ] **Step 1: Create organization models file**

```python
# backend/app/models/organization.py
import uuid
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    logo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    primary_color: Mapped[str | None] = mapped_column(String(7), nullable=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    plan: Mapped[str] = mapped_column(String(50), default="free")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", foreign_keys=[owner_id])
    departments: Mapped[list["Department"]] = relationship(back_populates="organization", cascade="all, delete-orphan")


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    parent_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    head_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("organization_id", "name", "parent_id", name="uq_dept_org_name_parent"),
    )

    organization: Mapped["Organization"] = relationship(back_populates="departments")
    parent = relationship("Department", remote_side="Department.id", backref="children")
    head = relationship("User", foreign_keys=[head_id])


class UserDepartment(Base):
    __tablename__ = "user_departments"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    department_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("departments.id", ondelete="CASCADE"), primary_key=True)
    joined_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
```

- [ ] **Step 2: Add organization_id and is_superadmin to User model**

In `backend/app/models/user.py`, add after the `updated_at` field:

```python
    organization_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True)
    is_superadmin: Mapped[bool] = mapped_column(Boolean, default=False)
```

Add relationship after existing relationships:

```python
    organization = relationship("Organization", foreign_keys=[organization_id])
```

- [ ] **Step 3: Add organization_id to Course model**

In `backend/app/models/course.py`, add after the `author_id` field:

```python
    organization_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True)
```

- [ ] **Step 4: Update models __init__.py**

Replace content of `backend/app/models/__init__.py`:

```python
from app.models.user import User, PasswordResetToken
from app.models.progress import Progress
from app.models.badge import UserBadge
from app.models.refresh_token import RefreshToken
from app.models.course import (
    Course, CourseSection, CourseLesson,
    CourseEnrollment, CourseLessonProgress, CourseReview,
)
from app.models.mentor import MentorSession, MentorMessage, KnowledgeProfile
from app.models.sprint import Sprint, TrophyEvent
from app.models.payment import PaymentRequest
from app.models.notification import Notification
from app.models.organization import Organization, Department, UserDepartment
from app.models.role import Role, RolePermission, UserRole
from app.models.invite import InviteLink

__all__ = [
    "User", "PasswordResetToken", "Progress", "UserBadge", "RefreshToken",
    "Course", "CourseSection", "CourseLesson",
    "CourseEnrollment", "CourseLessonProgress", "CourseReview",
    "MentorSession", "MentorMessage", "KnowledgeProfile",
    "Sprint", "TrophyEvent",
    "PaymentRequest", "Notification",
    "Organization", "Department", "UserDepartment",
    "Role", "RolePermission", "UserRole",
    "InviteLink",
]
```

- [ ] **Step 5: Commit**

```bash
git add backend/app/models/organization.py backend/app/models/user.py backend/app/models/course.py backend/app/models/__init__.py
git commit -m "feat: add Organization, Department, UserDepartment models + org_id on User/Course"
```

---

## Task 2: Role & Permission Models

**Files:**
- Create: `backend/app/models/role.py`
- Create: `backend/app/permissions.py`

- [ ] **Step 1: Create role models file**

```python
# backend/app/models/role.py
import uuid
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    is_system: Mapped[bool] = mapped_column(Boolean, default=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    color: Mapped[str | None] = mapped_column(String(7), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("organization_id", "slug", name="uq_role_org_slug"),
    )

    permissions: Mapped[list["RolePermission"]] = relationship(back_populates="role", cascade="all, delete-orphan")


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    permission: Mapped[str] = mapped_column(String(100), primary_key=True)

    role: Mapped["Role"] = relationship(back_populates="permissions")


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    assigned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    assigned_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
```

- [ ] **Step 2: Create permissions module**

```python
# backend/app/permissions.py
import uuid

from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.models.user import User
from app.models.role import Role, RolePermission, UserRole

PERMISSIONS = [
    # Organization
    "org.settings.edit",
    "org.branding.edit",
    "org.billing.manage",
    # Users
    "users.invite",
    "users.remove",
    "users.view_all",
    "users.edit_roles",
    # Departments
    "departments.create",
    "departments.edit",
    "departments.delete",
    "departments.manage_members",
    # Courses
    "courses.create",
    "courses.edit",
    "courses.delete",
    "courses.publish",
    "courses.assign",
    # Learning Paths (Phase 2)
    "paths.create",
    "paths.edit",
    "paths.assign",
    # Progress
    "progress.view_own",
    "progress.view_department",
    "progress.view_all",
    "progress.export",
    # Analytics (Phase 3)
    "analytics.view_department",
    "analytics.view_all",
]

# Permissions for each system role
SYSTEM_ROLE_PERMISSIONS = {
    "admin": [p for p in PERMISSIONS if p != "org.billing.manage"],
    "manager": [
        "departments.manage_members",
        "courses.assign",
        "progress.view_own",
        "progress.view_department",
        "analytics.view_department",
        "users.view_all",
    ],
    "employee": [
        "progress.view_own",
    ],
}


async def get_user_permissions(db: AsyncSession, user_id: uuid.UUID) -> set[str]:
    """Get union of all permissions from all roles assigned to user."""
    result = await db.execute(
        select(RolePermission.permission)
        .join(UserRole, UserRole.role_id == RolePermission.role_id)
        .where(UserRole.user_id == user_id)
    )
    return set(result.scalars().all())


async def get_user_roles(db: AsyncSession, user_id: uuid.UUID) -> list[Role]:
    """Get all roles assigned to user."""
    result = await db.execute(
        select(Role)
        .join(UserRole, UserRole.role_id == Role.id)
        .where(UserRole.user_id == user_id)
    )
    return list(result.scalars().all())


async def check_permission(db: AsyncSession, user_id: uuid.UUID, permission: str) -> None:
    """Raise 403 if user doesn't have the permission. Owner and superadmin bypass."""
    # Check superadmin
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    if user.is_superadmin:
        return

    # Check owner role
    roles = await get_user_roles(db, user_id)
    if any(r.slug == "owner" for r in roles):
        return

    # Check permissions
    perms = await get_user_permissions(db, user_id)
    if permission not in perms:
        raise HTTPException(status_code=403, detail="Insufficient permissions")


def require_permission(permission: str):
    """FastAPI dependency factory for permission checking."""
    async def _checker(
        user_id: uuid.UUID = Depends(get_current_user_id),
        db: AsyncSession = Depends(get_db),
    ):
        await check_permission(db, user_id, permission)
        return user_id
    return _checker
```

- [ ] **Step 3: Commit**

```bash
git add backend/app/models/role.py backend/app/permissions.py
git commit -m "feat: add Role, RolePermission, UserRole models + permissions module"
```

---

## Task 3: InviteLink Model

**Files:**
- Create: `backend/app/models/invite.py`

- [ ] **Step 1: Create invite model file**

```python
# backend/app/models/invite.py
import uuid
from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class InviteLink(Base):
    __tablename__ = "invite_links"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    department_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    role_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("roles.id", ondelete="SET NULL"), nullable=True)
    max_uses: Mapped[int | None] = mapped_column(Integer, nullable=True)
    used_count: Mapped[int] = mapped_column(Integer, default=0)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_by: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    organization = relationship("Organization")
    department = relationship("Department")
    role = relationship("Role")
    creator = relationship("User", foreign_keys=[created_by])
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/models/invite.py
git commit -m "feat: add InviteLink model"
```

---

## Task 4: Alembic Migration

**Files:**
- Create: `backend/alembic/versions/b2b_saas_phase1_multitenant.py`
- Modify: `backend/alembic/env.py`

- [ ] **Step 1: Update alembic env.py to import new models**

At the top of `backend/alembic/env.py`, after existing model imports, add:

```python
from app.models.organization import Organization, Department, UserDepartment  # noqa: F401
from app.models.role import Role, RolePermission, UserRole  # noqa: F401
from app.models.invite import InviteLink  # noqa: F401
```

- [ ] **Step 2: Generate migration**

Run from `backend/` directory:

```bash
cd backend && alembic revision --autogenerate -m "b2b_saas_phase1_multitenant"
```

- [ ] **Step 3: Review and run migration**

```bash
cd backend && alembic upgrade head
```

Expected: 6 new tables created (`organizations`, `departments`, `user_departments`, `roles`, `role_permissions`, `user_roles`, `invite_links`) + 2 new columns on `users` (`organization_id`, `is_superadmin`) + 1 new column on `courses` (`organization_id`).

- [ ] **Step 4: Commit**

```bash
git add backend/alembic/
git commit -m "feat: add b2b saas phase 1 migration"
```

---

## Task 5: Extend JWT & Dependencies

**Files:**
- Modify: `backend/app/utils/security.py`
- Modify: `backend/app/dependencies.py`
- Modify: `backend/app/services/auth_service.py`

- [ ] **Step 1: Extend create_access_token to accept org_id and is_superadmin**

In `backend/app/utils/security.py`, replace `create_access_token`:

```python
def create_access_token(user_id: str, org_id: str | None = None, is_superadmin: bool = False) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_EXPIRE_MINUTES)
    payload = {
        "sub": user_id,
        "exp": expire,
        "type": "access",
    }
    if org_id:
        payload["org_id"] = org_id
    if is_superadmin:
        payload["is_superadmin"] = True
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)
```

Update `decode_access_token` to return a dict:

```python
def decode_access_token(token: str) -> dict | None:
    """Returns payload dict with sub, org_id, is_superadmin or None if invalid."""
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            return None
        return {
            "sub": payload.get("sub"),
            "org_id": payload.get("org_id"),
            "is_superadmin": payload.get("is_superadmin", False),
        }
    except JWTError:
        return None
```

- [ ] **Step 2: Update dependencies.py**

Replace the content of `backend/app/dependencies.py`:

```python
import uuid
from dataclasses import dataclass
from typing import AsyncGenerator

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session
from app.utils.security import decode_access_token

security_scheme = HTTPBearer()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


@dataclass
class CurrentUser:
    id: uuid.UUID
    org_id: uuid.UUID | None
    is_superadmin: bool


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> CurrentUser:
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    org_id = uuid.UUID(payload["org_id"]) if payload.get("org_id") else None
    return CurrentUser(
        id=uuid.UUID(payload["sub"]),
        org_id=org_id,
        is_superadmin=payload.get("is_superadmin", False),
    )


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> uuid.UUID:
    """Backward-compatible dependency — returns just the user UUID."""
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return uuid.UUID(payload["sub"])


optional_security = HTTPBearer(auto_error=False)


async def get_optional_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(optional_security),
) -> uuid.UUID | None:
    if credentials is None:
        return None
    payload = decode_access_token(credentials.credentials)
    if payload is None:
        return None
    return uuid.UUID(payload["sub"])


def require_superadmin():
    """Dependency that ensures the user is a superadmin."""
    async def _checker(user: CurrentUser = Depends(get_current_user)):
        if not user.is_superadmin:
            raise HTTPException(status_code=403, detail="Superadmin access required")
        return user
    return _checker
```

- [ ] **Step 3: Update auth_service.py to pass org_id into JWT**

In `backend/app/services/auth_service.py`, update the `register` and `login` functions. Where `create_access_token(str(user.id))` is called, change to:

```python
access_token = create_access_token(
    str(user.id),
    org_id=str(user.organization_id) if user.organization_id else None,
    is_superadmin=user.is_superadmin,
)
```

Also update the `refresh` function similarly — after loading the user from the refresh token, pass org_id and is_superadmin.

- [ ] **Step 4: Commit**

```bash
git add backend/app/utils/security.py backend/app/dependencies.py backend/app/services/auth_service.py
git commit -m "feat: extend JWT with org_id and is_superadmin, add CurrentUser dependency"
```

---

## Task 6: Pydantic Schemas

**Files:**
- Create: `backend/app/schemas/organization.py`
- Create: `backend/app/schemas/role.py`
- Create: `backend/app/schemas/invite.py`

- [ ] **Step 1: Create organization schemas**

```python
# backend/app/schemas/organization.py
import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class CreateOrganizationRequest(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    slug: str = Field(min_length=2, max_length=100, pattern=r"^[a-z0-9\-]+$")


class UpdateOrganizationRequest(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=255)
    logo_url: str | None = None
    primary_color: str | None = Field(None, pattern=r"^#[0-9a-fA-F]{6}$")


class OrganizationResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    logo_url: str | None
    primary_color: str | None
    plan: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class CreateDepartmentRequest(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    parent_id: uuid.UUID | None = None
    head_id: uuid.UUID | None = None


class UpdateDepartmentRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=255)
    parent_id: uuid.UUID | None = None
    head_id: uuid.UUID | None = None


class DepartmentResponse(BaseModel):
    id: uuid.UUID
    name: str
    parent_id: uuid.UUID | None
    head_id: uuid.UUID | None
    created_at: datetime

    model_config = {"from_attributes": True}


class AddMemberRequest(BaseModel):
    user_id: uuid.UUID
```

- [ ] **Step 2: Create role schemas**

```python
# backend/app/schemas/role.py
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
```

- [ ] **Step 3: Create invite schemas**

```python
# backend/app/schemas/invite.py
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
```

- [ ] **Step 4: Commit**

```bash
git add backend/app/schemas/organization.py backend/app/schemas/role.py backend/app/schemas/invite.py
git commit -m "feat: add Pydantic schemas for organizations, roles, invites"
```

---

## Task 7: Organization Service

**Files:**
- Create: `backend/app/services/organization_service.py`

- [ ] **Step 1: Create organization service**

```python
# backend/app/services/organization_service.py
import uuid

from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organization import Organization, Department, UserDepartment
from app.models.role import Role, RolePermission, UserRole
from app.models.user import User
from app.permissions import SYSTEM_ROLE_PERMISSIONS


async def create_organization(db: AsyncSession, owner_id: uuid.UUID, name: str, slug: str) -> Organization:
    # Check slug uniqueness
    existing = await db.execute(select(Organization).where(Organization.slug == slug))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Slug already taken")

    org = Organization(name=name, slug=slug, owner_id=owner_id)
    db.add(org)
    await db.flush()

    # Update user's organization_id
    user = await db.get(User, owner_id)
    user.organization_id = org.id

    # Create system roles
    for role_slug, permissions in [
        ("owner", []),  # owner has implicit all-permissions
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

    # Assign owner role to the creator
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
    # Validate nesting depth (max 3 levels)
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
        return  # already a member
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
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/services/organization_service.py
git commit -m "feat: add organization and department service"
```

---

## Task 8: Role Service

**Files:**
- Create: `backend/app/services/role_service.py`

- [ ] **Step 1: Create role service**

```python
# backend/app/services/role_service.py
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
    # Validate permissions
    invalid = [p for p in permissions if p not in PERMISSIONS]
    if invalid:
        raise HTTPException(status_code=400, detail=f"Invalid permissions: {invalid}")

    # Check slug uniqueness within org
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
        # Replace all permissions
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
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/services/role_service.py
git commit -m "feat: add role service with CRUD and assignment"
```

---

## Task 9: Invite Service

**Files:**
- Create: `backend/app/services/invite_service.py`

- [ ] **Step 1: Create invite service**

```python
# backend/app/services/invite_service.py
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
    # Find invite
    result = await db.execute(select(InviteLink).where(InviteLink.code == code, InviteLink.is_active == True))
    invite = result.scalar_one_or_none()
    if not invite:
        raise HTTPException(status_code=404, detail="Invalid or expired invite")

    # Check expiry
    if invite.expires_at and invite.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=410, detail="Invite has expired")

    # Check usage limit
    if invite.max_uses and invite.used_count >= invite.max_uses:
        raise HTTPException(status_code=410, detail="Invite usage limit reached")

    # Check org is active
    org = await db.get(Organization, invite.organization_id)
    if not org or not org.is_active:
        raise HTTPException(status_code=400, detail="Organization is inactive")

    # Check email not taken
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    # Create user
    user = User(
        email=email,
        password=hash_password(password),
        name=name,
        direction="",
        organization_id=invite.organization_id,
    )
    db.add(user)
    await db.flush()

    # Create progress record
    db.add(Progress(user_id=user.id))

    # Assign to department
    if invite.department_id:
        db.add(UserDepartment(user_id=user.id, department_id=invite.department_id))

    # Assign role (or default employee)
    if invite.role_id:
        db.add(UserRole(user_id=user.id, role_id=invite.role_id))
    else:
        # Assign default "employee" role
        emp_role = await db.execute(
            select(Role).where(
                Role.organization_id == invite.organization_id,
                Role.slug == "employee",
            )
        )
        emp = emp_role.scalar_one_or_none()
        if emp:
            db.add(UserRole(user_id=user.id, role_id=emp.id))

    # Increment used_count
    invite.used_count += 1

    # Create tokens
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
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/services/invite_service.py
git commit -m "feat: add invite service with create, list, accept"
```

---

## Task 10: API Routers — Organizations & Departments

**Files:**
- Create: `backend/app/routers/organizations.py`
- Create: `backend/app/routers/departments.py`

- [ ] **Step 1: Create organizations router**

```python
# backend/app/routers/organizations.py
from fastapi import APIRouter, Depends
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
        from fastapi import HTTPException
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
```

- [ ] **Step 2: Create departments router**

```python
# backend/app/routers/departments.py
from fastapi import APIRouter, Depends
import uuid
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
```

- [ ] **Step 3: Commit**

```bash
git add backend/app/routers/organizations.py backend/app/routers/departments.py
git commit -m "feat: add organizations and departments API routers"
```

---

## Task 11: API Routers — Roles & Invites

**Files:**
- Create: `backend/app/routers/roles.py`
- Create: `backend/app/routers/invites.py`

- [ ] **Step 1: Create roles router**

```python
# backend/app/routers/roles.py
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
```

- [ ] **Step 2: Create invites router**

```python
# backend/app/routers/invites.py
import os

from fastapi import APIRouter, Depends, Response
import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser
from app.permissions import require_permission
from app.schemas.invite import CreateInviteRequest, InviteResponse, AcceptInviteRequest
from app.schemas.auth import TokenResponse
from app.services import invite_service

router = APIRouter(prefix="/api/invites", tags=["invites"])

COOKIE_KEY = "refresh_token"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60


def _set_refresh_cookie(response: Response, raw_token: str):
    response.set_cookie(
        key=COOKIE_KEY,
        value=raw_token,
        httponly=True,
        secure=os.getenv("ENV", "dev") != "dev",
        samesite="lax",
        max_age=COOKIE_MAX_AGE,
        path="/",
    )


@router.post("/", response_model=InviteResponse)
async def create_invite(
    body: CreateInviteRequest,
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await invite_service.create_invite(
        db, user.org_id, user.id, body.department_id, body.role_id, body.max_uses, body.expires_in_days,
    )


@router.get("/", response_model=list[InviteResponse])
async def list_invites(
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await invite_service.list_invites(db, user.org_id)


@router.delete("/{invite_id}", status_code=204)
async def deactivate_invite(
    invite_id: uuid.UUID,
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await invite_service.deactivate_invite(db, user.org_id, invite_id)


@router.post("/join/{code}", response_model=TokenResponse)
async def accept_invite(
    code: str,
    body: AcceptInviteRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    user, access_token, raw_refresh = await invite_service.accept_invite(
        db, code, body.email, body.password, body.name,
    )
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)
```

- [ ] **Step 3: Commit**

```bash
git add backend/app/routers/roles.py backend/app/routers/invites.py
git commit -m "feat: add roles and invites API routers"
```

---

## Task 12: Platform Admin Router

**Files:**
- Create: `backend/app/routers/platform_admin.py`

- [ ] **Step 1: Create platform admin router**

```python
# backend/app/routers/platform_admin.py
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
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/routers/platform_admin.py
git commit -m "feat: add platform admin router for superadmin"
```

---

## Task 13: Register New Routers in main.py

**Files:**
- Modify: `backend/app/main.py`

- [ ] **Step 1: Add new router imports and registrations**

In `backend/app/main.py`, add to the import block (after existing router imports):

```python
from app.routers import organizations, departments, roles, invites, platform_admin
```

Add to the `app.include_router()` block:

```python
app.include_router(organizations.router)
app.include_router(departments.router)
app.include_router(roles.router)
app.include_router(invites.router)
app.include_router(platform_admin.router)
```

- [ ] **Step 2: Verify server starts**

```bash
cd backend && uvicorn app.main:app --reload --port 3847
```

Expected: server starts without import errors, new routes visible at `/docs`.

- [ ] **Step 3: Commit**

```bash
git add backend/app/main.py
git commit -m "feat: register organization, department, role, invite, platform-admin routers"
```

---

## Task 14: Verify Full Integration

- [ ] **Step 1: Start the backend server**

```bash
cd backend && uvicorn app.main:app --reload --port 3847
```

- [ ] **Step 2: Check that all new endpoints appear in Swagger**

Open http://localhost:3847/docs and verify these endpoint groups exist:
- `/api/organizations` (3 endpoints)
- `/api/departments` (6 endpoints)
- `/api/roles` (7 endpoints)
- `/api/invites` (4 endpoints)
- `/api/platform-admin` (3 endpoints)

- [ ] **Step 3: Test basic flow manually via Swagger**

1. Register a user via POST `/api/auth/register`
2. Create organization via POST `/api/organizations/`
3. Get current org via GET `/api/organizations/current`
4. Create department via POST `/api/departments/`
5. List roles via GET `/api/roles/`
6. Create invite via POST `/api/invites/`

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "feat: B2B SaaS Phase 1 complete — multi-tenant organizations, departments, RBAC, invites"
```
