# AI Mentor Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add memory/context persistence, interactive exercises, progress-based recommendations, and voice lessons to the AI mentor.

**Architecture:** 4 backend modules (memory, exercises, progress advisor, voice lessons) with a new `/api/mentor` router, 3 new DB tables, and updated frontend Mentor page with session sidebar, exercise blocks, recommendation cards, and voice lesson mode.

**Tech Stack:** FastAPI, SQLAlchemy 2.0 async, PostgreSQL, Alembic, Anthropic Claude API, React, Zustand, TypeScript

**Spec:** `docs/superpowers/specs/2026-04-14-ai-mentor-upgrade-design.md`

---

## File Structure

### Backend — New Files
- `backend/app/models/mentor.py` — MentorSession, MentorMessage, KnowledgeProfile models
- `backend/app/schemas/mentor.py` — Pydantic request/response schemas
- `backend/app/services/mentor_service.py` — Orchestrator + memory + exercises + recommendations + voice lesson logic
- `backend/app/routers/mentor.py` — All `/api/mentor/*` endpoints

### Backend — Modified Files
- `backend/app/models/__init__.py` — Add new model imports
- `backend/app/main.py` — Register mentor router

### Frontend — New Files
- `src/hooks/useMentorSessions.ts` — Session CRUD hook
- `src/hooks/useRecommendations.ts` — Recommendations hook
- `src/hooks/useVoiceLesson.ts` — Voice lesson state machine hook
- `src/components/mentor/SessionList.tsx` — Session sidebar
- `src/components/mentor/ExerciseBlock.tsx` — Exercise renderer
- `src/components/mentor/ExerciseResult.tsx` — Exercise result card
- `src/components/mentor/RecommendationCard.tsx` — Recommendation card
- `src/components/mentor/VoiceLessonMode.tsx` — Voice lesson UI

### Frontend — Modified Files
- `src/pages/Mentor.tsx` — Integrate all new components
- `src/services/mentorApi.ts` — New API service (or create new)
- `src/hooks/useChat.ts` — Update to work with session_id

---

## Tasks

### Task 1: Backend Models & Migration

**Files:**
- Create: `backend/app/models/mentor.py`
- Modify: `backend/app/models/__init__.py`

- [ ] **Step 1: Create mentor models**

Create `backend/app/models/mentor.py`:

```python
import uuid
from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class MentorSession(Base):
    __tablename__ = "mentor_sessions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    direction: Mapped[str] = mapped_column(String(20), nullable=False)
    title: Mapped[str] = mapped_column(String(200), default="Новая сессия")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    messages: Mapped[list["MentorMessage"]] = relationship(back_populates="session", cascade="all, delete-orphan", order_by="MentorMessage.created_at")


class MentorMessage(Base):
    __tablename__ = "mentor_messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("mentor_sessions.id", ondelete="CASCADE"))
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    session: Mapped["MentorSession"] = relationship(back_populates="messages")


class KnowledgeProfile(Base):
    __tablename__ = "knowledge_profiles"
    __table_args__ = (UniqueConstraint("user_id", "direction", name="uq_knowledge_user_direction"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    direction: Mapped[str] = mapped_column(String(20), nullable=False)
    strengths: Mapped[dict] = mapped_column(JSON, default=list)
    weaknesses: Mapped[dict] = mapped_column(JSON, default=list)
    notes: Mapped[dict] = mapped_column(JSON, default=list)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
```

- [ ] **Step 2: Update models __init__.py**

Add to `backend/app/models/__init__.py`:

```python
from app.models.mentor import MentorSession, MentorMessage, KnowledgeProfile
```

And add to `__all__`:

```python
"MentorSession", "MentorMessage", "KnowledgeProfile",
```

- [ ] **Step 3: Generate and run Alembic migration**

```bash
cd backend && venv/bin/python -m alembic revision --autogenerate -m "add mentor tables"
cd backend && venv/bin/python -m alembic upgrade head
```

- [ ] **Step 4: Commit**

```bash
git add backend/app/models/mentor.py backend/app/models/__init__.py backend/alembic/versions/
git commit -m "feat: add mentor_sessions, mentor_messages, knowledge_profiles tables"
```

---

### Task 2: Backend Schemas

**Files:**
- Create: `backend/app/schemas/mentor.py`

- [ ] **Step 1: Create mentor schemas**

Create `backend/app/schemas/mentor.py`:

