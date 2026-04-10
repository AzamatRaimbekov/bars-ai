import json

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

        system = f"You are a helpful {direction} mentor. Be concise and practical."
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
