"""
Seed: CIB, Call Center, SMM courses.
Usage: cd backend && PYTHONPATH=. python -m app.seed_courses
"""
import asyncio, uuid
from sqlalchemy import select
from app.database import async_session
from app.models.course import Course, CourseSection, CourseLesson
from app.models.user import User

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSES = [
    {
        "title": "CIB — Корпоративный и инвестиционный банкинг",
        "description": "Полный курс по корпоративному и инвестиционному банкингу: финансовые рынки, банковские операции, M&A, финансовый анализ и подготовка к интервью.",
        "category": "CIB",
        "difficulty": "Intermediate",
        "sections": [
            {"title": "Основы финансов", "pos": 0, "lessons": [
                {"title": "Типы рынков", "xp": 20, "v2": "cib-1-1"},
                {"title": "Ключевые участники", "xp": 15, "v2": "cib-1-2"},
                {"title": "Финансовая отчётность", "xp": 20, "v2": "cib-2-1"},
                {"title": "Ключевые коэффициенты", "xp": 20, "v2": "cib-2-2"},
                {"title": "Концепции TVM", "xp": 30, "v2": "cib-3-1"},
                {"title": "Облигации и доходность", "xp": 35, "v2": "cib-4-1"},
            ]},
            {"title": "Банковские операции", "pos": 1, "lessons": [
                {"title": "Основы банкинга", "xp": 30, "v2": "cib-5-1"},
                {"title": "Корпоративные кредиты", "xp": 35, "v2": "cib-6-1"},
                {"title": "Торговое финансирование", "xp": 30, "v2": "cib-7-1"},
                {"title": "Валюта и казначейство", "xp": 30, "v2": "cib-8-1"},
            ]},
            {"title": "Инвестиционный банкинг", "pos": 2, "lessons": [
                {"title": "Процесс M&A", "xp": 20, "v2": "cib-9-1"},
                {"title": "Типы сделок", "xp": 20, "v2": "cib-9-2"},
                {"title": "Рынки акционерного капитала", "xp": 35, "v2": "cib-10-1"},
                {"title": "Рынки долгового капитала", "xp": 35, "v2": "cib-11-1"},
                {"title": "Питч-буки", "xp": 30, "v2": "cib-12-1"},
            ]},
            {"title": "Финансовый анализ", "pos": 3, "lessons": [
                {"title": "Модель DCF", "xp": 25, "v2": "cib-13-1"},
                {"title": "WACC и терминальная стоимость", "xp": 20, "v2": "cib-13-2"},
                {"title": "Сравнительный анализ", "xp": 35, "v2": "cib-14-1"},
                {"title": "Основы LBO", "xp": 40, "v2": "cib-15-1"},
                {"title": "Навыки Excel", "xp": 35, "v2": "cib-16-1"},
            ]},
            {"title": "Подготовка к интервью", "pos": 4, "lessons": [
                {"title": "Поведенческие вопросы", "xp": 30, "v2": "cib-17-1"},
                {"title": "Техническая подготовка", "xp": 40, "v2": "cib-18-1"},
                {"title": "Кейсы", "xp": 35, "v2": "cib-19-1"},
                {"title": "Нетворкинг", "xp": 25, "v2": "cib-20-1"},
            ]},
        ],
    },
    {
        "title": "Call Center — Операторская работа",
        "description": "Курс для операторов колл-центра: коммуникация, телефонный этикет, обслуживание клиентов, решение конфликтов и продвинутые навыки.",
        "category": "Call Center",
        "difficulty": "Beginner",
        "sections": [
            {"title": "Основы коммуникации", "pos": 0, "lessons": [
                {"title": "Чёткая коммуникация", "xp": 25, "v2": "cc-1-1"},
                {"title": "Навыки слушания", "xp": 25, "v2": "cc-2-1"},
                {"title": "Тон и эмпатия", "xp": 25, "v2": "cc-3-1"},
                {"title": "Лексика обслуживания", "xp": 25, "v2": "cc-4-1"},
            ]},
            {"title": "Телефонный этикет", "pos": 1, "lessons": [
                {"title": "Скрипты приветствия", "xp": 20, "v2": "cc-5-1"},
                {"title": "Удержание и перевод", "xp": 20, "v2": "cc-6-1"},
                {"title": "Скрипты завершения", "xp": 20, "v2": "cc-7-1"},
                {"title": "Ведение записей", "xp": 20, "v2": "cc-8-1"},
            ]},
            {"title": "Обслуживание клиентов", "pos": 2, "lessons": [
                {"title": "Решение проблем", "xp": 30, "v2": "cc-9-1"},
                {"title": "Обучение по продукту", "xp": 30, "v2": "cc-10-1"},
                {"title": "Техники продаж", "xp": 25, "v2": "cc-11-1"},
                {"title": "Стратегии FCR", "xp": 25, "v2": "cc-12-1"},
            ]},
            {"title": "Решение конфликтов", "pos": 3, "lessons": [
                {"title": "Деэскалация", "xp": 30, "v2": "cc-13-1"},
                {"title": "Обработка жалоб", "xp": 30, "v2": "cc-14-1"},
                {"title": "Позитивный отказ", "xp": 25, "v2": "cc-15-1"},
                {"title": "Эскалация", "xp": 25, "v2": "cc-16-1"},
            ]},
            {"title": "Продвинутые навыки", "pos": 4, "lessons": [
                {"title": "Метрики эффективности", "xp": 30, "v2": "cc-17-1"},
                {"title": "Управление стрессом", "xp": 25, "v2": "cc-18-1"},
                {"title": "Мультиканальность", "xp": 30, "v2": "cc-19-1"},
                {"title": "Лидерство в команде", "xp": 30, "v2": "cc-20-1"},
            ]},
        ],
    },
    {
        "title": "SMM — Маркетинг в социальных сетях",
        "description": "Полный курс по SMM: стратегия, контент-маркетинг, таргетированная реклама, аналитика, работа с блогерами и построение бренда в соцсетях.",
        "category": "Other",
        "difficulty": "Beginner",
        "sections": [
            {"title": "Основы SMM", "pos": 0, "lessons": [
                {"title": "Что такое SMM", "xp": 15, "v2": ""},
                {"title": "Платформы и их аудитория", "xp": 20, "v2": ""},
                {"title": "Построение стратегии", "xp": 25, "v2": ""},
                {"title": "Целевая аудитория и персоны", "xp": 20, "v2": ""},
            ]},
            {"title": "Контент-маркетинг", "pos": 1, "lessons": [
                {"title": "Типы контента", "xp": 20, "v2": ""},
                {"title": "Контент-план и календарь", "xp": 25, "v2": ""},
                {"title": "Визуальный контент и Canva", "xp": 30, "v2": ""},
                {"title": "Копирайтинг для соцсетей", "xp": 25, "v2": ""},
                {"title": "Видео и Reels", "xp": 30, "v2": ""},
            ]},
            {"title": "Таргетированная реклама", "pos": 2, "lessons": [
                {"title": "Основы таргета", "xp": 25, "v2": ""},
                {"title": "Facebook/Instagram Ads", "xp": 35, "v2": ""},
                {"title": "Аудитории и ретаргетинг", "xp": 30, "v2": ""},
                {"title": "A/B тестирование", "xp": 25, "v2": ""},
                {"title": "Бюджетирование и ROI", "xp": 30, "v2": ""},
            ]},
            {"title": "Аналитика и метрики", "pos": 3, "lessons": [
                {"title": "KPI в SMM", "xp": 20, "v2": ""},
                {"title": "Инструменты аналитики", "xp": 25, "v2": ""},
                {"title": "Отчётность", "xp": 20, "v2": ""},
                {"title": "Оптимизация на основе данных", "xp": 30, "v2": ""},
            ]},
            {"title": "Продвинутый SMM", "pos": 4, "lessons": [
                {"title": "Работа с блогерами", "xp": 30, "v2": ""},
                {"title": "Комьюнити-менеджмент", "xp": 25, "v2": ""},
                {"title": "Кризисные коммуникации", "xp": 25, "v2": ""},
                {"title": "Личный бренд", "xp": 30, "v2": ""},
                {"title": "Монетизация и продажи", "xp": 35, "v2": ""},
            ]},
        ],
    },
]