```python
from pydantic import BaseModel, Field
from datetime import datetime


class MentorChatRequest(BaseModel):
    session_id: str | None = None
    content: str = Field(min_length=1)


class MentorChatResponse(BaseModel):
    content: str
    session_id: str
    message_id: str


class SessionCreate(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    title: str | None = None


class SessionOut(BaseModel):
    id: str
    direction: str
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MessageOut(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class KnowledgeProfileOut(BaseModel):
    direction: str
    strengths: list
    weaknesses: list
    notes: list
    updated_at: datetime

    class Config:
        from_attributes = True


class RecommendationItem(BaseModel):
    lesson_id: str
    lesson_title: str
    course_title: str
    reason: str
    priority: str


class RecommendationsResponse(BaseModel):
    weekly_plan: list[RecommendationItem]
    stats: dict


class VoiceLessonRequest(BaseModel):
    session_id: str
    action: str = Field(pattern=r"^(start|next|repeat|answer)$")
    topic: str | None = None
    content: str | None = None


class VoiceLessonResponse(BaseModel):
    phase: str
    content: str
    exercise: dict | None = None
    progress: float
    is_complete: bool
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/schemas/mentor.py
git commit -m "feat: add mentor Pydantic schemas"
```

---

### Task 3: Backend Mentor Service

**Files:**
- Create: `backend/app/services/mentor_service.py`

- [ ] **Step 1: Create mentor service with all functions**

Create `backend/app/services/mentor_service.py`:

