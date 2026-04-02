# Stage 1: Backend Foundation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a FastAPI backend with PostgreSQL + Redis, JWT/OAuth auth, and migrate the frontend from localStorage to API-driven state.

**Architecture:** FastAPI app with SQLAlchemy ORM, Alembic migrations, Redis for sessions/caching. Frontend keeps Zustand stores but syncs with backend API instead of localStorage. Claude API calls move to backend to protect API keys.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0, Alembic, asyncpg, Redis (aioredis), Pydantic v2, python-jose (JWT), httpx (Claude API), pytest + httpx (testing)

---

## File Structure

### Backend (`backend/`)

```
backend/
├── pyproject.toml
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app, CORS, lifespan
│   ├── config.py                  # Settings via pydantic-settings
│   ├── database.py                # SQLAlchemy async engine + session
│   ├── redis.py                   # Redis connection
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                # User model
│   │   └── progress.py            # Progress, CompletedNode, CompletedLesson, EarnedBadge
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py                # Login, Register, Token schemas
│   │   ├── user.py                # UserProfile, UserUpdate schemas
│   │   └── progress.py            # XP, streak, node/lesson completion schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py                # /api/auth/* endpoints
│   │   ├── users.py               # /api/users/* endpoints
│   │   ├── progress.py            # /api/progress/* endpoints
│   │   └── ai.py                  # /api/ai/* endpoints (Claude proxy)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py        # JWT creation/validation, password hashing
│   │   ├── user_service.py        # User CRUD
│   │   ├── progress_service.py    # XP, streak, node/lesson logic
│   │   └── claude_service.py      # Claude API calls
│   └── middleware/
│       ├── __init__.py
│       └── auth.py                # get_current_user dependency
├── tests/
│   ├── conftest.py                # Fixtures: test DB, client, auth headers
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_progress.py
│   └── test_ai.py
└── .env.example
```

### Frontend changes (`src/`)

```
src/
├── services/
│   ├── api.ts                     # New: axios/fetch wrapper with JWT
│   ├── authApi.ts                 # New: login, register, refresh
│   ├── userApi.ts                 # New: profile CRUD
│   ├── progressApi.ts             # New: XP, nodes, lessons, badges
│   └── claudeApi.ts               # Modified: proxy through backend
├── store/
│   ├── authStore.ts               # New: JWT tokens, auth state
│   └── userStore.ts               # Modified: sync with backend
├── hooks/
│   └── useAuth.ts                 # New: login/register/logout logic
├── components/
│   └── auth/
│       ├── LoginForm.tsx          # New
│       ├── RegisterForm.tsx       # New
│       └── AuthGuard.tsx          # New: replaces inline check in App.tsx
└── pages/
    ├── Login.tsx                  # New
    └── Register.tsx               # New
```

---

## Task 1: Backend Project Scaffold

**Files:**
- Create: `backend/pyproject.toml`
- Create: `backend/app/__init__.py`
- Create: `backend/app/main.py`
- Create: `backend/app/config.py`
- Create: `backend/.env.example`

- [ ] **Step 1: Create pyproject.toml**

```toml
[project]
name = "pathmind-backend"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.34.0",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.30.0",
    "alembic>=1.14.0",
    "pydantic-settings>=2.7.0",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
    "httpx>=0.28.0",
    "redis>=5.2.0",
    "python-multipart>=0.0.20",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.25.0",
    "httpx>=0.28.0",
    "aiosqlite>=0.20.0",
]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

- [ ] **Step 2: Create config.py**

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/pathmind"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    anthropic_api_key: str = ""
    claude_model: str = "claude-sonnet-4-20250514"
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = {"env_file": ".env", "env_prefix": "PATHMIND_"}


settings = Settings()
```