async def seed():
    async with async_session() as db:
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        if not user:
            print("No users found"); return

        for c_data in COURSES:
            existing = await db.execute(select(Course).where(Course.title == c_data["title"]))
            if existing.scalar_one_or_none():
                print(f"  SKIP: '{c_data['title']}' already exists")
                continue

            course = Course(
                id=uuid.uuid4(),
                title=c_data["title"],
                slug=c_data["title"].lower().replace(" ", "-")[:40] + "-" + uuid.uuid4().hex[:6],
                description=c_data["description"],
                author_id=user.id,
                category=c_data["category"],
                difficulty=c_data["difficulty"],
                price=0, currency="USD", status="published",
            )
            db.add(course)
            await db.flush()

            all_positions, global_idx = [], 0
            for sec_data in c_data["sections"]:
                section = CourseSection(
                    id=uuid.uuid4(), course_id=course.id,
                    title=sec_data["title"], position=sec_data["pos"],
                )
                db.add(section)
                await db.flush()

                for i, l_data in enumerate(sec_data["lessons"]):
                    lesson = CourseLesson(
                        id=uuid.uuid4(), section_id=section.id,
                        title=l_data["title"], position=i,
                        content_type="interactive",
                        content_markdown=l_data["v2"],
                        xp_reward=l_data["xp"], steps=None,
                    )
                    db.add(lesson)
                    await db.flush()
                    x = SNAKE_X[global_idx % len(SNAKE_X)] * CANVAS_W
                    y = V_PAD + global_idx * ROW_H
                    all_positions.append({"id": str(lesson.id), "x": x, "y": y})
                    global_idx += 1

            edges = [
                {"id": f"e-{i}", "source": all_positions[i-1]["id"], "target": all_positions[i]["id"]}
                for i in range(1, len(all_positions))
            ]
            course.roadmap_nodes = all_positions
            course.roadmap_edges = edges
            await db.commit()
            print(f"  OK: '{c_data['title']}' — {global_idx} lessons")

    print("Done!")

if __name__ == "__main__":
    asyncio.run(seed())