```python
import json
import uuid
from datetime import datetime, timezone

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.mentor import MentorSession, MentorMessage, KnowledgeProfile
from app.models.progress import Progress
from app.models.course import Course, CourseSection, CourseLesson, CourseEnrollment, CourseLessonProgress
from app.models.user import User
from app.services.ai_service import _call_claude, MENTOR_PROMPTS


# ── Session Management ──

async def get_sessions(db: AsyncSession, user_id: uuid.UUID) -> list[MentorSession]:
    result = await db.execute(
        select(MentorSession)
        .where(MentorSession.user_id == user_id)
        .order_by(MentorSession.updated_at.desc())
        .limit(50)
    )
    return list(result.scalars().all())


async def create_session(db: AsyncSession, user_id: uuid.UUID, direction: str, title: str | None = None) -> MentorSession:
    session = MentorSession(
        user_id=user_id,
        direction=direction,
        title=title or "Новая сессия",
    )
    db.add(session)
    await db.flush()
    return session


async def get_messages(db: AsyncSession, session_id: uuid.UUID, user_id: uuid.UUID, limit: int = 50, offset: int = 0) -> list[MentorMessage]:
    result = await db.execute(
        select(MentorMessage)
        .join(MentorSession)
        .where(MentorMessage.session_id == session_id, MentorSession.user_id == user_id)
        .order_by(MentorMessage.created_at)
        .offset(offset)
        .limit(limit)
    )
    return list(result.scalars().all())


async def delete_session(db: AsyncSession, session_id: uuid.UUID, user_id: uuid.UUID) -> bool:
    result = await db.execute(
        select(MentorSession).where(MentorSession.id == session_id, MentorSession.user_id == user_id)
    )
    session = result.scalar_one_or_none()
    if not session:
        return False
    await db.delete(session)
    return True


# ── Knowledge Profile ──

async def get_or_create_profile(db: AsyncSession, user_id: uuid.UUID, direction: str) -> KnowledgeProfile:
    result = await db.execute(
        select(KnowledgeProfile).where(
            KnowledgeProfile.user_id == user_id,
            KnowledgeProfile.direction == direction,
        )
    )
    profile = result.scalar_one_or_none()
    if not profile:
        profile = KnowledgeProfile(user_id=user_id, direction=direction, strengths=[], weaknesses=[], notes=[])
        db.add(profile)
        await db.flush()
    return profile


async def update_knowledge_profile(db: AsyncSession, user_id: uuid.UUID, direction: str, messages: list[dict]) -> None:
    """Use Claude to analyze recent conversation and update knowledge profile."""
    profile = await get_or_create_profile(db, user_id, direction)

    analysis_prompt = (
        "Analyze this student conversation and extract:\n"
        "1. strengths - topics the student understands well (list of strings)\n"
        "2. weaknesses - topics the student struggles with (list of strings)\n"
        "3. notes - important observations about the student (list of strings)\n\n"
        "Respond ONLY with valid JSON: {\"strengths\": [...], \"weaknesses\": [...], \"notes\": [...]}\n"
        "Merge with existing profile, don't duplicate."
    )

    existing = json.dumps({"strengths": profile.strengths, "weaknesses": profile.weaknesses, "notes": profile.notes}, ensure_ascii=False)
    conversation = "\n".join(f"{m['role']}: {m['content']}" for m in messages[-20:])

    try:
        raw = await _call_claude(
            analysis_prompt,
            [{"role": "user", "content": f"Existing profile:\n{existing}\n\nRecent conversation:\n{conversation}"}],
            max_tokens=512,
        )
        data = json.loads(raw)
        profile.strengths = data.get("strengths", profile.strengths)
        profile.weaknesses = data.get("weaknesses", profile.weaknesses)
        profile.notes = data.get("notes", profile.notes)
    except (json.JSONDecodeError, Exception):
        pass


# ── Chat Orchestrator ──

async def chat(db: AsyncSession, user_id: uuid.UUID, session_id: str | None, content: str) -> dict:
    """Main chat function — orchestrates memory, context, and response."""
    # Get user info
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one()
    direction = user.direction or "frontend"
    language = user.language or "ru"

    # Get or create session
    if session_id:
        sess_result = await db.execute(
            select(MentorSession).where(MentorSession.id == uuid.UUID(session_id), MentorSession.user_id == user_id)
        )
        session = sess_result.scalar_one_or_none()
        if not session:
            session = await create_session(db, user_id, direction)
    else:
        session = await create_session(db, user_id, direction)

    # Save user message
    user_msg = MentorMessage(session_id=session.id, role="user", content=content)
    db.add(user_msg)
    await db.flush()

    # Build context
    history = await get_messages(db, session.id, user_id, limit=20)
    profile = await get_or_create_profile(db, user_id, direction)
    progress = await _get_progress_summary(db, user_id)

    # Build system prompt
    base_prompt = MENTOR_PROMPTS.get(direction, MENTOR_PROMPTS["frontend"])
    context_parts = [
        base_prompt,
        f"\nStudent: {user.name}, Level: {user.assessment_level or 'beginner'}, Direction: {direction}",
        f"\nKnowledge Profile — Strengths: {json.dumps(profile.strengths, ensure_ascii=False)}, Weaknesses: {json.dumps(profile.weaknesses, ensure_ascii=False)}",
        f"\nCourse Progress: {progress}",
    ]
    if language == "ru":
        context_parts.append("\n\nIMPORTANT: Respond entirely in Russian.")

    context_parts.append(
        "\n\nYou can give exercises. Wrap them in markers:\n"
        "[EXERCISE:qa] for question-answer\n"
        "[EXERCISE:code] for code tasks (ONLY for frontend direction)\n"
        "[EXERCISE:roleplay] for role-play scenarios\n"
        "[/EXERCISE] to close\n"
        "[EXERCISE_RESULT] for grading with score and feedback\n"
        "[/EXERCISE_RESULT] to close\n"
        "You can recommend lessons: use format [RECOMMEND:lesson_id:lesson_title]\n"
        "Keep responses concise and conversational."
    )

    system_prompt = "".join(context_parts)
    messages_for_api = [{"role": m.role, "content": m.content} for m in history]

    # Call Claude
    response = await _call_claude(system_prompt, messages_for_api, max_tokens=1500)

    # Save assistant message
    assistant_msg = MentorMessage(session_id=session.id, role="assistant", content=response)
    db.add(assistant_msg)

    # Update session title from first message
    msg_count = await db.execute(
        select(func.count()).select_from(MentorMessage).where(MentorMessage.session_id == session.id)
    )
    if msg_count.scalar() <= 2:
        session.title = content[:80] if len(content) <= 80 else content[:77] + "..."

    # Update knowledge profile every 10 messages
    total = msg_count.scalar() or 0
    if total > 0 and total % 10 == 0:
        all_msgs = [{"role": m.role, "content": m.content} for m in history]
        await update_knowledge_profile(db, user_id, direction, all_msgs)

    await db.commit()

    return {
        "content": response,
        "session_id": str(session.id),
        "message_id": str(assistant_msg.id),
    }


async def _get_progress_summary(db: AsyncSession, user_id: uuid.UUID) -> str:
    result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    progress = result.scalar_one_or_none()
    if not progress:
        return "No progress data."
    completed = len(progress.completed_lessons) if progress.completed_lessons else 0
    return f"XP: {progress.xp}, Level: {progress.level}, Completed lessons: {completed}, Streak: {progress.streak} days"


# ── Recommendations ──

async def get_recommendations(db: AsyncSession, user_id: uuid.UUID) -> dict:
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one()
    direction = user.direction or "frontend"

    profile = await get_or_create_profile(db, user_id, direction)
    progress_result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    progress = progress_result.scalar_one_or_none()

    completed_ids = set(progress.completed_lessons) if progress and progress.completed_lessons else set()

    # Find enrolled courses
    enrollments = await db.execute(
        select(CourseEnrollment.course_id).where(CourseEnrollment.user_id == user_id)
    )
    enrolled_course_ids = [row[0] for row in enrollments.all()]

    recommendations = []
    for course_id in enrolled_course_ids[:5]:
        course_result = await db.execute(select(Course).where(Course.id == course_id))
        course = course_result.scalar_one_or_none()
        if not course:
            continue

        sections = await db.execute(
            select(CourseSection).where(CourseSection.course_id == course_id).order_by(CourseSection.position)
        )
        for section in sections.scalars():
            lessons = await db.execute(
                select(CourseLesson).where(CourseLesson.section_id == section.id).order_by(CourseLesson.position)
            )
            for lesson in lessons.scalars():
                if str(lesson.id) not in completed_ids:
                    # Check if topic matches weakness
                    priority = "normal"
                    reason = "Следующий непройденный урок"
                    if profile.weaknesses:
                        for weakness in profile.weaknesses:
                            if weakness.lower() in lesson.title.lower():
                                priority = "high"
                                reason = f"У тебя пробел в теме: {weakness}"
                                break

                    recommendations.append({
                        "lesson_id": str(lesson.id),
                        "lesson_title": lesson.title,
                        "course_title": course.title,
                        "reason": reason,
                        "priority": priority,
                    })

                    if len(recommendations) >= 5:
                        break
            if len(recommendations) >= 5:
                break
        if len(recommendations) >= 5:
            break

    # Sort high priority first
    recommendations.sort(key=lambda x: 0 if x["priority"] == "high" else 1)

    total_lessons = 0
    for cid in enrolled_course_ids[:5]:
        count = await db.execute(
            select(func.count()).select_from(CourseLesson)
            .join(CourseSection)
            .where(CourseSection.course_id == cid)
        )
        total_lessons += count.scalar() or 0

    completed_pct = round(len(completed_ids) / max(total_lessons, 1) * 100)

    return {
        "weekly_plan": recommendations[:5],
        "stats": {
            "completed_percentage": completed_pct,
            "strong_topics": profile.strengths[:5] if profile.strengths else [],
            "weak_topics": profile.weaknesses[:5] if profile.weaknesses else [],
        },
    }


# ── Voice Lesson ──

VOICE_LESSON_PHASES = ["intro", "explain", "check", "practice", "summary"]

async def voice_lesson(db: AsyncSession, user_id: uuid.UUID, session_id: str, action: str, topic: str | None = None, content: str | None = None) -> dict:
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one()
    direction = user.direction or "frontend"
    language = user.language or "ru"

    sess_result = await db.execute(
        select(MentorSession).where(MentorSession.id == uuid.UUID(session_id), MentorSession.user_id == user_id)
    )
    session = sess_result.scalar_one_or_none()
    if not session:
        return {"phase": "error", "content": "Session not found", "exercise": None, "progress": 0, "is_complete": True}

    history = await get_messages(db, session.id, user_id, limit=30)
    messages_for_api = [{"role": m.role, "content": m.content} for m in history]

    lang_instruction = "\n\nIMPORTANT: Respond entirely in Russian. Keep it conversational for voice." if language == "ru" else "\nKeep it conversational for voice."

    if action == "start":
        system = (
            f"{MENTOR_PROMPTS.get(direction, MENTOR_PROMPTS['frontend'])}\n"
            f"You are starting a structured voice lesson on: {topic}.\n"
            f"Phase: INTRODUCTION (30 seconds).\n"
            f"Introduce the topic, explain why it's important, and what the student will learn.\n"
            f"Keep it SHORT — this will be spoken aloud.{lang_instruction}"
        )
        messages_for_api.append({"role": "user", "content": f"Start a voice lesson on: {topic}"})
        response = await _call_claude(system, messages_for_api, max_tokens=300)
        # Save messages
        db.add(MentorMessage(session_id=session.id, role="user", content=f"[VOICE_LESSON:start] {topic}"))
        db.add(MentorMessage(session_id=session.id, role="assistant", content=response))
        await db.commit()
        return {"phase": "intro", "content": response, "exercise": None, "progress": 0.1, "is_complete": False}

    elif action == "next":
        # Determine current phase from conversation
        phase_idx = _detect_phase(messages_for_api)
        next_phase = VOICE_LESSON_PHASES[min(phase_idx + 1, len(VOICE_LESSON_PHASES) - 1)]

        phase_instructions = {
            "explain": "Phase: EXPLANATION (2-3 min). Explain the main concepts with examples. Clear and simple.",
            "check": "Phase: CHECK (1-2 min). Ask the student 2-3 questions to verify understanding.",
            "practice": "Phase: PRACTICE (2-3 min). Give a practical exercise or role-play scenario.",
            "summary": "Phase: SUMMARY (30 sec). Summarize what was learned. Suggest what to study next.",
        }

        system = (
            f"{MENTOR_PROMPTS.get(direction, MENTOR_PROMPTS['frontend'])}\n"
            f"{phase_instructions.get(next_phase, '')}\n"
            f"Keep it SHORT for voice.{lang_instruction}"
        )
        messages_for_api.append({"role": "user", "content": f"[VOICE_LESSON:next] Continue to {next_phase}"})
        response = await _call_claude(system, messages_for_api, max_tokens=500)
        db.add(MentorMessage(session_id=session.id, role="user", content=f"[VOICE_LESSON:next]"))
        db.add(MentorMessage(session_id=session.id, role="assistant", content=response))
        await db.commit()

        progress_val = (VOICE_LESSON_PHASES.index(next_phase) + 1) / len(VOICE_LESSON_PHASES)
        return {"phase": next_phase, "content": response, "exercise": None, "progress": progress_val, "is_complete": next_phase == "summary"}

    elif action == "answer":
        system = (
            f"{MENTOR_PROMPTS.get(direction, MENTOR_PROMPTS['frontend'])}\n"
            f"The student answered a question during a voice lesson. Evaluate their answer.\n"
            f"If correct, praise and move on. If wrong, explain gently and give another chance.\n"
            f"Keep it SHORT for voice.{lang_instruction}"
        )
        messages_for_api.append({"role": "user", "content": content or ""})
        response = await _call_claude(system, messages_for_api, max_tokens=400)
        db.add(MentorMessage(session_id=session.id, role="user", content=content or ""))
        db.add(MentorMessage(session_id=session.id, role="assistant", content=response))
        await db.commit()

        phase_idx = _detect_phase(messages_for_api)
        current_phase = VOICE_LESSON_PHASES[min(phase_idx, len(VOICE_LESSON_PHASES) - 1)]
        progress_val = (phase_idx + 1) / len(VOICE_LESSON_PHASES)
        return {"phase": current_phase, "content": response, "exercise": None, "progress": progress_val, "is_complete": False}

    elif action == "repeat":
        system = (
            f"{MENTOR_PROMPTS.get(direction, MENTOR_PROMPTS['frontend'])}\n"
            f"The student asked you to repeat. Rephrase your last explanation in simpler terms.\n"
            f"Keep it SHORT for voice.{lang_instruction}"
        )
        messages_for_api.append({"role": "user", "content": "Повтори, пожалуйста, попроще."})
        response = await _call_claude(system, messages_for_api, max_tokens=400)
        db.add(MentorMessage(session_id=session.id, role="user", content="[VOICE_LESSON:repeat]"))
        db.add(MentorMessage(session_id=session.id, role="assistant", content=response))
        await db.commit()

        phase_idx = _detect_phase(messages_for_api)
        current_phase = VOICE_LESSON_PHASES[min(phase_idx, len(VOICE_LESSON_PHASES) - 1)]
        progress_val = (phase_idx + 1) / len(VOICE_LESSON_PHASES)
        return {"phase": current_phase, "content": response, "exercise": None, "progress": progress_val, "is_complete": False}

    return {"phase": "error", "content": "Unknown action", "exercise": None, "progress": 0, "is_complete": True}


def _detect_phase(messages: list[dict]) -> int:
    """Detect current voice lesson phase by counting [VOICE_LESSON:next] markers."""
    count = sum(1 for m in messages if "[VOICE_LESSON:" in m.get("content", ""))
    return min(count, len(VOICE_LESSON_PHASES) - 1)
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/services/mentor_service.py
git commit -m "feat: add mentor service — memory, exercises, recommendations, voice lessons"
```

