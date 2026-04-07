# Stage 1: Backend Foundation — Design Spec

**Date:** 2026-04-07
**Status:** Approved
**Stack:** FastAPI + PostgreSQL + Redis + Docker Compose

---

## 1. Architecture

```
React App :5173
    ↓
Nginx (reverse proxy :80)
    ├── /api/* → FastAPI :8000
    └── /*     → React static

FastAPI :8000
    ├── auth module     — JWT (access 30min + refresh 7d)
    ├── users module    — Profile CRUD
    ├── progress module — XP, nodes, lessons, badges, streak
    └── ai module       — Claude API proxy

PostgreSQL :5432 — users, progress, badges, refresh_tokens
Redis :6379      — sessions, rate-limit, daily tips cache
```

**Tech stack:**
- Python 3.12, FastAPI, Uvicorn
- SQLAlchemy 2.0 (async) + Alembic (migrations)
- Pydantic v2 (validation)
- python-jose (JWT), passlib[bcrypt] (passwords)
- httpx (async Claude API calls)
- aioredis (Redis)
- Docker Compose (Postgres + Redis + API + Nginx)

---

## 2. Project Structure

```
backend/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
├── app/
│   ├── main.py                 # FastAPI app, lifespan, middleware
│   ├── config.py               # Settings (Pydantic BaseSettings)
│   ├── database.py             # Async engine, session factory
│   ├── redis.py                # Redis connection pool
│   ├── dependencies.py         # get_db, get_current_user, get_redis
│   │
│   ├── models/                 # SQLAlchemy models
│   │   ├── user.py
│   │   ├── progress.py
│   │   └── badge.py
│   │
│   ├── schemas/                # Pydantic schemas (request/response)
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── progress.py
│   │   └── ai.py
│   │
│   ├── routers/                # API endpoints (thin)
│   │   ├── auth.py             # register, login, refresh, logout
│   │   ├── users.py            # GET/PATCH /me, GET /users/{id}
│   │   ├── progress.py         # XP, nodes, lessons, badges, streak
│   │   └── ai.py               # Claude proxy: chat, assess, tip, score
│   │
│   ├── services/               # Business logic
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── progress_service.py
│   │   └── ai_service.py
│   │
│   └── utils/
│       ├── security.py         # Hash passwords, JWT encode/decode
│       └── rate_limiter.py     # Redis-based rate limiting
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_progress.py
│   └── test_ai.py
│
└── nginx/
    └── nginx.conf
```

**Principles:**
- Router → Service → Model (thin routers, logic in services)
- Schemas separated from Models (Pydantic for API, SQLAlchemy for DB)
- Reusable dependencies (auth, db, redis)

---

## 3. Database Schema

### users
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK, default gen_random_uuid() |
| email | VARCHAR(255) | UNIQUE, NOT NULL |
| password | VARCHAR(255) | NOT NULL (bcrypt hash) |
| name | VARCHAR(100) | NOT NULL |
| direction | VARCHAR(20) | NOT NULL (frontend/english/callcenter/cib) |
| assessment_level | VARCHAR(20) | DEFAULT 'beginner' |
| language | VARCHAR(5) | DEFAULT 'ru' |
| avatar_url | VARCHAR(500) | NULLABLE |
| created_at | TIMESTAMPTZ | DEFAULT now() |
| updated_at | TIMESTAMPTZ | DEFAULT now() |

### progress
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK |
| user_id | UUID | UNIQUE, FK → users(id) ON DELETE CASCADE |
| xp | INTEGER | DEFAULT 0 |
| level | VARCHAR(20) | DEFAULT 'Novice' |
| streak | INTEGER | DEFAULT 0 |
| longest_streak | INTEGER | DEFAULT 0 |
| last_active_date | DATE | NULLABLE |
| completed_nodes | TEXT[] | DEFAULT '{}' |
| completed_lessons | TEXT[] | DEFAULT '{}' |
| updated_at | TIMESTAMPTZ | DEFAULT now() |

### user_badges
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK |
| user_id | UUID | FK → users(id) ON DELETE CASCADE |
| badge_id | VARCHAR(50) | NOT NULL |
| earned_at | TIMESTAMPTZ | DEFAULT now() |
| | | UNIQUE(user_id, badge_id) |