- [ ] **Step 3: Create main.py**

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine
from app.models import Base
from app.routers import auth, users, progress, ai


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(title="PathMind API", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(progress.router, prefix="/api/progress", tags=["progress"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])


@app.get("/api/health")
async def health():
    return {"status": "ok"}
```

- [ ] **Step 4: Create .env.example**

```env
PATHMIND_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/pathmind
PATHMIND_REDIS_URL=redis://localhost:6379/0
PATHMIND_SECRET_KEY=your-secret-key-here
PATHMIND_ANTHROPIC_API_KEY=your-anthropic-key-here
```

- [ ] **Step 5: Create __init__.py files**

```python
# backend/app/__init__.py
# empty
```

- [ ] **Step 6: Verify project structure**

Run:
```bash
cd backend && ls -la app/ && cat pyproject.toml
```
Expected: All files present, pyproject.toml readable.

- [ ] **Step 7: Commit**

```bash
git add backend/pyproject.toml backend/app/__init__.py backend/app/main.py backend/app/config.py backend/.env.example
git commit -m "feat(backend): scaffold FastAPI project with config"
```

---

## Task 2: Database Setup (SQLAlchemy + Alembic)

**Files:**
- Create: `backend/app/database.py`
- Create: `backend/app/models/__init__.py`
- Create: `backend/app/models/user.py`
- Create: `backend/app/models/progress.py`
- Create: `backend/alembic.ini`
- Create: `backend/alembic/env.py`

- [ ] **Step 1: Create database.py**

```python
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.config import settings

engine = create_async_engine(settings.database_url, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session
```

- [ ] **Step 2: Create User model**

```python
# backend/app/models/user.py
import uuid
from datetime import datetime, date

from sqlalchemy import String, Boolean, Integer, Date, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

import enum


class DirectionEnum(str, enum.Enum):
    frontend = "frontend"
    english = "english"
    callcenter = "callcenter"
    cib = "cib"


class LevelEnum(str, enum.Enum):
    Novice = "Novice"
    Apprentice = "Apprentice"
    Practitioner = "Practitioner"
    Expert = "Expert"
    Master = "Master"
    Legend = "Legend"


class AssessmentLevelEnum(str, enum.Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(100))
    direction: Mapped[DirectionEnum | None] = mapped_column(SAEnum(DirectionEnum), nullable=True)
    level: Mapped[LevelEnum] = mapped_column(SAEnum(LevelEnum), default=LevelEnum.Novice)
    xp: Mapped[int] = mapped_column(Integer, default=0)
    streak: Mapped[int] = mapped_column(Integer, default=0)
    last_active_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    assessment_level: Mapped[AssessmentLevelEnum | None] = mapped_column(
        SAEnum(AssessmentLevelEnum), nullable=True
    )
    onboarding_complete: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # OAuth fields
    google_id: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)
    github_id: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)

    completed_nodes: Mapped[list["CompletedNode"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    completed_lessons: Mapped[list["CompletedLesson"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    earned_badges: Mapped[list["EarnedBadge"]] = relationship(back_populates="user", cascade="all, delete-orphan")
```

- [ ] **Step 3: Create Progress models**

```python
# backend/app/models/progress.py
import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class CompletedNode(Base):
    __tablename__ = "completed_nodes"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    node_id: Mapped[str] = mapped_column(String(50))
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="completed_nodes")


class CompletedLesson(Base):
    __tablename__ = "completed_lessons"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    lesson_id: Mapped[str] = mapped_column(String(50))
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="completed_lessons")


class EarnedBadge(Base):
    __tablename__ = "earned_badges"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    badge_id: Mapped[str] = mapped_column(String(50))
    earned_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="earned_badges")
```

- [ ] **Step 4: Create models __init__.py with Base**

```python
# backend/app/models/__init__.py
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User
from app.models.progress import CompletedNode, CompletedLesson, EarnedBadge
```

- [ ] **Step 5: Create alembic.ini**

```ini
[alembic]
script_location = alembic
sqlalchemy.url = postgresql+asyncpg://postgres:postgres@localhost:5432/pathmind

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

- [ ] **Step 6: Create alembic/env.py**

```python
import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import settings
from app.models import Base

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    url = settings.database_url
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    connectable = create_async_engine(settings.database_url)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
```

- [ ] **Step 7: Create alembic/versions/ directory**

```bash
mkdir -p backend/alembic/versions && touch backend/alembic/versions/.gitkeep
```

- [ ] **Step 8: Commit**

```bash
git add backend/app/database.py backend/app/models/ backend/alembic.ini backend/alembic/
git commit -m "feat(backend): add database models and Alembic setup"
```

---

## Task 3: Auth Schemas and Service

**Files:**
- Create: `backend/app/schemas/__init__.py`
- Create: `backend/app/schemas/auth.py`
- Create: `backend/app/services/__init__.py`
- Create: `backend/app/services/auth_service.py`
- Create: `backend/app/middleware/__init__.py`
- Create: `backend/app/middleware/auth.py`

- [ ] **Step 1: Create auth schemas**

```python
# backend/app/schemas/__init__.py
# empty

# backend/app/schemas/auth.py
from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str
```

- [ ] **Step 2: Create auth service**

```python
# backend/app/services/__init__.py
# empty

# backend/app/services/auth_service.py
import uuid
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(user_id: uuid.UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": str(user_id), "exp": expire, "type": "access"}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def create_refresh_token(user_id: uuid.UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
    payload = {"sub": str(user_id), "exp": expire, "type": "refresh"}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None
```

- [ ] **Step 3: Create auth middleware (get_current_user)**

```python
# backend/app/middleware/__init__.py
# empty

# backend/app/middleware/auth.py
import uuid

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.services.auth_service import decode_token

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    payload = decode_token(credentials.credentials)
    if payload is None or payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    result = await db.execute(select(User).where(User.id == uuid.UUID(user_id)))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user
```

- [ ] **Step 4: Commit**

```bash
git add backend/app/schemas/ backend/app/services/auth_service.py backend/app/middleware/
git commit -m "feat(backend): add auth schemas, service, and middleware"
```

---

## Task 4: Auth Router (Register, Login, Refresh)

**Files:**
- Create: `backend/app/routers/__init__.py`
- Create: `backend/app/routers/auth.py`
- Create: `backend/tests/conftest.py`
- Create: `backend/tests/test_auth.py`

- [ ] **Step 1: Write failing tests for auth**

```python
# backend/tests/conftest.py
import asyncio
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.models import Base
from app.database import get_db
from app.main import app

TEST_DB_URL = "sqlite+aiosqlite:///./test.db"
test_engine = create_async_engine(TEST_DB_URL, echo=False)
TestSession = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(autouse=True)
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db():
    async with TestSession() as session:
        yield session


@pytest.fixture
async def client():
    async def override_get_db():
        async with TestSession() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
async def auth_headers(client: AsyncClient) -> dict:
    await client.post("/api/auth/register", json={
        "email": "test@test.com",
        "password": "testpass123",
        "name": "Test User",
    })
    resp = await client.post("/api/auth/login", json={
        "email": "test@test.com",
        "password": "testpass123",
    })
    token = resp.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

```python
# backend/tests/test_auth.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "user@example.com",
        "password": "password123",
        "name": "New User",
    })
    assert resp.status_code == 201
    data = resp.json()
    assert "access_token" in data
    assert "refresh_token" in data


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    payload = {"email": "dup@example.com", "password": "pass123", "name": "Dup"}
    await client.post("/api/auth/register", json=payload)
    resp = await client.post("/api/auth/register", json=payload)
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient):
    await client.post("/api/auth/register", json={
        "email": "login@example.com",
        "password": "pass123",
        "name": "Login User",
    })
    resp = await client.post("/api/auth/login", json={
        "email": "login@example.com",
        "password": "pass123",
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient):
    await client.post("/api/auth/register", json={
        "email": "wrong@example.com",
        "password": "correct",
        "name": "Wrong",
    })
    resp = await client.post("/api/auth/login", json={
        "email": "wrong@example.com",
        "password": "incorrect",
    })
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient):
    reg = await client.post("/api/auth/register", json={
        "email": "refresh@example.com",
        "password": "pass123",
        "name": "Refresh",
    })
    refresh_token = reg.json()["refresh_token"]
    resp = await client.post("/api/auth/refresh", json={
        "refresh_token": refresh_token,
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && pip install -e ".[dev]" && pytest tests/test_auth.py -v`
Expected: FAIL — routers not implemented yet

- [ ] **Step 3: Implement auth router**

```python
# backend/app/routers/__init__.py
# empty

# backend/app/routers/auth.py
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, RefreshRequest
from app.services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)

router = APIRouter()


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == body.email))
    if result.scalar_one_or_none() is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(
        email=body.email,
        hashed_password=hash_password(body.password),
        name=body.name,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return TokenResponse(
        access_token=create_access_token(user.id),
        refresh_token=create_refresh_token(user.id),
    )


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()
    if user is None or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return TokenResponse(
        access_token=create_access_token(user.id),
        refresh_token=create_refresh_token(user.id),
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh(body: RefreshRequest, db: AsyncSession = Depends(get_db)):
    payload = decode_token(body.refresh_token)
    if payload is None or payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    user_id = payload.get("sub")
    result = await db.execute(select(User).where(User.id == uuid.UUID(user_id)))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return TokenResponse(
        access_token=create_access_token(user.id),
        refresh_token=create_refresh_token(user.id),
    )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_auth.py -v`
Expected: All 5 tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/routers/ backend/tests/
git commit -m "feat(backend): implement auth endpoints with tests"
```

---

## Task 5: User Profile Router

**Files:**
- Create: `backend/app/schemas/user.py`
- Create: `backend/app/routers/users.py`
- Create: `backend/tests/test_users.py`

- [ ] **Step 1: Create user schemas**

```python
# backend/app/schemas/user.py
import uuid
from datetime import date, datetime

from pydantic import BaseModel

from app.models.user import DirectionEnum, LevelEnum, AssessmentLevelEnum


class UserProfileResponse(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    direction: DirectionEnum | None
    level: LevelEnum
    xp: int
    streak: int
    last_active_date: date | None
    assessment_level: AssessmentLevelEnum | None
    onboarding_complete: bool
    completed_nodes: list[str]
    completed_lessons: list[str]
    earned_badges: list[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class UserUpdateRequest(BaseModel):
    name: str | None = None
    direction: DirectionEnum | None = None
    assessment_level: AssessmentLevelEnum | None = None
    onboarding_complete: bool | None = None
```

- [ ] **Step 2: Write failing tests**

```python
# backend/tests/test_users.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_profile(client: AsyncClient, auth_headers: dict):
    resp = await client.get("/api/users/me", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@test.com"
    assert data["level"] == "Novice"
    assert data["xp"] == 0


@pytest.mark.asyncio
async def test_get_profile_unauthorized(client: AsyncClient):
    resp = await client.get("/api/users/me")
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_update_profile(client: AsyncClient, auth_headers: dict):
    resp = await client.patch("/api/users/me", headers=auth_headers, json={
        "name": "Updated Name",
        "direction": "frontend",
    })
    assert resp.status_code == 200
    assert resp.json()["name"] == "Updated Name"
    assert resp.json()["direction"] == "frontend"


@pytest.mark.asyncio
async def test_complete_onboarding(client: AsyncClient, auth_headers: dict):
    resp = await client.patch("/api/users/me", headers=auth_headers, json={
        "direction": "frontend",
        "assessment_level": "beginner",
        "onboarding_complete": True,
    })
    assert resp.status_code == 200
    assert resp.json()["onboarding_complete"] is True
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd backend && pytest tests/test_users.py -v`
Expected: FAIL — router not implemented

- [ ] **Step 4: Implement users router**

```python
# backend/app/routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.middleware.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserProfileResponse, UserUpdateRequest

router = APIRouter()


def _user_to_response(user: User) -> UserProfileResponse:
    return UserProfileResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        direction=user.direction,
        level=user.level,
        xp=user.xp,
        streak=user.streak,
        last_active_date=user.last_active_date,
        assessment_level=user.assessment_level,
        onboarding_complete=user.onboarding_complete,
        completed_nodes=[cn.node_id for cn in user.completed_nodes],
        completed_lessons=[cl.lesson_id for cl in user.completed_lessons],
        earned_badges=[eb.badge_id for eb in user.earned_badges],
        created_at=user.created_at,
    )


@router.get("/me", response_model=UserProfileResponse)
async def get_profile(user: User = Depends(get_current_user)):
    return _user_to_response(user)


@router.patch("/me", response_model=UserProfileResponse)
async def update_profile(
    body: UserUpdateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    update_data = body.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)
    await db.commit()
    await db.refresh(user)
    return _user_to_response(user)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_users.py -v`
Expected: All 4 tests PASS

- [ ] **Step 6: Commit**

```bash
git add backend/app/schemas/user.py backend/app/routers/users.py backend/tests/test_users.py
git commit -m "feat(backend): implement user profile endpoints with tests"
```

---

## Task 6: Progress Router (XP, Streaks, Nodes, Lessons, Badges)

**Files:**
- Create: `backend/app/schemas/progress.py`
- Create: `backend/app/services/progress_service.py`
- Create: `backend/app/routers/progress.py`
- Create: `backend/tests/test_progress.py`

- [ ] **Step 1: Create progress schemas**

```python
# backend/app/schemas/progress.py
from pydantic import BaseModel


class AddXPRequest(BaseModel):
    amount: int
    reason: str  # "lesson", "quiz", "interview", "streak"


class AddXPResponse(BaseModel):
    xp: int
    level: str
    leveled_up: bool
    new_level: str | None


class CompleteNodeRequest(BaseModel):
    node_id: str


class CompleteLessonRequest(BaseModel):
    lesson_id: str


class EarnBadgeRequest(BaseModel):
    badge_id: str


class StreakResponse(BaseModel):
    streak: int
    updated: bool
```

- [ ] **Step 2: Create progress service**

```python
# backend/app/services/progress_service.py
from datetime import date, timedelta

from app.models.user import User, LevelEnum

LEVEL_THRESHOLDS: dict[LevelEnum, int] = {
    LevelEnum.Novice: 0,
    LevelEnum.Apprentice: 500,
    LevelEnum.Practitioner: 1500,
    LevelEnum.Expert: 4000,
    LevelEnum.Master: 8000,
    LevelEnum.Legend: 15000,
}

LEVELS_ORDERED = [
    LevelEnum.Novice,
    LevelEnum.Apprentice,
    LevelEnum.Practitioner,
    LevelEnum.Expert,
    LevelEnum.Master,
    LevelEnum.Legend,
]


def calculate_level(xp: int) -> LevelEnum:
    current = LevelEnum.Novice
    for level in LEVELS_ORDERED:
        if xp >= LEVEL_THRESHOLDS[level]:
            current = level
    return current


def update_streak(user: User) -> bool:
    today = date.today()
    if user.last_active_date == today:
        return False

    if user.last_active_date == today - timedelta(days=1):
        user.streak += 1
    else:
        user.streak = 1

    user.last_active_date = today
    return True
```

- [ ] **Step 3: Write failing tests**

```python
# backend/tests/test_progress.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_xp(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/xp", headers=auth_headers, json={
        "amount": 500,
        "reason": "lesson",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["xp"] == 500
    assert data["leveled_up"] is True
    assert data["new_level"] == "Apprentice"


@pytest.mark.asyncio
async def test_add_xp_no_level_up(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/xp", headers=auth_headers, json={
        "amount": 50,
        "reason": "lesson",
    })
    assert resp.status_code == 200
    assert resp.json()["leveled_up"] is False
    assert resp.json()["new_level"] is None


@pytest.mark.asyncio
async def test_complete_node(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/nodes", headers=auth_headers, json={
        "node_id": "fe-1",
    })
    assert resp.status_code == 200
    assert "fe-1" in resp.json()["completed_nodes"]


@pytest.mark.asyncio
async def test_complete_node_duplicate(client: AsyncClient, auth_headers: dict):
    await client.post("/api/progress/nodes", headers=auth_headers, json={"node_id": "fe-1"})
    resp = await client.post("/api/progress/nodes", headers=auth_headers, json={"node_id": "fe-1"})
    assert resp.status_code == 200
    assert resp.json()["completed_nodes"].count("fe-1") == 1


@pytest.mark.asyncio
async def test_complete_lesson(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/lessons", headers=auth_headers, json={
        "lesson_id": "fe-1-1",
    })
    assert resp.status_code == 200
    assert "fe-1-1" in resp.json()["completed_lessons"]


@pytest.mark.asyncio
async def test_earn_badge(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/badges", headers=auth_headers, json={
        "badge_id": "first-step",
    })
    assert resp.status_code == 200
    assert "first-step" in resp.json()["earned_badges"]


@pytest.mark.asyncio
async def test_update_streak(client: AsyncClient, auth_headers: dict):
    resp = await client.post("/api/progress/streak", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["streak"] == 1
    assert resp.json()["updated"] is True


@pytest.mark.asyncio
async def test_update_streak_same_day(client: AsyncClient, auth_headers: dict):
    await client.post("/api/progress/streak", headers=auth_headers)
    resp = await client.post("/api/progress/streak", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["streak"] == 1
    assert resp.json()["updated"] is False
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `cd backend && pytest tests/test_progress.py -v`
Expected: FAIL — router not implemented

- [ ] **Step 5: Implement progress router**

```python
# backend/app/routers/progress.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.middleware.auth import get_current_user
from app.models.user import User
from app.models.progress import CompletedNode, CompletedLesson, EarnedBadge
from app.schemas.progress import (
    AddXPRequest, AddXPResponse,
    CompleteNodeRequest, CompleteLessonRequest, EarnBadgeRequest,
    StreakResponse,
)
from app.services.progress_service import calculate_level, update_streak

router = APIRouter()


@router.post("/xp", response_model=AddXPResponse)
async def add_xp(
    body: AddXPRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    old_level = user.level
    user.xp += body.amount
    new_level = calculate_level(user.xp)
    leveled_up = new_level != old_level
    user.level = new_level
    await db.commit()

    return AddXPResponse(
        xp=user.xp,
        level=new_level.value,
        leveled_up=leveled_up,
        new_level=new_level.value if leveled_up else None,
    )


@router.post("/nodes")
async def complete_node(
    body: CompleteNodeRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    existing = [cn.node_id for cn in user.completed_nodes]
    if body.node_id not in existing:
        node = CompletedNode(user_id=user.id, node_id=body.node_id)
        db.add(node)
        await db.commit()
        await db.refresh(user)

    return {"completed_nodes": [cn.node_id for cn in user.completed_nodes]}


@router.post("/lessons")
async def complete_lesson(
    body: CompleteLessonRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    existing = [cl.lesson_id for cl in user.completed_lessons]
    if body.lesson_id not in existing:
        lesson = CompletedLesson(user_id=user.id, lesson_id=body.lesson_id)
        db.add(lesson)
        await db.commit()
        await db.refresh(user)

    return {"completed_lessons": [cl.lesson_id for cl in user.completed_lessons]}


@router.post("/badges")
async def earn_badge(
    body: EarnBadgeRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    existing = [eb.badge_id for eb in user.earned_badges]
    if body.badge_id not in existing:
        badge = EarnedBadge(user_id=user.id, badge_id=body.badge_id)
        db.add(badge)
        await db.commit()
        await db.refresh(user)

    return {"earned_badges": [eb.badge_id for eb in user.earned_badges]}


@router.post("/streak", response_model=StreakResponse)
async def post_streak(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    updated = update_streak(user)
    await db.commit()
    return StreakResponse(streak=user.streak, updated=updated)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_progress.py -v`
Expected: All 8 tests PASS

- [ ] **Step 7: Commit**

```bash
git add backend/app/schemas/progress.py backend/app/services/progress_service.py backend/app/routers/progress.py backend/tests/test_progress.py
git commit -m "feat(backend): implement progress endpoints (XP, streak, nodes, lessons, badges)"
```

---

## Task 7: Claude API Proxy Router

**Files:**
- Create: `backend/app/services/claude_service.py`
- Create: `backend/app/routers/ai.py`
- Create: `backend/tests/test_ai.py`

- [ ] **Step 1: Create Claude service**

```python
# backend/app/services/claude_service.py
import httpx

from app.config import settings

CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"


async def call_claude(
    system_prompt: str,
    messages: list[dict],
    max_tokens: int = 1024,
) -> str:
    headers = {
        "x-api-key": settings.anthropic_api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    body = {
        "model": settings.claude_model,
        "max_tokens": max_tokens,
        "system": system_prompt,
        "messages": messages,
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(CLAUDE_API_URL, headers=headers, json=body)
        resp.raise_for_status()
        data = resp.json()
        return data["content"][0]["text"]


async def assess_level(direction: str, answers: list[str], language: str = "ru") -> str:
    lang_instruction = "\n\nIMPORTANT: Respond entirely in Russian." if language == "ru" else ""
    system = (
        f"You are an assessment expert for {direction}. "
        f"Based on the student's answers, classify their level as exactly one word: "
        f"beginner, intermediate, or advanced. Respond with ONLY that one word.{lang_instruction}"
    )
    content = "\n".join(f"Answer {i+1}: {a}" for i, a in enumerate(answers))
    result = await call_claude(system, [{"role": "user", "content": content}], max_tokens=50)
    level = result.strip().lower()
    if level not in ("beginner", "intermediate", "advanced"):
        return "beginner"
    return level


async def generate_tip(direction: str, level: str, language: str = "ru") -> str:
    lang_instruction = "\n\nIMPORTANT: Respond entirely in Russian." if language == "ru" else ""
    system = (
        f"You are a learning mentor for {direction}. Generate a short, practical tip "
        f"for a {level} student. Keep it under 2 sentences.{lang_instruction}"
    )
    return await call_claude(system, [{"role": "user", "content": "Give me today's tip."}], max_tokens=256)


async def score_answer(
    question: str, answer: str, direction: str, language: str = "ru"
) -> dict:
    lang_instruction = "\n\nIMPORTANT: Respond entirely in Russian." if language == "ru" else ""
    system = (
        f"You are an interview evaluator for {direction}. Score the answer 1-10. "
        f"Respond in JSON: {{\"score\": N, \"feedback\": \"...\", \"modelAnswer\": \"...\"}}{lang_instruction}"
    )
    content = f"Question: {question}\nAnswer: {answer}"
    result = await call_claude(system, [{"role": "user", "content": content}])
    try:
        import json
        return json.loads(result)
    except (json.JSONDecodeError, KeyError):
        return {"score": 5, "feedback": result, "modelAnswer": "Could not parse response"}
```

- [ ] **Step 2: Create AI router**

```python
# backend/app/routers/ai.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.middleware.auth import get_current_user
from app.models.user import User
from app.services.claude_service import call_claude, assess_level, generate_tip, score_answer

router = APIRouter()


class ChatRequest(BaseModel):
    system_prompt: str
    messages: list[dict]
    language: str = "ru"


class ChatResponse(BaseModel):
    content: str


class AssessRequest(BaseModel):
    direction: str
    answers: list[str]
    language: str = "ru"


class AssessResponse(BaseModel):
    level: str


class TipRequest(BaseModel):
    direction: str
    level: str
    language: str = "ru"


class TipResponse(BaseModel):
    tip: str


class ScoreRequest(BaseModel):
    question: str
    answer: str
    direction: str
    language: str = "ru"


class ScoreResponse(BaseModel):
    score: int
    feedback: str
    modelAnswer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(body: ChatRequest, user: User = Depends(get_current_user)):
    lang_instruction = "\n\nIMPORTANT: Respond entirely in Russian." if body.language == "ru" else ""
    content = await call_claude(body.system_prompt + lang_instruction, body.messages)
    return ChatResponse(content=content)


@router.post("/assess", response_model=AssessResponse)
async def assess(body: AssessRequest, user: User = Depends(get_current_user)):
    level = await assess_level(body.direction, body.answers, body.language)
    return AssessResponse(level=level)


@router.post("/tip", response_model=TipResponse)
async def tip(body: TipRequest, user: User = Depends(get_current_user)):
    result = await generate_tip(body.direction, body.level, body.language)
    return TipResponse(tip=result)


@router.post("/score", response_model=ScoreResponse)
async def score(body: ScoreRequest, user: User = Depends(get_current_user)):
    result = await score_answer(body.question, body.answer, body.direction, body.language)
    return ScoreResponse(**result)
```

- [ ] **Step 3: Write tests (mocking Claude API)**

```python
# backend/tests/test_ai.py
import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient


@pytest.mark.asyncio
@patch("app.services.claude_service.call_claude", new_callable=AsyncMock)
async def test_chat(mock_claude, client: AsyncClient, auth_headers: dict):
    mock_claude.return_value = "Hello! I'm your mentor."
    resp = await client.post("/api/ai/chat", headers=auth_headers, json={
        "system_prompt": "You are a mentor.",
        "messages": [{"role": "user", "content": "Hi"}],
    })
    assert resp.status_code == 200
    assert resp.json()["content"] == "Hello! I'm your mentor."


@pytest.mark.asyncio
@patch("app.services.claude_service.call_claude", new_callable=AsyncMock)
async def test_assess(mock_claude, client: AsyncClient, auth_headers: dict):
    mock_claude.return_value = "intermediate"
    resp = await client.post("/api/ai/assess", headers=auth_headers, json={
        "direction": "frontend",
        "answers": ["ans1", "ans2", "ans3", "ans4", "ans5"],
    })
    assert resp.status_code == 200
    assert resp.json()["level"] == "intermediate"


@pytest.mark.asyncio
@patch("app.services.claude_service.call_claude", new_callable=AsyncMock)
async def test_tip(mock_claude, client: AsyncClient, auth_headers: dict):
    mock_claude.return_value = "Use semantic HTML for accessibility."
    resp = await client.post("/api/ai/tip", headers=auth_headers, json={
        "direction": "frontend",
        "level": "beginner",
    })
    assert resp.status_code == 200
    assert "semantic" in resp.json()["tip"].lower()


@pytest.mark.asyncio
@patch("app.services.claude_service.call_claude", new_callable=AsyncMock)
async def test_score(mock_claude, client: AsyncClient, auth_headers: dict):
    mock_claude.return_value = '{"score": 8, "feedback": "Good answer", "modelAnswer": "The ideal answer..."}'
    resp = await client.post("/api/ai/score", headers=auth_headers, json={
        "question": "What is closure?",
        "answer": "A function with access to outer scope.",
        "direction": "frontend",
    })
    assert resp.status_code == 200
    assert resp.json()["score"] == 8


@pytest.mark.asyncio
async def test_chat_unauthorized(client: AsyncClient):
    resp = await client.post("/api/ai/chat", json={
        "system_prompt": "test",
        "messages": [{"role": "user", "content": "hi"}],
    })
    assert resp.status_code == 403
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_ai.py -v`
Expected: All 5 tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/claude_service.py backend/app/routers/ai.py backend/tests/test_ai.py
git commit -m "feat(backend): implement Claude API proxy with tests"
```

---

## Task 8: Redis Setup

**Files:**
- Create: `backend/app/redis.py`

- [ ] **Step 1: Create Redis connection module**

```python
# backend/app/redis.py
from redis.asyncio import from_url

from app.config import settings

redis_client = from_url(settings.redis_url, decode_responses=True)


async def get_redis():
    return redis_client
```

- [ ] **Step 2: Add Redis to lifespan in main.py**

Update `backend/app/main.py` — replace the lifespan function:

```python
from app.redis import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_client.aclose()
    await engine.dispose()
```

- [ ] **Step 3: Verify Redis import works**

Run: `cd backend && python -c "from app.redis import redis_client; print('Redis module OK')"`
Expected: `Redis module OK`

- [ ] **Step 4: Commit**

```bash
git add backend/app/redis.py backend/app/main.py
git commit -m "feat(backend): add Redis connection module"
```

---

## Task 9: Run All Backend Tests

**Files:** No new files

- [ ] **Step 1: Run full test suite**

Run: `cd backend && pytest tests/ -v --tb=short`
Expected: All tests PASS (5 auth + 4 users + 8 progress + 5 ai = 22 tests)

- [ ] **Step 2: Check health endpoint**

Run: `cd backend && python -c "from app.main import app; print('App imports OK')"`
Expected: `App imports OK`

- [ ] **Step 3: Commit (if any fixes needed)**

```bash
git add -A backend/
git commit -m "fix(backend): resolve any test issues"
```

---

## Task 10: Frontend API Client

**Files:**
- Create: `src/services/api.ts`
- Create: `src/services/authApi.ts`
- Create: `src/services/userApi.ts`
- Create: `src/services/progressApi.ts`

- [ ] **Step 1: Create base API client**

```typescript
// src/services/api.ts
const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

interface RequestOptions {
  method?: string;
  body?: unknown;
  headers?: Record<string, string>;
}

async function request<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const { method = "GET", body, headers = {} } = options;

  const token = localStorage.getItem("pathmind-access-token");
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const config: RequestInit = {
    method,
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
  };

  if (body) {
    config.body = JSON.stringify(body);
  }

  const resp = await fetch(`${API_BASE}${path}`, config);

  if (resp.status === 401) {
    const refreshed = await tryRefreshToken();
    if (refreshed) {
      return request<T>(path, options);
    }
    localStorage.removeItem("pathmind-access-token");
    localStorage.removeItem("pathmind-refresh-token");
    window.location.href = "/login";
    throw new Error("Unauthorized");
  }

  if (!resp.ok) {
    const error = await resp.json().catch(() => ({ detail: "Request failed" }));
    throw new Error(error.detail || "Request failed");
  }

  return resp.json();
}

async function tryRefreshToken(): Promise<boolean> {
  const refreshToken = localStorage.getItem("pathmind-refresh-token");
  if (!refreshToken) return false;

  try {
    const resp = await fetch(`${API_BASE}/auth/refresh`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });
    if (!resp.ok) return false;
    const data = await resp.json();
    localStorage.setItem("pathmind-access-token", data.access_token);
    localStorage.setItem("pathmind-refresh-token", data.refresh_token);
    return true;
  } catch {
    return false;
  }
}

export const api = {
  get: <T>(path: string) => request<T>(path),
  post: <T>(path: string, body?: unknown) => request<T>(path, { method: "POST", body }),
  patch: <T>(path: string, body?: unknown) => request<T>(path, { method: "PATCH", body }),
  delete: <T>(path: string) => request<T>(path, { method: "DELETE" }),
};
```

- [ ] **Step 2: Create auth API**

```typescript
// src/services/authApi.ts
const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export async function registerUser(
  email: string,
  password: string,
  name: string,
): Promise<TokenResponse> {
  const resp = await fetch(`${API_BASE}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, name }),
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ detail: "Registration failed" }));
    throw new Error(err.detail);
  }
  const data: TokenResponse = await resp.json();
  localStorage.setItem("pathmind-access-token", data.access_token);
  localStorage.setItem("pathmind-refresh-token", data.refresh_token);
  return data;
}

export async function loginUser(email: string, password: string): Promise<TokenResponse> {
  const resp = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({ detail: "Invalid credentials" }));
    throw new Error(err.detail);
  }
  const data: TokenResponse = await resp.json();
  localStorage.setItem("pathmind-access-token", data.access_token);
  localStorage.setItem("pathmind-refresh-token", data.refresh_token);
  return data;
}