---

### Task 4: Backend Router & Registration

**Files:**
- Create: `backend/app/routers/mentor.py`
- Modify: `backend/app/main.py`

- [ ] **Step 1: Create mentor router**

Create `backend/app/routers/mentor.py`:

```python
import uuid

from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.mentor import (
    MentorChatRequest, MentorChatResponse,
    SessionCreate, SessionOut, MessageOut,
    KnowledgeProfileOut, RecommendationsResponse,
    VoiceLessonRequest, VoiceLessonResponse,
)
from app.services import mentor_service
from app.utils.rate_limiter import rate_limit

router = APIRouter(prefix="/api/mentor", tags=["mentor"])


@router.get("/sessions", response_model=list[SessionOut])
async def list_sessions(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    sessions = await mentor_service.get_sessions(db, user_id)
    return [SessionOut(id=str(s.id), direction=s.direction, title=s.title, created_at=s.created_at, updated_at=s.updated_at) for s in sessions]


@router.post("/sessions", response_model=SessionOut)
async def create_session(body: SessionCreate, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    session = await mentor_service.create_session(db, user_id, body.direction, body.title)
    await db.commit()
    return SessionOut(id=str(session.id), direction=session.direction, title=session.title, created_at=session.created_at, updated_at=session.updated_at)


@router.get("/sessions/{session_id}/messages", response_model=list[MessageOut])
async def get_messages(
    session_id: uuid.UUID,
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0),
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    messages = await mentor_service.get_messages(db, session_id, user_id, limit, offset)
    return [MessageOut(id=str(m.id), role=m.role, content=m.content, created_at=m.created_at) for m in messages]


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: uuid.UUID, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    deleted = await mentor_service.delete_session(db, session_id, user_id)
    await db.commit()
    if not deleted:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Session not found")
    return {"ok": True}


@router.get("/profile", response_model=KnowledgeProfileOut)
async def get_profile(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    from app.models.user import User
    from sqlalchemy import select
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one()
    profile = await mentor_service.get_or_create_profile(db, user_id, user.direction or "frontend")
    await db.commit()
    return KnowledgeProfileOut(direction=profile.direction, strengths=profile.strengths, weaknesses=profile.weaknesses, notes=profile.notes, updated_at=profile.updated_at)


@router.post("/chat", response_model=MentorChatResponse)
async def chat(body: MentorChatRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await mentor_service.chat(db, user_id, body.session_id, body.content)
    return MentorChatResponse(**result)


@router.get("/recommendations", response_model=RecommendationsResponse)
async def recommendations(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    result = await mentor_service.get_recommendations(db, user_id)
    return RecommendationsResponse(**result)


@router.post("/voice-lesson", response_model=VoiceLessonResponse)
async def voice_lesson(body: VoiceLessonRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await mentor_service.voice_lesson(db, user_id, body.session_id, body.action, body.topic, body.content)
    return VoiceLessonResponse(**result)
```