### refresh_tokens
| Column | Type | Constraints |
|--------|------|-------------|
| id | UUID | PK |
| user_id | UUID | FK → users(id) ON DELETE CASCADE |
| token_hash | VARCHAR(255) | NOT NULL (SHA-256) |
| expires_at | TIMESTAMPTZ | NOT NULL |
| revoked | BOOLEAN | DEFAULT false |
| created_at | TIMESTAMPTZ | DEFAULT now() |

**Design decisions:**
- UUID PKs — no auto-increment leaks
- Progress as separate table — separates auth from game data
- Badges are static on frontend, DB stores only earned facts
- Refresh tokens stored as SHA-256 hash — safe even if DB leaks
- completed_nodes/lessons as TEXT[] — PostgreSQL arrays, simple at current scale

---

## 4. API Endpoints

### Auth (public)
| Method | Path | Body | Response |
|--------|------|------|----------|
| POST | /api/auth/register | { email, password, name, direction } | { access_token, user } |
| POST | /api/auth/login | { email, password } | { access_token } + httpOnly cookie |
| POST | /api/auth/refresh | (cookie) | { access_token } + new cookie |
| POST | /api/auth/logout | (cookie) | 204 |

### Users (auth required)
| Method | Path | Body | Response |
|--------|------|------|----------|
| GET | /api/users/me | — | full profile + progress |
| PATCH | /api/users/me | { name?, language?, avatar_url? } | updated profile |
| GET | /api/users/{id} | — | public profile (name, level, badges) |

### Progress (auth required)
| Method | Path | Body | Response |
|--------|------|------|----------|
| POST | /api/progress/xp | { amount, source } | { xp, level, leveled_up } |
| POST | /api/progress/node | { node_id } | { completed_nodes } |
| POST | /api/progress/lesson | { lesson_id } | { completed_lessons } |
| POST | /api/progress/badge | { badge_id } | { badge, earned_at } |
| POST | /api/progress/streak | — | { streak, longest_streak } |
| GET | /api/progress/stats | — | full stats object |

### AI (auth required, rate-limited 20 req/min)
| Method | Path | Body | Response |
|--------|------|------|----------|
| POST | /api/ai/chat | { messages, direction } | { content } |
| POST | /api/ai/assess | { direction, answers } | { level } |
| POST | /api/ai/tip | { direction, level } | { tip } (cached 24h in Redis) |
| POST | /api/ai/score | { question, answer, direction } | { score, feedback, model_answer } |

---

## 5. Infrastructure (Docker Compose)

### Services:
- **api** — FastAPI on Uvicorn, hot-reload in dev, depends on postgres + redis
- **postgres** — PostgreSQL 16 Alpine, volume `pgdata`, healthcheck via pg_isready
- **redis** — Redis 7 Alpine, volume `redisdata`, healthcheck via redis-cli ping
- **nginx** — reverse proxy, /api/* → api:8000, /* → frontend

### Environment (.env):
```
DB_PASSWORD=secure_password_here
DATABASE_URL=postgresql+asyncpg://pathmind:${DB_PASSWORD}@postgres:5432/pathmind
REDIS_URL=redis://redis:6379/0
ANTHROPIC_API_KEY=sk-ant-...
JWT_SECRET=random_64_char_string
JWT_ACCESS_EXPIRE_MINUTES=30
JWT_REFRESH_EXPIRE_DAYS=7
```

### Dockerfile:
- Python 3.12-slim base
- pip install requirements.txt
- Alembic migrations on startup
- Uvicorn with --reload for dev

---

## 6. Frontend Migration

### New files:
- `src/services/api.ts` — base HTTP client with JWT interceptors
- `src/services/authApi.ts` — register, login, refresh, logout
- `src/store/authStore.ts` — tokens, isAuthenticated, user
- `src/pages/Login.tsx` — login page
- `src/pages/Register.tsx` — registration page

### Modified files:
- `claudeApi.ts` — calls go through /api/ai/* instead of direct Anthropic
- `userStore.ts` — remove localStorage persist, read/write via API
- `App.tsx` — add Login/Register routes, AuthGuard via token
- `Onboarding.tsx` — register API call instead of localStorage

### Token strategy:
- Access token in memory (Zustand) — not localStorage (XSS-safe)
- Refresh token in httpOnly cookie (sent automatically)
- Interceptor: on 401 → attempt refresh → if fails → logout
