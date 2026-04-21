import json

import httpx
import redis.asyncio as aioredis

from app.config import settings
from app.redis import get_redis_client

CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

BARSBEK_BASE = """You are Barsbek — the AI learning assistant of Bars AI platform. You are friendly, supportive, and highly knowledgeable. You speak with warmth and encouragement, like a wise older brother who genuinely wants the student to succeed. You use clear explanations, real-world examples, and practical advice. When the student struggles, you break things down into simpler steps. You celebrate their progress. You never talk down to the student."""

MENTOR_PROMPTS = {
    "frontend": f"{BARSBEK_BASE}\n\nYour specialty is Frontend development — HTML, CSS, JavaScript, TypeScript, React, and modern web development. Give practical code examples and career advice.",
    "english": f"{BARSBEK_BASE}\n\nYour specialty is English language teaching — vocabulary, grammar, pronunciation, conversational and business English. Adapt to the student's level (A1-C2). Correct mistakes gently and explain why.",
    "callcenter": f"{BARSBEK_BASE}\n\nYour specialty is call center training — customer service, conflict resolution, communication scripts, phone etiquette. Train with real scenarios and build confidence.",
    "cib": f"{BARSBEK_BASE}\n\nYour specialty is Corporate & Investment Banking — financial concepts, banking operations, Excel modeling, client communication, interview prep. Be professional and structured.",
    "programming": f"{BARSBEK_BASE}\n\nYour specialty is programming — Python, algorithms, data structures, debugging, best practices. Give clear code examples and explain step by step.",
    "design": f"{BARSBEK_BASE}\n\nYour specialty is UI/UX and graphic design — layout, typography, color theory, Figma, user research. Give visual thinking advice and practical tips.",
    "marketing": f"{BARSBEK_BASE}\n\nYour specialty is digital marketing — SMM, targeting, copywriting, analytics, content strategy. Give actionable tips with real examples.",
    "languages": f"{BARSBEK_BASE}\n\nYour specialty is language learning — you help with any language the student is studying. Use immersive techniques, mnemonics, and cultural context.",
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
    content = "Here are the student's answers:\n" + "\n".join(f"Q{i+1}: {a}" for i, a in enumerate(answers)) + "\n\nWhat is their level? Respond with only: beginner, intermediate, or advanced"
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

        system = f"You are Barsbek, the AI assistant of Bars AI platform. You are a helpful {direction} mentor. Be concise and practical."
        content = f"Give me one short, actionable tip of the day for a {level} {direction} student. Max 2 sentences."
        result = await _call_claude(system, [{"role": "user", "content": content}])

        await r.setex(cache_key, 86400, result)
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


async def transcribe(audio_bytes: bytes, filename: str = "recording.webm") -> dict:
    """Send audio to OpenAI Whisper and return transcription."""
    from openai import AsyncOpenAI
    import io

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = filename

    response = await client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="verbose_json",
    )

    return {
        "text": response.text,
        "confidence": getattr(response, "confidence", 0.9),
    }


LANG_NAMES = {"ru": "Russian", "en": "English", "kz": "Kazakh", "de": "German", "fr": "French"}


async def check_translation(
    sentence: str,
    user_answer: str,
    source_language: str,
    target_language: str,
) -> dict:
    """Use Claude to evaluate a translation."""
    src = LANG_NAMES.get(source_language, source_language)
    tgt = LANG_NAMES.get(target_language, target_language)

    system = (
        f"You are a language teacher evaluating a student's translation from {src} to {tgt}. "
        "Respond in JSON with keys: correct (bool), feedback (string in Russian, 1-2 sentences), "
        "suggested (the best translation). Accept semantically correct translations even if wording differs. "
        "Only output valid JSON, no markdown."
    )
    content = f"Original ({src}): {sentence}\nStudent's translation ({tgt}): {user_answer}"

    raw = await _call_claude(system, [{"role": "user", "content": content}], max_tokens=256)

    try:
        data = json.loads(raw)
        return {
            "correct": bool(data.get("correct", False)),
            "feedback": str(data.get("feedback", "")),
            "suggested": str(data.get("suggested", "")),
        }
    except (json.JSONDecodeError, KeyError):
        return {"correct": False, "feedback": "Ошибка проверки.", "suggested": ""}