- [ ] **Step 2: Register router in main.py**

Add to `backend/app/main.py` after the existing router imports:

```python
from app.routers import mentor
app.include_router(mentor.router)
```

- [ ] **Step 3: Commit**

```bash
git add backend/app/routers/mentor.py backend/app/main.py
git commit -m "feat: add /api/mentor endpoints — chat, sessions, recommendations, voice lessons"
```

---

### Task 5: Frontend API Service

**Files:**
- Create: `src/services/mentorApi.ts`

- [ ] **Step 1: Create mentor API service**

Create `src/services/mentorApi.ts`:

```typescript
import { apiFetch } from './api'

export interface Session {
  id: string
  direction: string
  title: string
  created_at: string
  updated_at: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  created_at: string
}

export interface KnowledgeProfile {
  direction: string
  strengths: string[]
  weaknesses: string[]
  notes: string[]
  updated_at: string
}

export interface RecommendationItem {
  lesson_id: string
  lesson_title: string
  course_title: string
  reason: string
  priority: string
}

export interface Recommendations {
  weekly_plan: RecommendationItem[]
  stats: {
    completed_percentage: number
    strong_topics: string[]
    weak_topics: string[]
  }
}

export interface ChatResponse {
  content: string
  session_id: string
  message_id: string
}

export interface VoiceLessonResponse {
  phase: string
  content: string
  exercise: Record<string, unknown> | null
  progress: number
  is_complete: boolean
}

export const mentorApi = {
  getSessions: () => apiFetch<Session[]>('/mentor/sessions'),

  createSession: (direction: string, title?: string) =>
    apiFetch<Session>('/mentor/sessions', {
      method: 'POST',
      body: JSON.stringify({ direction, title }),
    }),

  getMessages: (sessionId: string, limit = 50, offset = 0) =>
    apiFetch<Message[]>(`/mentor/sessions/${sessionId}/messages?limit=${limit}&offset=${offset}`),

  deleteSession: (sessionId: string) =>
    apiFetch<{ ok: boolean }>(`/mentor/sessions/${sessionId}`, { method: 'DELETE' }),

  getProfile: () => apiFetch<KnowledgeProfile>('/mentor/profile'),

  chat: (content: string, sessionId?: string) =>
    apiFetch<ChatResponse>('/mentor/chat', {
      method: 'POST',
      body: JSON.stringify({ content, session_id: sessionId }),
    }),

  getRecommendations: () => apiFetch<Recommendations>('/mentor/recommendations'),

  voiceLesson: (sessionId: string, action: string, topic?: string, content?: string) =>
    apiFetch<VoiceLessonResponse>('/mentor/voice-lesson', {
      method: 'POST',
      body: JSON.stringify({ session_id: sessionId, action, topic, content }),
    }),
}
```