export function logoutUser(): void {
  localStorage.removeItem("pathmind-access-token");
  localStorage.removeItem("pathmind-refresh-token");
}

export function isAuthenticated(): boolean {
  return localStorage.getItem("pathmind-access-token") !== null;
}
```

- [ ] **Step 3: Create user API**

```typescript
// src/services/userApi.ts
import { api } from "./api";
import type { UserProfile, Direction } from "../types";

interface UserProfileResponse {
  id: string;
  email: string;
  name: string;
  direction: Direction | null;
  level: string;
  xp: number;
  streak: number;
  last_active_date: string | null;
  assessment_level: "beginner" | "intermediate" | "advanced" | null;
  onboarding_complete: boolean;
  completed_nodes: string[];
  completed_lessons: string[];
  earned_badges: string[];
}

export async function fetchProfile(): Promise<UserProfileResponse> {
  return api.get<UserProfileResponse>("/users/me");
}

export async function updateProfile(data: {
  name?: string;
  direction?: Direction;
  assessment_level?: "beginner" | "intermediate" | "advanced";
  onboarding_complete?: boolean;
}): Promise<UserProfileResponse> {
  return api.patch<UserProfileResponse>("/users/me", data);
}
```

- [ ] **Step 4: Create progress API**

```typescript
// src/services/progressApi.ts
import { api } from "./api";

