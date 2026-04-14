import json
import random
from datetime import date

import redis.asyncio as aioredis

QUEST_POOL = [
    {
        "id": "complete_lessons_3",
        "title": {"en": "Complete 3 Lessons", "ru": "Пройдите 3 урока"},
        "description": {"en": "Complete 3 lessons today", "ru": "Пройдите 3 урока сегодня"},
        "xp_reward": 50,
        "target": 3,
    },
    {
        "id": "earn_xp_100",
        "title": {"en": "Earn 100 XP", "ru": "Заработайте 100 XP"},
        "description": {"en": "Earn 100 XP today", "ru": "Заработайте 100 XP сегодня"},
        "xp_reward": 30,
        "target": 100,
    },
    {
        "id": "complete_lessons_1",
        "title": {"en": "Complete 1 Lesson", "ru": "Пройдите 1 урок"},
        "description": {"en": "Complete 1 lesson today", "ru": "Пройдите 1 урок сегодня"},
        "xp_reward": 20,
        "target": 1,
    },
    {
        "id": "maintain_streak",
        "title": {"en": "Maintain Your Streak", "ru": "Сохраните серию"},
        "description": {"en": "Keep your learning streak alive", "ru": "Поддержите свою серию обучения"},
        "xp_reward": 25,
        "target": 1,
    },
    {
        "id": "complete_quiz_2",
        "title": {"en": "Pass 2 Quizzes", "ru": "Пройдите 2 теста"},
        "description": {"en": "Pass 2 quizzes today", "ru": "Пройдите 2 теста сегодня"},
        "xp_reward": 40,
        "target": 2,
    },
    {
        "id": "study_30min",
        "title": {"en": "Study for 30 Minutes", "ru": "Учитесь 30 минут"},
        "description": {"en": "Study for 30 minutes today", "ru": "Учитесь 30 минут сегодня"},
        "xp_reward": 35,
        "target": 30,
    },
    {
        "id": "earn_xp_50",
        "title": {"en": "Earn 50 XP", "ru": "Заработайте 50 XP"},
        "description": {"en": "Earn 50 XP today", "ru": "Заработайте 50 XP сегодня"},
        "xp_reward": 20,
        "target": 50,
    },
    {
        "id": "complete_node",
        "title": {"en": "Complete a Topic", "ru": "Завершите тему"},
        "description": {"en": "Complete a topic on the roadmap", "ru": "Завершите тему на дорожной карте"},
        "xp_reward": 45,
        "target": 1,
    },
    {
        "id": "earn_xp_200",
        "title": {"en": "Earn 200 XP", "ru": "Заработайте 200 XP"},
        "description": {"en": "Earn 200 XP today", "ru": "Заработайте 200 XP сегодня"},
        "xp_reward": 60,
        "target": 200,
    },
    {
        "id": "complete_lessons_5",
        "title": {"en": "Complete 5 Lessons", "ru": "Пройдите 5 уроков"},
        "description": {"en": "Complete 5 lessons today", "ru": "Пройдите 5 уроков сегодня"},
        "xp_reward": 75,
        "target": 5,
    },
]

QUEST_MAP = {q["id"]: q for q in QUEST_POOL}


def _today_str() -> str:
    return date.today().isoformat()


async def _get_or_assign_quests(r: aioredis.Redis, user_id: str) -> list[dict]:
    today = _today_str()
    key = f"quests:{user_id}:{today}"
    raw = await r.get(key)
    if raw:
        return json.loads(raw)

    picked = random.sample(QUEST_POOL, 3)
    quest_ids = [q["id"] for q in picked]
    await r.set(key, json.dumps(quest_ids), ex=86400)
    return picked


async def _get_quest_ids(r: aioredis.Redis, user_id: str) -> list[str]:
    today = _today_str()
    key = f"quests:{user_id}:{today}"
    raw = await r.get(key)
    if raw:
        ids = json.loads(raw)
        if isinstance(ids[0], dict):
            return [q["id"] for q in ids]
        return ids
    return []


async def get_daily_quests(r: aioredis.Redis, user_id: str) -> dict:
    today = _today_str()
    assigned = await _get_or_assign_quests(r, user_id)
    quest_ids = [q["id"] if isinstance(q, dict) else q for q in assigned]

    progress_key = f"quest_progress:{user_id}:{today}"
    progress_data = await r.hgetall(progress_key)

    quests = []
    for qid in quest_ids:
        template = QUEST_MAP.get(qid)
        if not template:
            continue
        current = int(progress_data.get(qid, 0))
        completed = current >= template["target"]
        quests.append({
            "id": qid,
            "title": template["title"],
            "description": template["description"],
            "xp_reward": template["xp_reward"],
            "target": template["target"],
            "progress": min(current, template["target"]),
            "completed": completed,
        })

    return {"quests": quests, "date": today}


async def check_quest_progress(r: aioredis.Redis, user_id: str) -> dict:
    today = _today_str()
    quest_ids = await _get_quest_ids(r, user_id)
    if not quest_ids:
        assigned = await _get_or_assign_quests(r, user_id)
        quest_ids = [q["id"] if isinstance(q, dict) else q for q in assigned]

    progress_key = f"quest_progress:{user_id}:{today}"

    for qid in quest_ids:
        template = QUEST_MAP.get(qid)
        if not template:
            continue
        current = int(await r.hget(progress_key, qid) or 0)
        if current < template["target"]:
            await r.hincrby(progress_key, qid, 1)

    await r.expire(progress_key, 86400)

    return await get_daily_quests(r, user_id)