- [ ] **Step 2: Commit**

```bash
git add src/services/mentorApi.ts
git commit -m "feat: add mentorApi frontend service"
```

---

### Task 6: Frontend Hooks

**Files:**
- Create: `src/hooks/useMentorSessions.ts`
- Create: `src/hooks/useRecommendations.ts`
- Create: `src/hooks/useVoiceLesson.ts`

- [ ] **Step 1: Create useMentorSessions hook**

Create `src/hooks/useMentorSessions.ts`:

```typescript
import { useState, useEffect, useCallback } from 'react'
import { mentorApi, type Session, type Message } from '@/services/mentorApi'

export function useMentorSessions() {
  const [sessions, setSessions] = useState<Session[]>([])
  const [activeSession, setActiveSession] = useState<Session | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const loadSessions = useCallback(async () => {
    try {
      const data = await mentorApi.getSessions()
      setSessions(data)
    } catch (err) {
      console.error('Failed to load sessions:', err)
    }
  }, [])

  const createSession = useCallback(async (direction: string) => {
    const session = await mentorApi.createSession(direction)
    setSessions(prev => [session, ...prev])
    setActiveSession(session)
    setMessages([])
    return session
  }, [])

  const selectSession = useCallback(async (session: Session) => {
    setActiveSession(session)
    setIsLoading(true)
    try {
      const msgs = await mentorApi.getMessages(session.id)
      setMessages(msgs)
    } catch (err) {
      console.error('Failed to load messages:', err)
    } finally {
      setIsLoading(false)
    }
  }, [])

  const deleteSession = useCallback(async (sessionId: string) => {
    await mentorApi.deleteSession(sessionId)
    setSessions(prev => prev.filter(s => s.id !== sessionId))
    if (activeSession?.id === sessionId) {
      setActiveSession(null)
      setMessages([])
    }
  }, [activeSession])

  const addMessage = useCallback((msg: Message) => {
    setMessages(prev => [...prev, msg])
  }, [])

  useEffect(() => { loadSessions() }, [loadSessions])

  return {
    sessions, activeSession, messages, isLoading,
    createSession, selectSession, deleteSession, addMessage,
    setActiveSession,
  }
}
```

