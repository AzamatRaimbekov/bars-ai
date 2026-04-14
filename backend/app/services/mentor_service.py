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
    msg_count_result = await db.execute(
        select(func.count()).select_from(MentorMessage).where(MentorMessage.session_id == session.id)
    )
    total = msg_count_result.scalar() or 0
    if total <= 2:
        session.title = content[:80] if len(content) <= 80 else content[:77] + "..."

    # Update knowledge profile every 10 messages
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
