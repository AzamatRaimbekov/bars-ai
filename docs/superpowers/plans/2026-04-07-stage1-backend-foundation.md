# Stage 1: Backend Foundation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a FastAPI backend with auth, progress tracking, and Claude API proxy — migrate frontend from localStorage to API.

**Architecture:** FastAPI with Router → Service → Model layering. PostgreSQL for persistence, Redis for caching/rate-limiting. Docker Compose orchestrates all services. Frontend stores access token in Zustand memory, refresh token in httpOnly cookie.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (async), Alembic, PostgreSQL 16, Redis 7, Docker Compose, pytest, httpx

---

## File Map

### New files (backend/)

| File | Responsibility |
|------|---------------|
| `backend/docker-compose.yml` | Orchestrate API + Postgres + Redis + Nginx |
| `backend/Dockerfile` | Build API container |
| `backend/requirements.txt` | Python dependencies |
| `backend/.env.example` | Environment variable template |
| `backend/alembic.ini` | Alembic config |
| `backend/alembic/env.py` | Alembic async env |
| `backend/app/__init__.py` | Package marker |
| `backend/app/main.py` | FastAPI app, lifespan, CORS, router includes |
| `backend/app/config.py` | Pydantic BaseSettings |
| `backend/app/database.py` | Async engine + session factory |
| `backend/app/redis.py` | Redis connection pool |
| `backend/app/dependencies.py` | get_db, get_current_user, get_redis |
| `backend/app/models/__init__.py` | Import all models for Alembic |
| `backend/app/models/user.py` | User SQLAlchemy model |
| `backend/app/models/progress.py` | Progress SQLAlchemy model |
| `backend/app/models/badge.py` | UserBadge SQLAlchemy model |
| `backend/app/models/refresh_token.py` | RefreshToken SQLAlchemy model |
| `backend/app/schemas/auth.py` | Register/Login/Token schemas |
| `backend/app/schemas/user.py` | UserResponse/UserUpdate schemas |
| `backend/app/schemas/progress.py` | XP/Node/Lesson/Badge/Stats schemas |
| `backend/app/schemas/ai.py` | Chat/Assess/Tip/Score schemas |
| `backend/app/routers/auth.py` | Auth endpoints |
| `backend/app/routers/users.py` | User endpoints |
| `backend/app/routers/progress.py` | Progress endpoints |
| `backend/app/routers/ai.py` | AI proxy endpoints |
| `backend/app/services/auth_service.py` | Auth business logic |
| `backend/app/services/user_service.py` | User business logic |
| `backend/app/services/progress_service.py` | Progress business logic |
| `backend/app/services/ai_service.py` | Claude API proxy logic |
| `backend/app/utils/security.py` | Password hashing, JWT |
| `backend/app/utils/rate_limiter.py` | Redis rate limiting |
| `backend/tests/__init__.py` | Package marker |
| `backend/tests/conftest.py` | Test fixtures |
| `backend/tests/test_auth.py` | Auth tests |
| `backend/tests/test_users.py` | User tests |
| `backend/tests/test_progress.py` | Progress tests |
| `backend/tests/test_ai.py` | AI proxy tests |
| `backend/nginx/nginx.conf` | Nginx reverse proxy config |

### New files (frontend src/)

| File | Responsibility |
|------|---------------|
| `src/services/api.ts` | Base HTTP client with JWT interceptor |
| `src/services/authApi.ts` | Auth API calls |
| `src/store/authStore.ts` | Auth state (token, user, isAuthenticated) |
| `src/pages/Login.tsx` | Login page |
| `src/pages/Register.tsx` | Registration page |

### Modified files (frontend src/)