- [ ] **Step 2: Create useRecommendations hook**

Create `src/hooks/useRecommendations.ts`:

```typescript
import { useState, useEffect } from 'react'
import { mentorApi, type Recommendations } from '@/services/mentorApi'

export function useRecommendations() {
  const [data, setData] = useState<Recommendations | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    mentorApi.getRecommendations()
      .then(setData)
      .catch(err => console.error('Failed to load recommendations:', err))
      .finally(() => setIsLoading(false))
  }, [])

  return { recommendations: data, isLoading }
}
```

- [ ] **Step 3: Create useVoiceLesson hook**

Create `src/hooks/useVoiceLesson.ts`:

```typescript
import { useState, useCallback } from 'react'
import { mentorApi, type VoiceLessonResponse } from '@/services/mentorApi'

type Phase = 'idle' | 'intro' | 'explain' | 'check' | 'practice' | 'summary' | 'complete'

export function useVoiceLesson(sessionId: string | null) {
  const [phase, setPhase] = useState<Phase>('idle')
  const [progress, setProgress] = useState(0)
  const [lastResponse, setLastResponse] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleResponse = useCallback((res: VoiceLessonResponse) => {
    setPhase(res.is_complete ? 'complete' : res.phase as Phase)
    setProgress(res.progress)
    setLastResponse(res.content)
  }, [])

  const start = useCallback(async (topic: string) => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'start', topic)
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const next = useCallback(async () => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'next')
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const answer = useCallback(async (content: string) => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'answer', undefined, content)
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const repeat = useCallback(async () => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'repeat')
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const reset = useCallback(() => {
    setPhase('idle')
    setProgress(0)
    setLastResponse('')
  }, [])

  return { phase, progress, lastResponse, isLoading, start, next, answer, repeat, reset }
}
```