interface AddXPResponse {
  xp: number;
  level: string;
  leveled_up: boolean;
  new_level: string | null;
}

export async function addXP(amount: number, reason: string): Promise<AddXPResponse> {
  return api.post<AddXPResponse>("/progress/xp", { amount, reason });
}

export async function completeNode(nodeId: string): Promise<{ completed_nodes: string[] }> {
  return api.post("/progress/nodes", { node_id: nodeId });
}

export async function completeLesson(lessonId: string): Promise<{ completed_lessons: string[] }> {
  return api.post("/progress/lessons", { lesson_id: lessonId });
}

export async function earnBadge(badgeId: string): Promise<{ earned_badges: string[] }> {
  return api.post("/progress/badges", { badge_id: badgeId });
}

export async function updateStreak(): Promise<{ streak: number; updated: boolean }> {
  return api.post("/progress/streak");
}
```

- [ ] **Step 5: Commit**

```bash
git add src/services/api.ts src/services/authApi.ts src/services/userApi.ts src/services/progressApi.ts
git commit -m "feat(frontend): add API client layer for backend integration"
```

---

## Task 11: Auth Store and Auth Pages

**Files:**
- Create: `src/store/authStore.ts`
- Create: `src/hooks/useAuth.ts`
- Create: `src/pages/Login.tsx`
- Create: `src/pages/Register.tsx`

- [ ] **Step 1: Create auth store**

```typescript
// src/store/authStore.ts
import { create } from "zustand";