| File | Change |
|------|--------|
| `src/services/claudeApi.ts` | Route through /api/ai/* instead of direct Anthropic |
| `src/store/userStore.ts` | Remove localStorage persist, sync with API |
| `src/App.tsx` | Add Login/Register routes, update AuthGuard |
| `src/pages/Onboarding.tsx` | Call register API after assessment |

---

## Task 1: Docker Compose & Infrastructure

**Files:**
- Create: `backend/docker-compose.yml`
- Create: `backend/Dockerfile`
- Create: `backend/requirements.txt`
- Create: `backend/.env.example`
- Create: `backend/nginx/nginx.conf`

- [ ] **Step 1: Create requirements.txt**

```
backend/requirements.txt
```

```txt
fastapi==0.115.12
uvicorn[standard]==0.34.2
sqlalchemy[asyncio]==2.0.40
asyncpg==0.30.0
alembic==1.15.2
pydantic==2.11.3
pydantic-settings==2.9.1
python-jose[cryptography]==3.4.0
passlib[bcrypt]==1.7.4
httpx==0.28.1
redis==5.3.0
python-multipart==0.0.20
pytest==8.3.5
pytest-asyncio==0.26.0
httpx==0.28.1
```

- [ ] **Step 2: Create .env.example**

```
backend/.env.example
```

```env
DB_PASSWORD=changeme
DATABASE_URL=postgresql+asyncpg://pathmind:changeme@postgres:5432/pathmind
REDIS_URL=redis://redis:6379/0
ANTHROPIC_API_KEY=sk-ant-your-key-here
JWT_SECRET=change-this-to-a-random-64-char-string
JWT_ACCESS_EXPIRE_MINUTES=30
JWT_REFRESH_EXPIRE_DAYS=7
CORS_ORIGINS=http://localhost:5173,http://localhost:80
```

- [ ] **Step 3: Create Dockerfile**

```
backend/Dockerfile
```

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
```

- [ ] **Step 4: Create docker-compose.yml**

```
backend/docker-compose.yml
```

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./app:/app/app
      - ./alembic:/app/alembic
    restart: unless-stopped

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: pathmind
      POSTGRES_USER: pathmind
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U pathmind"]
      interval: 5s
      timeout: 3s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
    restart: unless-stopped

volumes:
  pgdata:
  redisdata:
```

- [ ] **Step 5: Create nginx.conf**

```
backend/nginx/nginx.conf
```

```nginx
events {
    worker_connections 1024;
}

http {
    upstream api {
        server api:8000;
    }

    upstream frontend {
        server host.docker.internal:5173;
    }

    server {
        listen 80;

        location /api/ {
            proxy_pass http://api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
    }
}
```

- [ ] **Step 6: Commit**

```bash
cd backend
git add docker-compose.yml Dockerfile requirements.txt .env.example nginx/nginx.conf
git commit -m "feat(backend): add Docker infrastructure"
```

---

## Task 2: FastAPI App Core & Config

**Files:**
- Create: `backend/app/__init__.py`
- Create: `backend/app/config.py`
- Create: `backend/app/database.py`
- Create: `backend/app/redis.py`
- Create: `backend/app/main.py`

- [ ] **Step 1: Create app/__init__.py**

```python
# backend/app/__init__.py
```

(empty file)

- [ ] **Step 2: Create config.py**

```python
# backend/app/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://redis:6379/0"
    ANTHROPIC_API_KEY: str
    JWT_SECRET: str
    JWT_ACCESS_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_EXPIRE_DAYS: int = 7
    CORS_ORIGINS: str = "http://localhost:5173"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]

    model_config = {"env_file": ".env"}


settings = Settings()
```

- [ ] **Step 3: Create database.py**

```python
# backend/app/database.py
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
```

- [ ] **Step 4: Create redis.py**

```python
# backend/app/redis.py
import redis.asyncio as aioredis

from app.config import settings

redis_pool = aioredis.ConnectionPool.from_url(settings.REDIS_URL, decode_responses=True)


def get_redis_client() -> aioredis.Redis:
    return aioredis.Redis(connection_pool=redis_pool)
```

- [ ] **Step 5: Create main.py**

```python
# backend/app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.redis import redis_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_pool.aclose()


app = FastAPI(title="PathMind API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health():
    return {"status": "ok"}
```

- [ ] **Step 6: Verify the app starts**

```bash
cd backend
cp .env.example .env
# Edit .env with real values
docker compose up --build -d
# Wait for services to start
curl http://localhost:8000/api/health
```

Expected: `{"status":"ok"}`

- [ ] **Step 7: Commit**

```bash
git add app/__init__.py app/config.py app/database.py app/redis.py app/main.py
git commit -m "feat(backend): add FastAPI core, config, database, redis"
```

---

## Task 3: SQLAlchemy Models & Alembic

**Files:**
- Create: `backend/app/models/__init__.py`
- Create: `backend/app/models/user.py`
- Create: `backend/app/models/progress.py`
- Create: `backend/app/models/badge.py`
- Create: `backend/app/models/refresh_token.py`
- Create: `backend/alembic.ini`
- Create: `backend/alembic/env.py`

- [ ] **Step 1: Create models/user.py**

```python
# backend/app/models/user.py
import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    direction: Mapped[str] = mapped_column(String(20), nullable=False)
    assessment_level: Mapped[str] = mapped_column(String(20), default="beginner")
    language: Mapped[str] = mapped_column(String(5), default="ru")
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    progress: Mapped["Progress"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")
    badges: Mapped[list["UserBadge"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(back_populates="user", cascade="all, delete-orphan")
```

- [ ] **Step 2: Create models/progress.py**

```python
# backend/app/models/progress.py
import uuid
from datetime import date, datetime

from sqlalchemy import Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Progress(Base):
    __tablename__ = "progress"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    xp: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[str] = mapped_column(String(20), default="Novice")
    streak: Mapped[int] = mapped_column(Integer, default=0)
    longest_streak: Mapped[int] = mapped_column(Integer, default=0)
    last_active_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    completed_nodes: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    completed_lessons: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship(back_populates="progress")
```

- [ ] **Step 3: Create models/badge.py**

```python
# backend/app/models/badge.py
import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UserBadge(Base):
    __tablename__ = "user_badges"
    __table_args__ = (UniqueConstraint("user_id", "badge_id"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    badge_id: Mapped[str] = mapped_column(String(50), nullable=False)
    earned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="badges")
```

- [ ] **Step 4: Create models/refresh_token.py**

```python
# backend/app/models/refresh_token.py
import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    token_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="refresh_tokens")
```

- [ ] **Step 5: Create models/__init__.py**

```python
# backend/app/models/__init__.py
from app.models.user import User
from app.models.progress import Progress
from app.models.badge import UserBadge
from app.models.refresh_token import RefreshToken

__all__ = ["User", "Progress", "UserBadge", "RefreshToken"]
```

- [ ] **Step 6: Initialize Alembic**

```bash
cd backend
docker compose exec api alembic init alembic
```

- [ ] **Step 7: Configure alembic.ini**

In `backend/alembic.ini`, set:
```ini
sqlalchemy.url =
```
(Leave empty — we set it from env.py)

- [ ] **Step 8: Create alembic/env.py**

```python
# backend/alembic/env.py
import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import settings
from app.database import Base
from app.models import User, Progress, UserBadge, RefreshToken  # noqa: F401

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(url=settings.DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    connectable = create_async_engine(settings.DATABASE_URL)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
```

- [ ] **Step 9: Generate initial migration**

```bash
docker compose exec api alembic revision --autogenerate -m "initial tables"
```

- [ ] **Step 10: Apply migration**

```bash
docker compose exec api alembic upgrade head
```

- [ ] **Step 11: Commit**

```bash
git add app/models/ alembic.ini alembic/
git commit -m "feat(backend): add SQLAlchemy models and Alembic migrations"
```

---

## Task 4: Security Utils & Dependencies

**Files:**
- Create: `backend/app/utils/__init__.py`
- Create: `backend/app/utils/security.py`
- Create: `backend/app/utils/rate_limiter.py`
- Create: `backend/app/dependencies.py`
- Create: `backend/app/schemas/__init__.py`

- [ ] **Step 1: Create utils/__init__.py**

```python
# backend/app/utils/__init__.py
```

- [ ] **Step 2: Create utils/security.py**

```python
# backend/app/utils/security.py
import hashlib
import uuid
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_EXPIRE_MINUTES)
    return jwt.encode({"sub": user_id, "exp": expire, "type": "access"}, settings.JWT_SECRET, algorithm=ALGORITHM)


def create_refresh_token() -> tuple[str, str]:
    """Returns (raw_token, token_hash) — store hash in DB, send raw to client."""
    raw = uuid.uuid4().hex + uuid.uuid4().hex
    token_hash = hashlib.sha256(raw.encode()).hexdigest()
    return raw, token_hash


def hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def decode_access_token(token: str) -> str | None:
    """Returns user_id or None if invalid."""
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            return None
        return payload.get("sub")
    except JWTError:
        return None
```

- [ ] **Step 3: Create utils/rate_limiter.py**

```python
# backend/app/utils/rate_limiter.py
from fastapi import HTTPException, Request, Depends
import redis.asyncio as aioredis

from app.redis import get_redis_client


async def rate_limit(request: Request, max_requests: int = 20, window_seconds: int = 60):
    """Rate limit by user. Call after authentication so request.state.user_id exists."""
    user_id = getattr(request.state, "user_id", "anon")
    r = get_redis_client()
    key = f"rate:{user_id}:{request.url.path}"
    try:
        count = await r.incr(key)
        if count == 1:
            await r.expire(key, window_seconds)
        if count > max_requests:
            raise HTTPException(status_code=429, detail="Too many requests")
    finally:
        await r.aclose()
```

- [ ] **Step 4: Create schemas/__init__.py**

```python
# backend/app/schemas/__init__.py
```

- [ ] **Step 5: Create dependencies.py**

```python
# backend/app/dependencies.py
import uuid
from typing import AsyncGenerator

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session
from app.utils.security import decode_access_token

security_scheme = HTTPBearer()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
) -> uuid.UUID:
    user_id = decode_access_token(credentials.credentials)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return uuid.UUID(user_id)
```

- [ ] **Step 6: Commit**

```bash
git add app/utils/ app/dependencies.py app/schemas/__init__.py
git commit -m "feat(backend): add security utils, rate limiter, dependencies"
```

---

## Task 5: Auth Schemas, Service & Router

**Files:**
- Create: `backend/app/schemas/auth.py`
- Create: `backend/app/services/__init__.py`
- Create: `backend/app/services/auth_service.py`
- Create: `backend/app/routers/__init__.py`
- Create: `backend/app/routers/auth.py`
- Modify: `backend/app/main.py`
- Create: `backend/tests/__init__.py`
- Create: `backend/tests/conftest.py`
- Create: `backend/tests/test_auth.py`

- [ ] **Step 1: Create schemas/auth.py**

```python
# backend/app/schemas/auth.py
from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    name: str = Field(min_length=1, max_length=100)
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    assessment_level: str = Field(default="beginner", pattern=r"^(beginner|intermediate|advanced)$")
    language: str = Field(default="ru", pattern=r"^(ru|en)$")


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

- [ ] **Step 2: Create services/__init__.py**

```python
# backend/app/services/__init__.py
```

- [ ] **Step 3: Create services/auth_service.py**

```python
# backend/app/services/auth_service.py
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.user import User
from app.models.progress import Progress
from app.models.refresh_token import RefreshToken
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_token,
)


async def register(db: AsyncSession, email: str, password: str, name: str, direction: str, assessment_level: str, language: str) -> tuple[User, str, str]:
    """Register user. Returns (user, access_token, raw_refresh_token)."""
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(
        email=email,
        password=hash_password(password),
        name=name,
        direction=direction,
        assessment_level=assessment_level,
        language=language,
    )
    db.add(user)
    await db.flush()

    progress = Progress(user_id=user.id)
    db.add(progress)

    access_token = create_access_token(str(user.id))
    raw_refresh, token_hash = create_refresh_token()
    rt = RefreshToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(rt)
    await db.commit()
    await db.refresh(user)

    return user, access_token, raw_refresh


async def login(db: AsyncSession, email: str, password: str) -> tuple[User, str, str]:
    """Login user. Returns (user, access_token, raw_refresh_token)."""
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(str(user.id))
    raw_refresh, token_hash = create_refresh_token()
    rt = RefreshToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(rt)
    await db.commit()

    return user, access_token, raw_refresh


async def refresh(db: AsyncSession, raw_token: str) -> tuple[str, str]:
    """Refresh tokens. Returns (new_access_token, new_raw_refresh_token)."""
    token_hash = hash_token(raw_token)
    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == token_hash,
            RefreshToken.revoked == False,
            RefreshToken.expires_at > datetime.now(timezone.utc),
        )
    )
    rt = result.scalar_one_or_none()
    if not rt:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    # Revoke old token
    rt.revoked = True

    # Issue new pair
    access_token = create_access_token(str(rt.user_id))
    new_raw, new_hash = create_refresh_token()
    new_rt = RefreshToken(
        user_id=rt.user_id,
        token_hash=new_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.JWT_REFRESH_EXPIRE_DAYS),
    )
    db.add(new_rt)
    await db.commit()

    return access_token, new_raw


async def logout(db: AsyncSession, raw_token: str) -> None:
    """Revoke refresh token."""
    token_hash = hash_token(raw_token)
    result = await db.execute(select(RefreshToken).where(RefreshToken.token_hash == token_hash))
    rt = result.scalar_one_or_none()
    if rt:
        rt.revoked = True
        await db.commit()
```

- [ ] **Step 4: Create routers/__init__.py**

```python
# backend/app/routers/__init__.py
```

- [ ] **Step 5: Create routers/auth.py**

```python
# backend/app/routers/auth.py
from fastapi import APIRouter, Depends, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])

COOKIE_KEY = "refresh_token"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60  # 7 days


def _set_refresh_cookie(response: Response, raw_token: str):
    response.set_cookie(
        key=COOKIE_KEY,
        value=raw_token,
        httponly=True,
        secure=False,  # Set True in production with HTTPS
        samesite="lax",
        max_age=COOKIE_MAX_AGE,
        path="/api/auth",
    )


@router.post("/register", response_model=TokenResponse)
async def register(body: RegisterRequest, response: Response, db: AsyncSession = Depends(get_db)):
    user, access_token, raw_refresh = await auth_service.register(
        db, body.email, body.password, body.name, body.direction, body.assessment_level, body.language,
    )
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, response: Response, db: AsyncSession = Depends(get_db)):
    user, access_token, raw_refresh = await auth_service.login(db, body.email, body.password)
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(response: Response, refresh_token: str | None = Cookie(None, alias=COOKIE_KEY), db: AsyncSession = Depends(get_db)):
    if not refresh_token:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="No refresh token")
    access_token, new_raw = await auth_service.refresh(db, refresh_token)
    _set_refresh_cookie(response, new_raw)
    return TokenResponse(access_token=access_token)


@router.post("/logout", status_code=204)
async def logout(response: Response, refresh_token: str | None = Cookie(None, alias=COOKIE_KEY), db: AsyncSession = Depends(get_db)):
    if refresh_token:
        await auth_service.logout(db, refresh_token)
    response.delete_cookie(COOKIE_KEY, path="/api/auth")
```

- [ ] **Step 6: Register auth router in main.py**

Add to `backend/app/main.py` after the health endpoint:

```python
from app.routers import auth

app.include_router(auth.router)
```

- [ ] **Step 7: Create tests/conftest.py**

```python
# backend/tests/conftest.py
import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base
from app.dependencies import get_db
from app.main import app

TEST_DB_URL = "postgresql+asyncpg://pathmind:changeme@localhost:5432/pathmind_test"

engine_test = create_async_engine(TEST_DB_URL, echo=False)
async_session_test = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def override_get_db():
    async with async_session_test() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


@pytest_asyncio.fixture
async def authenticated_client(client: AsyncClient):
    """Returns (client, user_data) with auth headers set."""
    resp = await client.post("/api/auth/register", json={
        "email": "test@example.com",
        "password": "testpass123",
        "name": "Test User",
        "direction": "frontend",
    })
    assert resp.status_code == 200
    token = resp.json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client
```

- [ ] **Step 8: Create tests/__init__.py**

```python
# backend/tests/__init__.py
```

- [ ] **Step 9: Create tests/test_auth.py**

```python
# backend/tests/test_auth.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "new@example.com",
        "password": "password123",
        "name": "New User",
        "direction": "frontend",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "refresh_token" in resp.cookies


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    payload = {
        "email": "dup@example.com",
        "password": "password123",
        "name": "User",
        "direction": "english",
    }
    await client.post("/api/auth/register", json=payload)
    resp = await client.post("/api/auth/register", json=payload)
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_register_invalid_direction(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "bad@example.com",
        "password": "password123",
        "name": "User",
        "direction": "invalid",
    })
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_register_short_password(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "short@example.com",
        "password": "123",
        "name": "User",
        "direction": "frontend",
    })
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient):
    await client.post("/api/auth/register", json={
        "email": "login@example.com",
        "password": "password123",
        "name": "User",
        "direction": "frontend",
    })
    resp = await client.post("/api/auth/login", json={
        "email": "login@example.com",
        "password": "password123",
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient):
    await client.post("/api/auth/register", json={
        "email": "wrong@example.com",
        "password": "password123",
        "name": "User",
        "direction": "frontend",
    })
    resp = await client.post("/api/auth/login", json={
        "email": "wrong@example.com",
        "password": "wrongpassword",
    })
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "refresh@example.com",
        "password": "password123",
        "name": "User",
        "direction": "frontend",
    })
    cookies = resp.cookies
    resp2 = await client.post("/api/auth/refresh", cookies=cookies)
    assert resp2.status_code == 200
    assert "access_token" in resp2.json()


@pytest.mark.asyncio
async def test_logout(client: AsyncClient):
    resp = await client.post("/api/auth/register", json={
        "email": "logout@example.com",
        "password": "password123",
        "name": "User",
        "direction": "frontend",
    })
    cookies = resp.cookies
    resp2 = await client.post("/api/auth/logout", cookies=cookies)
    assert resp2.status_code == 204
    # Refresh should fail after logout
    resp3 = await client.post("/api/auth/refresh", cookies=cookies)
    assert resp3.status_code == 401
```

- [ ] **Step 10: Run tests**

```bash
docker compose exec api pytest tests/test_auth.py -v
```

Expected: All 8 tests pass.

- [ ] **Step 11: Commit**

```bash
git add app/schemas/auth.py app/services/ app/routers/ tests/
git commit -m "feat(backend): add auth module (register, login, refresh, logout)"
```

---

## Task 6: User Schemas, Service & Router

**Files:**
- Create: `backend/app/schemas/user.py`
- Create: `backend/app/services/user_service.py`
- Create: `backend/app/routers/users.py`
- Modify: `backend/app/main.py`
- Create: `backend/tests/test_users.py`

- [ ] **Step 1: Create schemas/user.py**

```python
# backend/app/schemas/user.py
import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    direction: str
    assessment_level: str
    language: str
    avatar_url: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class UserWithProgressResponse(UserResponse):
    xp: int = 0
    level: str = "Novice"
    streak: int = 0
    longest_streak: int = 0
    completed_nodes: list[str] = []
    completed_lessons: list[str] = []
    earned_badges: list[str] = []


class UserUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    language: str | None = Field(None, pattern=r"^(ru|en)$")
    avatar_url: str | None = None


class PublicUserResponse(BaseModel):
    id: uuid.UUID
    name: str
    direction: str
    level: str
    earned_badges: list[str]

    model_config = {"from_attributes": True}
```

- [ ] **Step 2: Create services/user_service.py**

```python
# backend/app/services/user_service.py
import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.user import User
from app.models.progress import Progress
from app.models.badge import UserBadge


async def get_me(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress = user.progress
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "direction": user.direction,
        "assessment_level": user.assessment_level,
        "language": user.language,
        "avatar_url": user.avatar_url,
        "created_at": user.created_at,
        "xp": progress.xp if progress else 0,
        "level": progress.level if progress else "Novice",
        "streak": progress.streak if progress else 0,
        "longest_streak": progress.longest_streak if progress else 0,
        "completed_nodes": progress.completed_nodes if progress else [],
        "completed_lessons": progress.completed_lessons if progress else [],
        "earned_badges": [b.badge_id for b in user.badges],
    }


async def update_me(db: AsyncSession, user_id: uuid.UUID, name: str | None, language: str | None, avatar_url: str | None) -> dict:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        user.name = name
    if language is not None:
        user.language = language
    if avatar_url is not None:
        user.avatar_url = avatar_url

    await db.commit()
    return await get_me(db, user_id)


async def get_public_profile(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "name": user.name,
        "direction": user.direction,
        "level": user.progress.level if user.progress else "Novice",
        "earned_badges": [b.badge_id for b in user.badges],
    }
```

- [ ] **Step 3: Create routers/users.py**

```python
# backend/app/routers/users.py
import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.user import UserWithProgressResponse, UserUpdateRequest, PublicUserResponse
from app.services import user_service

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/me", response_model=UserWithProgressResponse)
async def get_me(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await user_service.get_me(db, user_id)


@router.patch("/me", response_model=UserWithProgressResponse)
async def update_me(body: UserUpdateRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await user_service.update_me(db, user_id, body.name, body.language, body.avatar_url)


@router.get("/{target_id}", response_model=PublicUserResponse)
async def get_user(target_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await user_service.get_public_profile(db, target_id)
```

- [ ] **Step 4: Register users router in main.py**

Add to `backend/app/main.py`:

```python
from app.routers import auth, users

app.include_router(auth.router)
app.include_router(users.router)
```

- [ ] **Step 5: Create tests/test_users.py**

```python
# backend/tests/test_users.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_me(authenticated_client: AsyncClient):
    resp = await authenticated_client.get("/api/users/me")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Test User"
    assert data["direction"] == "frontend"
    assert data["xp"] == 0
    assert data["level"] == "Novice"


@pytest.mark.asyncio
async def test_update_me(authenticated_client: AsyncClient):
    resp = await authenticated_client.patch("/api/users/me", json={"name": "Updated Name", "language": "en"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "Updated Name"
    assert resp.json()["language"] == "en"


@pytest.mark.asyncio
async def test_get_me_unauthorized(client: AsyncClient):
    resp = await client.get("/api/users/me")
    assert resp.status_code == 403  # No auth header


@pytest.mark.asyncio
async def test_get_public_profile(authenticated_client: AsyncClient):
    me = await authenticated_client.get("/api/users/me")
    user_id = me.json()["id"]
    resp = await authenticated_client.get(f"/api/users/{user_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert "name" in data
    assert "email" not in data  # Public profile shouldn't expose email
```

- [ ] **Step 6: Run tests**

```bash
docker compose exec api pytest tests/test_users.py -v
```

Expected: All 4 tests pass.

- [ ] **Step 7: Commit**

```bash
git add app/schemas/user.py app/services/user_service.py app/routers/users.py tests/test_users.py app/main.py
git commit -m "feat(backend): add users module (me, update, public profile)"
```

---

## Task 7: Progress Schemas, Service & Router

**Files:**
- Create: `backend/app/schemas/progress.py`
- Create: `backend/app/services/progress_service.py`
- Create: `backend/app/routers/progress.py`
- Modify: `backend/app/main.py`
- Create: `backend/tests/test_progress.py`

- [ ] **Step 1: Create schemas/progress.py**

```python
# backend/app/schemas/progress.py
from datetime import datetime

from pydantic import BaseModel, Field


class AddXPRequest(BaseModel):
    amount: int = Field(gt=0, le=1000)
    source: str = Field(min_length=1, max_length=50)


class AddXPResponse(BaseModel):
    xp: int
    level: str
    leveled_up: bool


class CompleteNodeRequest(BaseModel):
    node_id: str = Field(min_length=1, max_length=100)


class CompleteLessonRequest(BaseModel):
    lesson_id: str = Field(min_length=1, max_length=100)


class EarnBadgeRequest(BaseModel):
    badge_id: str = Field(min_length=1, max_length=50)


class EarnBadgeResponse(BaseModel):
    badge_id: str
    earned_at: datetime


class StreakResponse(BaseModel):
    streak: int
    longest_streak: int


class StatsResponse(BaseModel):
    xp: int
    level: str
    streak: int
    longest_streak: int
    completed_nodes: list[str]
    completed_lessons: list[str]
    earned_badges: list[str]
```

- [ ] **Step 2: Create services/progress_service.py**

```python
# backend/app/services/progress_service.py
import uuid
from datetime import date

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.progress import Progress
from app.models.badge import UserBadge
from app.models.user import User

LEVEL_THRESHOLDS = [
    ("Novice", 0),
    ("Apprentice", 500),
    ("Practitioner", 1500),
    ("Expert", 4000),
    ("Master", 8000),
    ("Legend", 15000),
]


def _calculate_level(xp: int) -> str:
    current = "Novice"
    for name, threshold in LEVEL_THRESHOLDS:
        if xp >= threshold:
            current = name
        else:
            break
    return current


async def _get_progress(db: AsyncSession, user_id: uuid.UUID) -> Progress:
    result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    progress = result.scalar_one_or_none()
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress


async def add_xp(db: AsyncSession, user_id: uuid.UUID, amount: int, source: str) -> dict:
    progress = await _get_progress(db, user_id)
    old_level = progress.level
    progress.xp += amount
    progress.level = _calculate_level(progress.xp)
    await db.commit()
    return {"xp": progress.xp, "level": progress.level, "leveled_up": progress.level != old_level}


async def complete_node(db: AsyncSession, user_id: uuid.UUID, node_id: str) -> dict:
    progress = await _get_progress(db, user_id)
    if node_id not in progress.completed_nodes:
        progress.completed_nodes = [*progress.completed_nodes, node_id]
        await db.commit()
    return {"completed_nodes": progress.completed_nodes}


async def complete_lesson(db: AsyncSession, user_id: uuid.UUID, lesson_id: str) -> dict:
    progress = await _get_progress(db, user_id)
    if lesson_id not in progress.completed_lessons:
        progress.completed_lessons = [*progress.completed_lessons, lesson_id]
        await db.commit()
    return {"completed_lessons": progress.completed_lessons}


async def earn_badge(db: AsyncSession, user_id: uuid.UUID, badge_id: str) -> dict:
    existing = await db.execute(
        select(UserBadge).where(UserBadge.user_id == user_id, UserBadge.badge_id == badge_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Badge already earned")

    badge = UserBadge(user_id=user_id, badge_id=badge_id)
    db.add(badge)
    await db.commit()
    await db.refresh(badge)
    return {"badge_id": badge.badge_id, "earned_at": badge.earned_at}


async def update_streak(db: AsyncSession, user_id: uuid.UUID) -> dict:
    progress = await _get_progress(db, user_id)
    today = date.today()

    if progress.last_active_date == today:
        return {"streak": progress.streak, "longest_streak": progress.longest_streak}

    yesterday = date.fromordinal(today.toordinal() - 1)
    if progress.last_active_date == yesterday:
        progress.streak += 1
    else:
        progress.streak = 1

    if progress.streak > progress.longest_streak:
        progress.longest_streak = progress.streak

    progress.last_active_date = today
    await db.commit()
    return {"streak": progress.streak, "longest_streak": progress.longest_streak}


async def get_stats(db: AsyncSession, user_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(User).options(selectinload(User.progress), selectinload(User.badges)).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress = user.progress
    return {
        "xp": progress.xp if progress else 0,
        "level": progress.level if progress else "Novice",
        "streak": progress.streak if progress else 0,
        "longest_streak": progress.longest_streak if progress else 0,
        "completed_nodes": progress.completed_nodes if progress else [],
        "completed_lessons": progress.completed_lessons if progress else [],
        "earned_badges": [b.badge_id for b in user.badges],
    }
```

- [ ] **Step 3: Create routers/progress.py**

```python
# backend/app/routers/progress.py
import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.progress import (
    AddXPRequest, AddXPResponse,
    CompleteNodeRequest, CompleteLessonRequest,
    EarnBadgeRequest, EarnBadgeResponse,
    StreakResponse, StatsResponse,
)
from app.services import progress_service

router = APIRouter(prefix="/api/progress", tags=["progress"])


@router.post("/xp", response_model=AddXPResponse)
async def add_xp(body: AddXPRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.add_xp(db, user_id, body.amount, body.source)


@router.post("/node")
async def complete_node(body: CompleteNodeRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.complete_node(db, user_id, body.node_id)


@router.post("/lesson")
async def complete_lesson(body: CompleteLessonRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.complete_lesson(db, user_id, body.lesson_id)


@router.post("/badge", response_model=EarnBadgeResponse)
async def earn_badge(body: EarnBadgeRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.earn_badge(db, user_id, body.badge_id)


@router.post("/streak", response_model=StreakResponse)
async def update_streak(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.update_streak(db, user_id)


@router.get("/stats", response_model=StatsResponse)
async def get_stats(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await progress_service.get_stats(db, user_id)
```

- [ ] **Step 4: Register progress router in main.py**

Add to `backend/app/main.py`:

```python
from app.routers import auth, users, progress

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(progress.router)
```

- [ ] **Step 5: Create tests/test_progress.py**

```python
# backend/tests/test_progress.py
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_xp(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/progress/xp", json={"amount": 100, "source": "lesson"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["xp"] == 100
    assert data["level"] == "Novice"
    assert data["leveled_up"] is False


@pytest.mark.asyncio
async def test_add_xp_level_up(authenticated_client: AsyncClient):
    await authenticated_client.post("/api/progress/xp", json={"amount": 500, "source": "lesson"})
    resp = await authenticated_client.post("/api/progress/xp", json={"amount": 1, "source": "bonus"})
    data = resp.json()
    assert data["level"] == "Apprentice"
    assert data["leveled_up"] is True


@pytest.mark.asyncio
async def test_complete_node(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/progress/node", json={"node_id": "html-basics"})
    assert resp.status_code == 200
    assert "html-basics" in resp.json()["completed_nodes"]


@pytest.mark.asyncio
async def test_complete_node_idempotent(authenticated_client: AsyncClient):
    await authenticated_client.post("/api/progress/node", json={"node_id": "css-101"})
    resp = await authenticated_client.post("/api/progress/node", json={"node_id": "css-101"})
    assert resp.json()["completed_nodes"].count("css-101") == 1


@pytest.mark.asyncio
async def test_complete_lesson(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/progress/lesson", json={"lesson_id": "lesson-1"})
    assert resp.status_code == 200
    assert "lesson-1" in resp.json()["completed_lessons"]


@pytest.mark.asyncio
async def test_earn_badge(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/progress/badge", json={"badge_id": "first-step"})
    assert resp.status_code == 200
    assert resp.json()["badge_id"] == "first-step"


@pytest.mark.asyncio
async def test_earn_badge_duplicate(authenticated_client: AsyncClient):
    await authenticated_client.post("/api/progress/badge", json={"badge_id": "speed-learner"})
    resp = await authenticated_client.post("/api/progress/badge", json={"badge_id": "speed-learner"})
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_update_streak(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/progress/streak")
    assert resp.status_code == 200
    assert resp.json()["streak"] == 1


@pytest.mark.asyncio
async def test_update_streak_idempotent_same_day(authenticated_client: AsyncClient):
    await authenticated_client.post("/api/progress/streak")
    resp = await authenticated_client.post("/api/progress/streak")
    assert resp.json()["streak"] == 1  # same day, no increment


@pytest.mark.asyncio
async def test_get_stats(authenticated_client: AsyncClient):
    await authenticated_client.post("/api/progress/xp", json={"amount": 50, "source": "test"})
    resp = await authenticated_client.get("/api/progress/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert data["xp"] == 50
    assert "completed_nodes" in data
    assert "earned_badges" in data
```

- [ ] **Step 6: Run tests**

```bash
docker compose exec api pytest tests/test_progress.py -v
```

Expected: All 10 tests pass.

- [ ] **Step 7: Commit**

```bash
git add app/schemas/progress.py app/services/progress_service.py app/routers/progress.py tests/test_progress.py app/main.py
git commit -m "feat(backend): add progress module (xp, nodes, lessons, badges, streak)"
```

---

## Task 8: AI Proxy Schemas, Service & Router

**Files:**
- Create: `backend/app/schemas/ai.py`
- Create: `backend/app/services/ai_service.py`
- Create: `backend/app/routers/ai.py`
- Modify: `backend/app/main.py`
- Create: `backend/tests/test_ai.py`

- [ ] **Step 1: Create schemas/ai.py**

```python
# backend/app/schemas/ai.py
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(pattern=r"^(user|assistant)$")
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1)
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")


class ChatResponse(BaseModel):
    content: str


class AssessRequest(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    answers: list[str] = Field(min_length=1, max_length=10)


class AssessResponse(BaseModel):
    level: str


class TipRequest(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    level: str


class TipResponse(BaseModel):
    tip: str


class ScoreRequest(BaseModel):
    question: str = Field(min_length=1)
    answer: str = Field(min_length=1)
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")


class ScoreResponse(BaseModel):
    score: int
    feedback: str
    model_answer: str
```

- [ ] **Step 2: Create services/ai_service.py**

```python
# backend/app/services/ai_service.py
import json
import uuid

import httpx
import redis.asyncio as aioredis

from app.config import settings
from app.redis import get_redis_client

CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

MENTOR_PROMPTS = {
    "frontend": "You are Alex, an expert Frontend developer mentor with 10 years of experience at top tech companies. You teach HTML, CSS, JavaScript, React, and modern web development. You speak in a friendly, encouraging way. Give practical examples, real code snippets, and career advice. Keep responses concise and actionable.",
    "english": "You are Emma, a certified English language teacher specializing in business and conversational English. You help students improve vocabulary, grammar, pronunciation tips, and confidence in speaking. Adapt to the student's level (A1-C2). Always correct mistakes gently and explain why. Keep responses concise.",
    "callcenter": "You are Jordan, a call center training specialist with expertise in customer service, conflict resolution, and communication scripts. You train students for real call center scenarios, teach proper phone etiquette, handle objections, and build confidence. Keep responses practical and scenario-focused.",
    "cib": "You are Morgan, a Corporate & Investment Banking professional with experience at major banks. You mentor students on financial concepts, banking operations, Excel modeling basics, client communication, and interview preparation for banking roles. Keep responses professional and structured.",
}


async def _call_claude(system_prompt: str, messages: list[dict], max_tokens: int = 1024) -> str:
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(
            CLAUDE_API_URL,
            headers={
                "Content-Type": "application/json",
                "x-api-key": settings.ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": CLAUDE_MODEL,
                "max_tokens": max_tokens,
                "system": system_prompt,
                "messages": messages,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        return data["content"][0]["text"]


async def chat(messages: list[dict], direction: str, language: str = "ru") -> str:
    system = MENTOR_PROMPTS[direction]
    if language == "ru":
        system += "\n\nIMPORTANT: Respond entirely in Russian."
    formatted = [{"role": m["role"], "content": m["content"]} for m in messages]
    return await _call_claude(system, formatted)


async def assess(direction: str, answers: list[str]) -> str:
    system = f"You are assessing a student's level in {direction}. Based on their answers to assessment questions, classify them as exactly one of: beginner, intermediate, advanced. Respond with ONLY that single word."
    content = f"Here are the student's answers:\n" + "\n".join(f"Q{i+1}: {a}" for i, a in enumerate(answers)) + "\n\nWhat is their level? Respond with only: beginner, intermediate, or advanced"
    result = await _call_claude(system, [{"role": "user", "content": content}])
    level = result.strip().lower()
    if level in ("beginner", "intermediate", "advanced"):
        return level
    return "beginner"


async def tip(direction: str, level: str, user_id: str) -> str:
    r = get_redis_client()
    try:
        from datetime import date
        cache_key = f"tip:{user_id}:{date.today().isoformat()}"
        cached = await r.get(cache_key)
        if cached:
            return cached

        system = f"You are a helpful {direction} mentor. Be concise and practical."
        content = f"Give me one short, actionable tip of the day for a {level} {direction} student. Max 2 sentences."
        result = await _call_claude(system, [{"role": "user", "content": content}])

        await r.setex(cache_key, 86400, result)  # 24h cache
        return result
    finally:
        await r.aclose()


async def score(question: str, answer: str, direction: str, language: str = "ru") -> dict:
    lang_suffix = "\n\nIMPORTANT: Respond entirely in Russian." if language == "ru" else ""
    system = f'You are an expert interviewer for {direction} positions. Score the candidate\'s answer on a scale of 1-10. Respond in this exact JSON format: {{"score": <number>, "feedback": "<string>", "modelAnswer": "<string>"}}{lang_suffix}'
    content = f"Question: {question}\n\nCandidate's answer: {answer}\n\nScore this answer. Respond ONLY with JSON."
    result = await _call_claude(system, [{"role": "user", "content": content}])
    try:
        parsed = json.loads(result)
        return {
            "score": parsed["score"],
            "feedback": parsed["feedback"],
            "model_answer": parsed.get("modelAnswer", parsed.get("model_answer", "")),
        }
    except (json.JSONDecodeError, KeyError):
        return {"score": 5, "feedback": result, "model_answer": "Could not parse response"}
```

- [ ] **Step 3: Create routers/ai.py**

```python
# backend/app/routers/ai.py
import uuid

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.ai import (
    ChatRequest, ChatResponse,
    AssessRequest, AssessResponse,
    TipRequest, TipResponse,
    ScoreRequest, ScoreResponse,
)
from app.services import ai_service
from app.utils.rate_limiter import rate_limit
from app.models.user import User
from sqlalchemy import select

router = APIRouter(prefix="/api/ai", tags=["ai"])


async def _get_user_language(db: AsyncSession, user_id: uuid.UUID) -> str:
    result = await db.execute(select(User.language).where(User.id == user_id))
    return result.scalar_one_or_none() or "ru"


@router.post("/chat", response_model=ChatResponse)
async def chat(body: ChatRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    language = await _get_user_language(db, user_id)
    messages = [{"role": m.role, "content": m.content} for m in body.messages]
    content = await ai_service.chat(messages, body.direction, language)
    return ChatResponse(content=content)


@router.post("/assess", response_model=AssessResponse)
async def assess(body: AssessRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    level = await ai_service.assess(body.direction, body.answers)
    return AssessResponse(level=level)


@router.post("/tip", response_model=TipResponse)
async def tip(body: TipRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await ai_service.tip(body.direction, body.level, str(user_id))
    return TipResponse(tip=result)


@router.post("/score", response_model=ScoreResponse)
async def score_answer(body: ScoreRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    language = await _get_user_language(db, user_id)
    result = await ai_service.score(body.question, body.answer, body.direction, language)
    return ScoreResponse(**result)
```

- [ ] **Step 4: Register ai router in main.py**

Final `backend/app/main.py` router section:

```python
from app.routers import auth, users, progress, ai

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(progress.router)
app.include_router(ai.router)
```

- [ ] **Step 5: Create tests/test_ai.py**

```python
# backend/tests/test_ai.py
import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient


@pytest.mark.asyncio
@patch("app.services.ai_service._call_claude", new_callable=AsyncMock)
async def test_chat(mock_claude, authenticated_client: AsyncClient):
    mock_claude.return_value = "Hello! I'm Alex, your frontend mentor."
    resp = await authenticated_client.post("/api/ai/chat", json={
        "messages": [{"role": "user", "content": "Hello"}],
        "direction": "frontend",
    })
    assert resp.status_code == 200
    assert resp.json()["content"] == "Hello! I'm Alex, your frontend mentor."


@pytest.mark.asyncio
@patch("app.services.ai_service._call_claude", new_callable=AsyncMock)
async def test_assess(mock_claude, authenticated_client: AsyncClient):
    mock_claude.return_value = "intermediate"
    resp = await authenticated_client.post("/api/ai/assess", json={
        "direction": "frontend",
        "answers": ["HTML is a markup language", "CSS handles styling"],
    })
    assert resp.status_code == 200
    assert resp.json()["level"] == "intermediate"


@pytest.mark.asyncio
@patch("app.services.ai_service._call_claude", new_callable=AsyncMock)
async def test_tip(mock_claude, authenticated_client: AsyncClient):
    mock_claude.return_value = "Practice CSS Grid today."
    resp = await authenticated_client.post("/api/ai/tip", json={
        "direction": "frontend",
        "level": "beginner",
    })
    assert resp.status_code == 200
    assert resp.json()["tip"] == "Practice CSS Grid today."


@pytest.mark.asyncio
@patch("app.services.ai_service._call_claude", new_callable=AsyncMock)
async def test_score(mock_claude, authenticated_client: AsyncClient):
    mock_claude.return_value = '{"score": 8, "feedback": "Good answer", "modelAnswer": "Model answer"}'
    resp = await authenticated_client.post("/api/ai/score", json={
        "question": "What is React?",
        "answer": "A JavaScript library for building UIs",
        "direction": "frontend",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["score"] == 8
    assert data["feedback"] == "Good answer"


@pytest.mark.asyncio
async def test_chat_unauthorized(client: AsyncClient):
    resp = await client.post("/api/ai/chat", json={
        "messages": [{"role": "user", "content": "Hello"}],
        "direction": "frontend",
    })
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_chat_invalid_direction(authenticated_client: AsyncClient):
    resp = await authenticated_client.post("/api/ai/chat", json={
        "messages": [{"role": "user", "content": "Hello"}],
        "direction": "invalid",
    })
    assert resp.status_code == 422
```

- [ ] **Step 6: Run all tests**

```bash
docker compose exec api pytest tests/ -v
```

Expected: All tests pass (auth: 8, users: 4, progress: 10, ai: 6 = 28 total).

- [ ] **Step 7: Commit**

```bash
git add app/schemas/ai.py app/services/ai_service.py app/routers/ai.py tests/test_ai.py app/main.py
git commit -m "feat(backend): add AI proxy module (chat, assess, tip, score)"
```

---

## Task 9: Frontend — Base API Client & Auth Store

**Files:**
- Create: `src/services/api.ts`
- Create: `src/services/authApi.ts`
- Create: `src/store/authStore.ts`

- [ ] **Step 1: Create src/services/api.ts**

```typescript
// src/services/api.ts
const BASE_URL = "/api";

let accessToken: string | null = null;
let refreshPromise: Promise<string | null> | null = null;

export function setAccessToken(token: string | null) {
  accessToken = token;
}

export function getAccessToken(): string | null {
  return accessToken;
}

async function refreshAccessToken(): Promise<string | null> {
  try {
    const resp = await fetch(`${BASE_URL}/auth/refresh`, {
      method: "POST",
      credentials: "include",
    });
    if (!resp.ok) return null;
    const data = await resp.json();
    accessToken = data.access_token;
    return accessToken;
  } catch {
    return null;
  }
}

export async function apiFetch<T>(
  path: string,
  options: RequestInit = {},
): Promise<T> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string>),
  };

  if (accessToken) {
    headers["Authorization"] = `Bearer ${accessToken}`;
  }

  let resp = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers,
    credentials: "include",
  });

  if (resp.status === 401 && accessToken) {
    if (!refreshPromise) {
      refreshPromise = refreshAccessToken();
    }
    const newToken = await refreshPromise;
    refreshPromise = null;

    if (newToken) {
      headers["Authorization"] = `Bearer ${newToken}`;
      resp = await fetch(`${BASE_URL}${path}`, {
        ...options,
        headers,
        credentials: "include",
      });
    } else {
      accessToken = null;
      window.location.href = "/login";
      throw new Error("Session expired");
    }
  }

  if (!resp.ok) {
    const error = await resp.json().catch(() => ({ detail: resp.statusText }));
    throw new Error(error.detail || `API error: ${resp.status}`);
  }

  if (resp.status === 204) return undefined as T;
  return resp.json();
}
```

- [ ] **Step 2: Create src/services/authApi.ts**

```typescript
// src/services/authApi.ts
import { apiFetch, setAccessToken } from "./api";

interface AuthResponse {
  access_token: string;
  token_type: string;
}

interface RegisterParams {
  email: string;
  password: string;
  name: string;
  direction: string;
  assessment_level?: string;
  language?: string;
}

export async function register(params: RegisterParams): Promise<void> {
  const data = await apiFetch<AuthResponse>("/auth/register", {
    method: "POST",
    body: JSON.stringify(params),
  });
  setAccessToken(data.access_token);
}

export async function login(email: string, password: string): Promise<void> {
  const data = await apiFetch<AuthResponse>("/auth/login", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });
  setAccessToken(data.access_token);
}

export async function logout(): Promise<void> {
  try {
    await apiFetch("/auth/logout", { method: "POST" });
  } finally {
    setAccessToken(null);
  }
}
```

- [ ] **Step 3: Create src/store/authStore.ts**

```typescript
// src/store/authStore.ts
import { create } from "zustand";
import { apiFetch, setAccessToken } from "@/services/api";
import * as authApi from "@/services/authApi";

interface UserData {
  id: string;
  email: string;
  name: string;
  direction: string;
  assessment_level: string;
  language: string;
  avatar_url: string | null;
  xp: number;
  level: string;
  streak: number;
  longest_streak: number;
  completed_nodes: string[];
  completed_lessons: string[];
  earned_badges: string[];
}

interface AuthState {
  user: UserData | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  register: (params: {
    email: string;
    password: string;
    name: string;
    direction: string;
    assessment_level?: string;
    language?: string;
  }) => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  fetchUser: () => Promise<void>;
  tryRestore: () => Promise<void>;
}

export const useAuthStore = create<AuthState>()((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: true,

  register: async (params) => {
    await authApi.register(params);
    const user = await apiFetch<UserData>("/users/me");
    set({ user, isAuthenticated: true });
  },

  login: async (email, password) => {
    await authApi.login(email, password);
    const user = await apiFetch<UserData>("/users/me");
    set({ user, isAuthenticated: true });
  },

  logout: async () => {
    await authApi.logout();
    set({ user: null, isAuthenticated: false });
  },

  fetchUser: async () => {
    const user = await apiFetch<UserData>("/users/me");
    set({ user, isAuthenticated: true });
  },

  tryRestore: async () => {
    try {
      // Attempt to refresh token from httpOnly cookie
      const resp = await fetch("/api/auth/refresh", {
        method: "POST",
        credentials: "include",
      });
      if (resp.ok) {
        const data = await resp.json();
        setAccessToken(data.access_token);
        const user = await apiFetch<UserData>("/users/me");
        set({ user, isAuthenticated: true, isLoading: false });
      } else {
        set({ isLoading: false });
      }
    } catch {
      set({ isLoading: false });
    }
  },
}));
```

- [ ] **Step 4: Commit**

```bash
git add src/services/api.ts src/services/authApi.ts src/store/authStore.ts
git commit -m "feat(frontend): add API client, auth API, and auth store"
```

---

## Task 10: Frontend — Login & Register Pages

**Files:**
- Create: `src/pages/Login.tsx`
- Create: `src/pages/Register.tsx`

- [ ] **Step 1: Create src/pages/Login.tsx**

```tsx
// src/pages/Login.tsx
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { LogIn, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { useAuthStore } from "@/store/authStore";
import { useTranslation } from "@/hooks/useTranslation";

export default function Login() {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const login = useAuthStore((s) => s.login);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md"
      >
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold">
            <span className="text-primary">Path</span>
            <span className="text-accent">Mind</span>
          </h1>
          <p className="text-text-secondary mt-2">Sign in to continue learning</p>
        </div>

        <Card>
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input
              label="Email"
              type="email"
              placeholder="your@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <Input
              label="Password"
              type="password"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />

            {error && (
              <p className="text-red-400 text-sm">{error}</p>
            )}

            <Button type="submit" className="w-full" disabled={loading}>
              {loading ? <Loader2 className="animate-spin" size={18} /> : <LogIn size={18} />}
              <span className="ml-2">Sign In</span>
            </Button>
          </form>

          <p className="text-center text-text-secondary text-sm mt-4">
            Don't have an account?{" "}
            <Link to="/" className="text-primary hover:underline">
              Sign Up
            </Link>
          </p>
        </Card>
      </motion.div>
    </div>
  );
}
```

- [ ] **Step 2: Create src/pages/Register.tsx**

```tsx
// src/pages/Register.tsx
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { UserPlus, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { useAuthStore } from "@/store/authStore";

export default function Register() {
  const navigate = useNavigate();
  const register = useAuthStore((s) => s.register);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await register({ email, password, name, direction: "frontend" });
      navigate("/");  // Go to onboarding to pick direction
    } catch (err: any) {
      setError(err.message || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md"
      >
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold">
            <span className="text-primary">Path</span>
            <span className="text-accent">Mind</span>
          </h1>
          <p className="text-text-secondary mt-2">Create your account</p>
        </div>

        <Card>
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input
              label="Name"
              placeholder="Your name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
            <Input
              label="Email"
              type="email"
              placeholder="your@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <Input
              label="Password"
              type="password"
              placeholder="At least 8 characters"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              minLength={8}
            />

            {error && (
              <p className="text-red-400 text-sm">{error}</p>
            )}

            <Button type="submit" className="w-full" disabled={loading}>
              {loading ? <Loader2 className="animate-spin" size={18} /> : <UserPlus size={18} />}
              <span className="ml-2">Create Account</span>
            </Button>
          </form>

          <p className="text-center text-text-secondary text-sm mt-4">
            Already have an account?{" "}
            <Link to="/login" className="text-primary hover:underline">
              Sign In
            </Link>
          </p>
        </Card>
      </motion.div>
    </div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/Login.tsx src/pages/Register.tsx
git commit -m "feat(frontend): add Login and Register pages"
```

---

## Task 11: Frontend — Migrate App.tsx, claudeApi, userStore, Onboarding

**Files:**
- Modify: `src/App.tsx`
- Modify: `src/services/claudeApi.ts`
- Modify: `src/store/userStore.ts`
- Modify: `src/pages/Onboarding.tsx`

- [ ] **Step 1: Update App.tsx**

Replace `src/App.tsx` with:

```tsx
// src/App.tsx
import { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuthStore } from "@/store/authStore";
import Login from "@/pages/Login";
import Register from "@/pages/Register";
import Onboarding from "@/pages/Onboarding";
import Dashboard from "@/pages/Dashboard";
import Roadmap from "@/pages/Roadmap";
import Mentor from "@/pages/Mentor";
import Simulator from "@/pages/Simulator";
import Lesson from "@/pages/Lesson";
import Achievements from "@/pages/Achievements";
import Profile from "@/pages/Profile";
import { Loader2 } from "lucide-react";

function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading } = useAuthStore();

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="animate-spin text-primary" size={32} />
      </div>
    );
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

export default function App() {
  const tryRestore = useAuthStore((s) => s.tryRestore);

  useEffect(() => {
    tryRestore();
  }, [tryRestore]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/"
          element={
            <AuthGuard>
              <Onboarding />
            </AuthGuard>
          }
        />
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <Dashboard />
            </AuthGuard>
          }
        />
        <Route
          path="/roadmap"
          element={
            <AuthGuard>
              <Roadmap />
            </AuthGuard>
          }
        />
        <Route
          path="/mentor"
          element={
            <AuthGuard>
              <Mentor />
            </AuthGuard>
          }
        />
        <Route
          path="/simulator"
          element={
            <AuthGuard>
              <Simulator />
            </AuthGuard>
          }
        />
        <Route
          path="/lesson/:id"
          element={
            <AuthGuard>
              <Lesson />
            </AuthGuard>
          }
        />
        <Route
          path="/achievements"
          element={
            <AuthGuard>
              <Achievements />
            </AuthGuard>
          }
        />
        <Route
          path="/profile"
          element={
            <AuthGuard>
              <Profile />
            </AuthGuard>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
```

- [ ] **Step 2: Update claudeApi.ts**

Replace `src/services/claudeApi.ts` with:

```typescript
// src/services/claudeApi.ts
import { apiFetch } from "./api";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export async function sendMessage(
  systemPrompt: string,
  messages: ChatMessage[],
  direction: string = "frontend",
): Promise<string> {
  const data = await apiFetch<{ content: string }>("/ai/chat", {
    method: "POST",
    body: JSON.stringify({
      messages: messages.map((m) => ({ role: m.role, content: m.content })),
      direction,
    }),
  });
  return data.content;
}

export async function assessLevel(
  direction: string,
  answers: string[],
): Promise<"beginner" | "intermediate" | "advanced"> {
  const data = await apiFetch<{ level: string }>("/ai/assess", {
    method: "POST",
    body: JSON.stringify({ direction, answers }),
  });
  const level = data.level;
  if (level === "beginner" || level === "intermediate" || level === "advanced") {
    return level;
  }
  return "beginner";
}

export async function generateTip(
  direction: string,
  level: string,
): Promise<string> {
  const data = await apiFetch<{ tip: string }>("/ai/tip", {
    method: "POST",
    body: JSON.stringify({ direction, level }),
  });
  return data.tip;
}

export async function scoreAnswer(
  question: string,
  answer: string,
  direction: string,
): Promise<{ score: number; feedback: string; modelAnswer: string }> {
  const data = await apiFetch<{ score: number; feedback: string; model_answer: string }>("/ai/score", {
    method: "POST",
    body: JSON.stringify({ question, answer, direction }),
  });
  return { score: data.score, feedback: data.feedback, modelAnswer: data.model_answer };
}
```

- [ ] **Step 3: Update userStore.ts**

Replace `src/store/userStore.ts` with:

```typescript
// src/store/userStore.ts
import { create } from "zustand";
import { apiFetch } from "@/services/api";
import type { Direction, Level } from "@/types";

interface UserState {
  addXP: (amount: number, source: string) => Promise<void>;
  completeNode: (nodeId: string) => Promise<void>;
  completeLesson: (lessonId: string) => Promise<void>;
  earnBadge: (badgeId: string) => Promise<void>;
  updateStreak: () => Promise<void>;
}

export const useUserStore = create<UserState>()(() => ({
  addXP: async (amount, source) => {
    await apiFetch("/progress/xp", {
      method: "POST",
      body: JSON.stringify({ amount, source }),
    });
  },

  completeNode: async (nodeId) => {
    await apiFetch("/progress/node", {
      method: "POST",
      body: JSON.stringify({ node_id: nodeId }),
    });
  },

  completeLesson: async (lessonId) => {
    await apiFetch("/progress/lesson", {
      method: "POST",
      body: JSON.stringify({ lesson_id: lessonId }),
    });
  },

  earnBadge: async (badgeId) => {
    await apiFetch("/progress/badge", {
      method: "POST",
      body: JSON.stringify({ badge_id: badgeId }),
    });
  },

  updateStreak: async () => {
    await apiFetch("/progress/streak", { method: "POST" });
  },
}));
```

- [ ] **Step 4: Update Onboarding.tsx handleFinish**

In `src/pages/Onboarding.tsx`, replace the `handleFinish` function:

```typescript
const handleFinish = async () => {
  if (!selectedDirection || !assessmentResult) return;
  try {
    // Update user direction and assessment on backend
    await apiFetch("/users/me", {
      method: "PATCH",
      body: JSON.stringify({ direction: selectedDirection }),
    });
    await fetchUser();
    navigate("/dashboard");
  } catch {
    navigate("/dashboard");
  }
};
```

And update imports at the top of the file — add:

```typescript
import { apiFetch } from "@/services/api";
import { useAuthStore } from "@/store/authStore";
```

Inside the component, add:

```typescript
const fetchUser = useAuthStore((s) => s.fetchUser);
```

Remove the old `setProfile` and `completeOnboarding` usage.

- [ ] **Step 5: Commit**

```bash
git add src/App.tsx src/services/claudeApi.ts src/store/userStore.ts src/pages/Onboarding.tsx
git commit -m "feat(frontend): migrate to backend API (auth, claude proxy, progress)"
```

---

## Task 12: Vite Proxy & End-to-End Verification

**Files:**
- Modify: `vite.config.ts`

- [ ] **Step 1: Add Vite proxy for development**

In `vite.config.ts`, add a proxy so `/api` calls go to the backend during `npm run dev`:

```typescript
// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
});
```

- [ ] **Step 2: Start backend and verify**

```bash
cd backend
docker compose up -d
```

Wait for healthy status, then:

```bash
curl http://localhost:8000/api/health
```

Expected: `{"status":"ok"}`

- [ ] **Step 3: Start frontend and verify**

```bash
cd ..  # project root
npm run dev
```

Open browser at `http://localhost:5173/login`. Verify:
1. Login page renders
2. Register link works
3. After registration → redirects to onboarding
4. After onboarding → dashboard loads with data from API

- [ ] **Step 4: Run all backend tests**

```bash
cd backend
docker compose exec api pytest tests/ -v --tb=short
```

Expected: All 28 tests pass.

- [ ] **Step 5: Commit**

```bash
git add vite.config.ts
git commit -m "feat: add Vite proxy for backend API in development"
```

---

## Summary

| Task | Description | Tests |
|------|-------------|-------|
| 1 | Docker Compose & Infrastructure | — |
| 2 | FastAPI App Core & Config | health check |
| 3 | SQLAlchemy Models & Alembic | migration |
| 4 | Security Utils & Dependencies | — |
| 5 | Auth (register, login, refresh, logout) | 8 tests |
| 6 | Users (me, update, public profile) | 4 tests |
| 7 | Progress (xp, nodes, lessons, badges, streak) | 10 tests |
| 8 | AI Proxy (chat, assess, tip, score) | 6 tests |
| 9 | Frontend API client & auth store | — |
| 10 | Frontend Login & Register pages | — |
| 11 | Frontend migration (App, claudeApi, userStore, Onboarding) | — |
| 12 | Vite proxy & end-to-end verification | integration |

**Total: 12 tasks, 28 backend tests, full-stack integration.**