- [ ] **Step 4: Commit**

```bash
git add src/hooks/useMentorSessions.ts src/hooks/useRecommendations.ts src/hooks/useVoiceLesson.ts
git commit -m "feat: add mentor hooks — sessions, recommendations, voice lessons"
```

---

### Task 7: Frontend Mentor Components

**Files:**
- Create: `src/components/mentor/SessionList.tsx`
- Create: `src/components/mentor/ExerciseBlock.tsx`
- Create: `src/components/mentor/RecommendationCard.tsx`
- Create: `src/components/mentor/VoiceLessonMode.tsx`

- [ ] **Step 1: Create all mentor components**

This task creates 4 new React components for the mentor UI. The subagent should:

1. Read `src/pages/Mentor.tsx` to understand the existing UI patterns, Tailwind classes, and component structure
2. Read `src/components/chat/ChatWindow.tsx` to understand the chat message rendering pattern
3. Create the 4 components following the same styling patterns

**SessionList.tsx** — sidebar with session list:
- List of past sessions with title and date
- "New session" button at top
- Active session highlighted
- Delete button (trash icon) on hover
- Props: `sessions, activeSession, onSelect, onCreate, onDelete`

**ExerciseBlock.tsx** — renders exercises inside chat messages:
- Parses `[EXERCISE:type]...[/EXERCISE]` markers from message content
- For `code` type: shows code input area with "Submit" button
- For `qa` type: shows question with input field
- For `roleplay` type: shows scenario indicator
- Parses `[EXERCISE_RESULT]...[/EXERCISE_RESULT]` for results: score badge + feedback
- Props: `content: string, onSubmit: (answer: string) => void`

**RecommendationCard.tsx** — recommendation banner:
- Shows top 1-2 recommendations with lesson title, reason, priority badge
- Link to lesson: `/courses/{courseId}/learn/{lessonId}`
- Props: `recommendations: RecommendationItem[]`

**VoiceLessonMode.tsx** — voice lesson overlay:
- Progress bar showing current phase (5 phases)
- Phase labels: Введение → Объяснение → Проверка → Практика → Итог
- Large text area showing current content
- Buttons: "Далее", "Повтори", mic button for answers
- Props: `phase, progress, content, isLoading, onNext, onRepeat, onAnswer, onClose`

- [ ] **Step 2: Commit**

```bash
git add src/components/mentor/
git commit -m "feat: add mentor UI components — SessionList, ExerciseBlock, RecommendationCard, VoiceLessonMode"
```

---

### Task 8: Update Mentor Page — Integration

**Files:**
- Modify: `src/pages/Mentor.tsx`

- [ ] **Step 1: Update Mentor page to integrate all modules**

Read the current `src/pages/Mentor.tsx` and update it to:

1. Import and use `useMentorSessions` hook instead of `useChatStore`
2. Import and use `useRecommendations` hook
3. Import and use `useVoiceLesson` hook
4. Add `SessionList` sidebar on the left
5. Add `RecommendationCard` above chat messages (shown if recommendations exist)
6. Use `mentorApi.chat()` instead of `sendMessage()` — passes `session_id`
7. Parse exercise markers in assistant messages using `ExerciseBlock`
8. Add "Voice Lesson" button that opens `VoiceLessonMode`
9. Keep existing voice mode (free conversation) as separate feature
10. When user sends a message, call `mentorApi.chat(content, activeSession?.id)` and add both messages to local state

The existing chat UI structure should be preserved — just replace the data source from in-memory store to persistent sessions.

- [ ] **Step 2: Verify the app compiles**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && npm run build 2>&1 | tail -5
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/Mentor.tsx
git commit -m "feat: integrate mentor modules into Mentor page — sessions, exercises, recommendations, voice lessons"
```