interface AuthState {
  isAuthenticated: boolean;
  isLoading: boolean;
  setAuthenticated: (value: boolean) => void;
  setLoading: (value: boolean) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: localStorage.getItem("pathmind-access-token") !== null,
  isLoading: false,
  setAuthenticated: (value) => set({ isAuthenticated: value }),
  setLoading: (value) => set({ isLoading: value }),
}));
```

- [ ] **Step 2: Create useAuth hook**

```typescript
// src/hooks/useAuth.ts
import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";
import { useUserStore } from "../store/userStore";
import { registerUser, loginUser, logoutUser } from "../services/authApi";
import { fetchProfile } from "../services/userApi";

export function useAuth() {
  const navigate = useNavigate();
  const { setAuthenticated, setLoading } = useAuthStore();
  const { setProfile } = useUserStore();

  const login = useCallback(async (email: string, password: string) => {
    setLoading(true);
    try {
      await loginUser(email, password);
      const profile = await fetchProfile();
      setProfile({
        name: profile.name,
        direction: profile.direction ?? "frontend",
        level: profile.level as any,
        xp: profile.xp,
        streak: profile.streak,
        lastActiveDate: profile.last_active_date ?? "",
        completedNodes: profile.completed_nodes,
        completedLessons: profile.completed_lessons,
        earnedBadges: profile.earned_badges,
        assessmentLevel: profile.assessment_level ?? "beginner",
        onboardingComplete: profile.onboarding_complete,
      });
      setAuthenticated(true);
      navigate(profile.onboarding_complete ? "/dashboard" : "/");
    } finally {
      setLoading(false);
    }
  }, [navigate, setAuthenticated, setLoading, setProfile]);

  const register = useCallback(async (email: string, password: string, name: string) => {
    setLoading(true);
    try {
      await registerUser(email, password, name);
      setAuthenticated(true);
      navigate("/");
    } finally {
      setLoading(false);
    }
  }, [navigate, setAuthenticated, setLoading]);

  const logout = useCallback(() => {
    logoutUser();
    setAuthenticated(false);
    setProfile(null as any);
    navigate("/login");
  }, [navigate, setAuthenticated, setProfile]);

  return { login, register, logout };
}
```

- [ ] **Step 3: Create Login page**

```tsx
// src/pages/Login.tsx
import { useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { useAuthStore } from "../store/authStore";
import { t } from "../lib/i18n";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login } = useAuth();
  const { isLoading } = useAuthStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    try {
      await login(email, password);
    } catch (err: any) {
      setError(err.message || "Login failed");
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0a0f] flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-[#12121a] rounded-2xl p-8 border border-white/10">
        <h1 className="text-2xl font-bold text-white mb-2">PathMind</h1>
        <p className="text-white/60 mb-8">{t("login.subtitle")}</p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="text-sm text-white/70 block mb-1">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white focus:border-indigo-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label className="text-sm text-white/70 block mb-1">{t("login.password")}</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white focus:border-indigo-500 focus:outline-none"
              required
            />
          </div>

          {error && <p className="text-red-400 text-sm">{error}</p>}

          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg py-3 font-medium transition-colors disabled:opacity-50"
          >
            {isLoading ? "..." : t("login.submit")}
          </button>
        </form>

        <p className="text-white/50 text-sm mt-6 text-center">
          {t("login.noAccount")}{" "}
          <Link to="/register" className="text-indigo-400 hover:text-indigo-300">
            {t("login.register")}
          </Link>
        </p>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Create Register page**

```tsx
// src/pages/Register.tsx
import { useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { useAuthStore } from "../store/authStore";
import { t } from "../lib/i18n";

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { register } = useAuth();
  const { isLoading } = useAuthStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    try {
      await register(email, password, name);
    } catch (err: any) {
      setError(err.message || "Registration failed");
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0a0f] flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-[#12121a] rounded-2xl p-8 border border-white/10">
        <h1 className="text-2xl font-bold text-white mb-2">PathMind</h1>
        <p className="text-white/60 mb-8">{t("register.subtitle")}</p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="text-sm text-white/70 block mb-1">{t("register.name")}</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white focus:border-indigo-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label className="text-sm text-white/70 block mb-1">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white focus:border-indigo-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label className="text-sm text-white/70 block mb-1">{t("register.password")}</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white focus:border-indigo-500 focus:outline-none"
              minLength={6}
              required
            />
          </div>

          {error && <p className="text-red-400 text-sm">{error}</p>}

          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg py-3 font-medium transition-colors disabled:opacity-50"
          >
            {isLoading ? "..." : t("register.submit")}
          </button>
        </form>

        <p className="text-white/50 text-sm mt-6 text-center">
          {t("register.hasAccount")}{" "}
          <Link to="/login" className="text-indigo-400 hover:text-indigo-300">
            {t("register.login")}
          </Link>
        </p>
      </div>
    </div>
  );
}
```

- [ ] **Step 5: Commit**

```bash
git add src/store/authStore.ts src/hooks/useAuth.ts src/pages/Login.tsx src/pages/Register.tsx
git commit -m "feat(frontend): add auth store, hook, and login/register pages"
```

---

## Task 12: Update Routing and Claude API Migration

**Files:**
- Modify: `src/App.tsx`
- Modify: `src/services/claudeApi.ts`

- [ ] **Step 1: Update App.tsx to add auth routes**

Add these imports and routes to `src/App.tsx`:

```tsx
// Add imports
import Login from "./pages/Login";
import Register from "./pages/Register";
import { useAuthStore } from "./store/authStore";

// Update AuthGuard to check token-based auth
function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore();
  const profile = useUserStore((s) => s.profile);

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }
  if (profile && !profile.onboardingComplete) {
    return <Navigate to="/" replace />;
  }
  return <>{children}</>;
}

// Add routes before the catch-all
// <Route path="/login" element={<Login />} />
// <Route path="/register" element={<Register />} />
```

- [ ] **Step 2: Migrate claudeApi.ts to use backend proxy**

```typescript
// src/services/claudeApi.ts — replace browser-direct calls with backend proxy
import { api } from "./api";
import { getLanguage } from "../lib/i18n";

export async function sendMessage(systemPrompt: string, messages: { role: string; content: string }[]): Promise<string> {
  const resp = await api.post<{ content: string }>("/ai/chat", {
    system_prompt: systemPrompt,
    messages,
    language: getLanguage(),
  });
  return resp.content;
}

export async function assessLevel(direction: string, answers: string[]): Promise<"beginner" | "intermediate" | "advanced"> {
  const resp = await api.post<{ level: string }>("/ai/assess", {
    direction,
    answers,
    language: getLanguage(),
  });
  return resp.level as "beginner" | "intermediate" | "advanced";
}

export async function generateTip(direction: string, level: string): Promise<string> {
  const resp = await api.post<{ tip: string }>("/ai/tip", {
    direction,
    level,
    language: getLanguage(),
  });
  return resp.tip;
}

export async function scoreAnswer(
  question: string,
  answer: string,
  direction: string,
): Promise<{ score: number; feedback: string; modelAnswer: string }> {
  return api.post("/ai/score", {
    question,
    answer,
    direction,
    language: getLanguage(),
  });
}
```

- [ ] **Step 3: Commit**

```bash
git add src/App.tsx src/services/claudeApi.ts
git commit -m "feat(frontend): add auth routes and migrate Claude API to backend proxy"
```

---

## Task 13: Add Auth Translations

**Files:**
- Modify: `src/lib/i18n.ts`

- [ ] **Step 1: Add auth-related translation keys to i18n.ts**

Add these keys to the translations object in `src/lib/i18n.ts`:

```typescript
// Add to Russian translations
"login.subtitle": "Войдите в свой аккаунт",
"login.password": "Пароль",
"login.submit": "Войти",
"login.noAccount": "Нет аккаунта?",
"login.register": "Зарегистрироваться",
"register.subtitle": "Создайте новый аккаунт",
"register.name": "Имя",
"register.password": "Пароль",
"register.submit": "Зарегистрироваться",
"register.hasAccount": "Уже есть аккаунт?",
"register.login": "Войти",

// Add to English translations
"login.subtitle": "Sign in to your account",
"login.password": "Password",
"login.submit": "Sign in",
"login.noAccount": "Don't have an account?",
"login.register": "Register",
"register.subtitle": "Create a new account",
"register.name": "Name",
"register.password": "Password",
"register.submit": "Register",
"register.hasAccount": "Already have an account?",
"register.login": "Sign in",
```

- [ ] **Step 2: Commit**

```bash
git add src/lib/i18n.ts
git commit -m "feat(frontend): add auth translation keys"
```

---

## Task 14: Docker Compose for Development

**Files:**
- Create: `docker-compose.yml`
- Create: `backend/Dockerfile`

- [ ] **Step 1: Create docker-compose.yml**

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: pathmind
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      PATHMIND_DATABASE_URL: postgresql+asyncpg://postgres:postgres@db:5432/pathmind
      PATHMIND_REDIS_URL: redis://redis:6379/0
      PATHMIND_SECRET_KEY: dev-secret-key-change-in-production
      PATHMIND_ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

volumes:
  pgdata:
```

- [ ] **Step 2: Create backend Dockerfile**

```dockerfile
# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 3: Commit**

```bash
git add docker-compose.yml backend/Dockerfile
git commit -m "feat: add Docker Compose for local development"
```

---

## Task 15: Integration Test — Full Flow

**Files:**
- Create: `backend/tests/test_integration.py`

- [ ] **Step 1: Write full-flow integration test**

```python
# backend/tests/test_integration.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_full_user_flow(client: AsyncClient):
    # 1. Register
    reg = await client.post("/api/auth/register", json={
        "email": "flow@example.com",
        "password": "pass123",
        "name": "Flow User",
    })
    assert reg.status_code == 201
    token = reg.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Get profile
    profile = await client.get("/api/users/me", headers=headers)
    assert profile.status_code == 200
    assert profile.json()["xp"] == 0
    assert profile.json()["onboarding_complete"] is False

    # 3. Complete onboarding
    onboard = await client.patch("/api/users/me", headers=headers, json={
        "direction": "frontend",
        "assessment_level": "beginner",
        "onboarding_complete": True,
    })
    assert onboard.status_code == 200
    assert onboard.json()["onboarding_complete"] is True

    # 4. Add XP and level up
    xp = await client.post("/api/progress/xp", headers=headers, json={
        "amount": 500,
        "reason": "lesson",
    })
    assert xp.status_code == 200
    assert xp.json()["leveled_up"] is True
    assert xp.json()["new_level"] == "Apprentice"

    # 5. Complete a node
    node = await client.post("/api/progress/nodes", headers=headers, json={
        "node_id": "fe-1",
    })
    assert node.status_code == 200
    assert "fe-1" in node.json()["completed_nodes"]

    # 6. Complete a lesson
    lesson = await client.post("/api/progress/lessons", headers=headers, json={
        "lesson_id": "fe-1-1",
    })
    assert lesson.status_code == 200
    assert "fe-1-1" in lesson.json()["completed_lessons"]

    # 7. Earn a badge
    badge = await client.post("/api/progress/badges", headers=headers, json={
        "badge_id": "first-step",
    })
    assert badge.status_code == 200
    assert "first-step" in badge.json()["earned_badges"]

    # 8. Update streak
    streak = await client.post("/api/progress/streak", headers=headers)
    assert streak.status_code == 200
    assert streak.json()["streak"] == 1

    # 9. Verify final profile state
    final = await client.get("/api/users/me", headers=headers)
    data = final.json()
    assert data["xp"] == 500
    assert data["level"] == "Apprentice"
    assert data["streak"] == 1
    assert "fe-1" in data["completed_nodes"]
    assert "fe-1-1" in data["completed_lessons"]
    assert "first-step" in data["earned_badges"]
    assert data["onboarding_complete"] is True
```

- [ ] **Step 2: Run integration test**

Run: `cd backend && pytest tests/test_integration.py -v`
Expected: PASS

- [ ] **Step 3: Run full test suite one final time**

Run: `cd backend && pytest tests/ -v --tb=short`
Expected: All 23 tests PASS

- [ ] **Step 4: Commit**

```bash
git add backend/tests/test_integration.py
git commit -m "test(backend): add full-flow integration test"
```

---

## Summary

| Task | Description | Tests |
|------|-------------|-------|
| 1 | Backend scaffold (FastAPI, config) | — |
| 2 | Database models (User, Progress) + Alembic | — |
| 3 | Auth schemas + service + middleware | — |
| 4 | Auth router (register, login, refresh) | 5 tests |
| 5 | User profile router (get, update) | 4 tests |
| 6 | Progress router (XP, streak, nodes, lessons, badges) | 8 tests |
| 7 | Claude API proxy router | 5 tests |
| 8 | Redis setup | — |
| 9 | Run all backend tests | 22 tests |
| 10 | Frontend API client layer | — |
| 11 | Auth store + login/register pages | — |
| 12 | Update routing + Claude API migration | — |
| 13 | Auth translations | — |
| 14 | Docker Compose | — |
| 15 | Integration test | 1 test |

**Total: 15 tasks, 23 backend tests, complete backend + frontend integration.**
