"""Seed production DB with courses and a default admin user."""
import asyncio, uuid, os
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson
from app.utils.security import hash_password

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90

COURSES_DATA = [
    {
        "title": "Frontend Development",
        "description": "Полный курс по Frontend-разработке: от HTML/CSS до React, TypeScript и деплоя.",
        "category": "Frontend", "difficulty": "Beginner",
        "sections": [
            {"title": "Junior · HTML", "pos": 0, "lessons": [
                {"t": "Структура документа", "xp": 15, "v2": "fe-1-1"}, {"t": "Основные теги", "xp": 15, "v2": "fe-1-2"},
                {"t": "Элементы форм", "xp": 15, "v2": "fe-2-1"}, {"t": "Таблицы", "xp": 10, "v2": "fe-2-2"},
                {"t": "Семантические элементы", "xp": 20, "v2": "fe-3-1"}, {"t": "ARIA и доступность", "xp": 25, "v2": "fe-4-1"},
            ]},
            {"title": "Junior · CSS", "pos": 1, "lessons": [
                {"t": "Селекторы и блочная модель", "xp": 20, "v2": "fe-5-1"}, {"t": "Цвета и типографика", "xp": 15, "v2": "fe-5-2"},
                {"t": "Компоновка Flexbox", "xp": 30, "v2": "fe-6-1"}, {"t": "Компоновка Grid", "xp": 30, "v2": "fe-7-1"},
                {"t": "Медиа-запросы", "xp": 15, "v2": "fe-8-1"}, {"t": "Mobile-First подход", "xp": 15, "v2": "fe-8-2"},
                {"t": "Анимации и переходы", "xp": 25, "v2": "fe-9-1"},
            ]},
            {"title": "Middle · JavaScript", "pos": 2, "lessons": [
                {"t": "Переменные и типы", "xp": 20, "v2": "fe-10-1"}, {"t": "Управление потоком", "xp": 20, "v2": "fe-10-2"},
                {"t": "Функции и замыкания", "xp": 35, "v2": "fe-11-1"}, {"t": "Методы массивов", "xp": 20, "v2": "fe-12-1"},
                {"t": "Паттерны объектов", "xp": 15, "v2": "fe-12-2"}, {"t": "DOM API", "xp": 30, "v2": "fe-13-1"},
                {"t": "Промисы и Async/Await", "xp": 20, "v2": "fe-14-1"}, {"t": "Fetch API", "xp": 20, "v2": "fe-14-2"},
                {"t": "Современные возможности JS", "xp": 30, "v2": "fe-15-1"},
            ]},
            {"title": "Middle · React", "pos": 3, "lessons": [
                {"t": "JSX и компоненты", "xp": 20, "v2": "fe-16-1"}, {"t": "Props и рендеринг", "xp": 20, "v2": "fe-16-2"},
                {"t": "useState и события", "xp": 35, "v2": "fe-17-1"}, {"t": "useEffect", "xp": 20, "v2": "fe-18-1"},
                {"t": "Пользовательские хуки", "xp": 20, "v2": "fe-18-2"}, {"t": "Маршрутизация", "xp": 25, "v2": "fe-19-1"},
                {"t": "Управление состоянием", "xp": 35, "v2": "fe-20-1"},
            ]},
            {"title": "Senior · Про навыки", "pos": 4, "lessons": [
                {"t": "Основы TypeScript", "xp": 40, "v2": "fe-21-1"}, {"t": "Тестирование React", "xp": 35, "v2": "fe-22-1"},
                {"t": "Рабочий процесс Git", "xp": 30, "v2": "fe-23-1"}, {"t": "Оптимизация", "xp": 30, "v2": "fe-24-1"},
                {"t": "Сборка и деплой", "xp": 25, "v2": "fe-25-1"},
            ]},
        ],
    },
    {
        "title": "CIB — Корпоративный и инвестиционный банкинг",
        "description": "Полный курс по CIB: финансовые рынки, банковские операции, M&A, анализ и интервью.",
        "category": "CIB", "difficulty": "Intermediate",
        "sections": [
            {"title": "Основы финансов", "pos": 0, "lessons": [
                {"t": "Типы рынков", "xp": 20, "v2": "cib-1-1"}, {"t": "Ключевые участники", "xp": 15, "v2": "cib-1-2"},
                {"t": "Финансовая отчётность", "xp": 20, "v2": "cib-2-1"}, {"t": "Ключевые коэффициенты", "xp": 20, "v2": "cib-2-2"},
                {"t": "Концепции TVM", "xp": 30, "v2": "cib-3-1"}, {"t": "Облигации и доходность", "xp": 35, "v2": "cib-4-1"},
            ]},
            {"title": "Банковские операции", "pos": 1, "lessons": [
                {"t": "Основы банкинга", "xp": 30, "v2": "cib-5-1"}, {"t": "Корпоративные кредиты", "xp": 35, "v2": "cib-6-1"},
                {"t": "Торговое финансирование", "xp": 30, "v2": "cib-7-1"}, {"t": "Валюта и казначейство", "xp": 30, "v2": "cib-8-1"},
            ]},
            {"title": "Инвестиционный банкинг", "pos": 2, "lessons": [
                {"t": "Процесс M&A", "xp": 20, "v2": "cib-9-1"}, {"t": "Типы сделок", "xp": 20, "v2": "cib-9-2"},
                {"t": "Рынки акционерного капитала", "xp": 35, "v2": "cib-10-1"}, {"t": "Рынки долгового капитала", "xp": 35, "v2": "cib-11-1"},
                {"t": "Питч-буки", "xp": 30, "v2": "cib-12-1"},
            ]},
            {"title": "Финансовый анализ", "pos": 3, "lessons": [
                {"t": "Модель DCF", "xp": 25, "v2": "cib-13-1"}, {"t": "WACC и терминальная стоимость", "xp": 20, "v2": "cib-13-2"},
                {"t": "Сравнительный анализ", "xp": 35, "v2": "cib-14-1"}, {"t": "Основы LBO", "xp": 40, "v2": "cib-15-1"},
                {"t": "Навыки Excel", "xp": 35, "v2": "cib-16-1"},
            ]},
            {"title": "Подготовка к интервью", "pos": 4, "lessons": [
                {"t": "Поведенческие вопросы", "xp": 30, "v2": "cib-17-1"}, {"t": "Техническая подготовка", "xp": 40, "v2": "cib-18-1"},
                {"t": "Кейсы", "xp": 35, "v2": "cib-19-1"}, {"t": "Нетворкинг", "xp": 25, "v2": "cib-20-1"},
            ]},
        ],
    },
    {
        "title": "Call Center — Операторская работа",
        "description": "Курс для операторов: коммуникация, телефонный этикет, обслуживание клиентов, решение конфликтов.",
        "category": "Call Center", "difficulty": "Beginner",
        "sections": [
            {"title": "Основы коммуникации", "pos": 0, "lessons": [
                {"t": "Чёткая коммуникация", "xp": 25, "v2": "cc-1-1"}, {"t": "Навыки слушания", "xp": 25, "v2": "cc-2-1"},
                {"t": "Тон и эмпатия", "xp": 25, "v2": "cc-3-1"}, {"t": "Лексика обслуживания", "xp": 25, "v2": "cc-4-1"},
            ]},
            {"title": "Телефонный этикет", "pos": 1, "lessons": [
                {"t": "Скрипты приветствия", "xp": 20, "v2": "cc-5-1"}, {"t": "Удержание и перевод", "xp": 20, "v2": "cc-6-1"},
                {"t": "Скрипты завершения", "xp": 20, "v2": "cc-7-1"}, {"t": "Ведение записей", "xp": 20, "v2": "cc-8-1"},
            ]},
            {"title": "Обслуживание клиентов", "pos": 2, "lessons": [
                {"t": "Решение проблем", "xp": 30, "v2": "cc-9-1"}, {"t": "Обучение по продукту", "xp": 30, "v2": "cc-10-1"},
                {"t": "Техники продаж", "xp": 25, "v2": "cc-11-1"}, {"t": "Стратегии FCR", "xp": 25, "v2": "cc-12-1"},
            ]},
            {"title": "Решение конфликтов", "pos": 3, "lessons": [
                {"t": "Деэскалация", "xp": 30, "v2": "cc-13-1"}, {"t": "Обработка жалоб", "xp": 30, "v2": "cc-14-1"},
                {"t": "Позитивный отказ", "xp": 25, "v2": "cc-15-1"}, {"t": "Эскалация", "xp": 25, "v2": "cc-16-1"},
            ]},
            {"title": "Продвинутые навыки", "pos": 4, "lessons": [
                {"t": "Метрики эффективности", "xp": 30, "v2": "cc-17-1"}, {"t": "Управление стрессом", "xp": 25, "v2": "cc-18-1"},
                {"t": "Мультиканальность", "xp": 30, "v2": "cc-19-1"}, {"t": "Лидерство в команде", "xp": 30, "v2": "cc-20-1"},
            ]},
        ],
    },
    {
        "title": "SMM — Маркетинг в социальных сетях",
        "description": "Курс по SMM: стратегия, контент, таргет, аналитика и построение бренда.",
        "category": "Other", "difficulty": "Beginner",
        "sections": [
            {"title": "Основы SMM", "pos": 0, "lessons": [
                {"t": "Что такое SMM", "xp": 15, "v2": ""}, {"t": "Платформы и аудитория", "xp": 20, "v2": ""},
                {"t": "Построение стратегии", "xp": 25, "v2": ""}, {"t": "Целевая аудитория", "xp": 20, "v2": ""},
            ]},
            {"title": "Контент-маркетинг", "pos": 1, "lessons": [
                {"t": "Типы контента", "xp": 20, "v2": ""}, {"t": "Контент-план", "xp": 25, "v2": ""},
                {"t": "Визуальный контент", "xp": 30, "v2": ""}, {"t": "Копирайтинг", "xp": 25, "v2": ""},
                {"t": "Видео и Reels", "xp": 30, "v2": ""},
            ]},
            {"title": "Таргетированная реклама", "pos": 2, "lessons": [
                {"t": "Основы таргета", "xp": 25, "v2": ""}, {"t": "Facebook/Instagram Ads", "xp": 35, "v2": ""},
                {"t": "Аудитории и ретаргетинг", "xp": 30, "v2": ""}, {"t": "A/B тестирование", "xp": 25, "v2": ""},
                {"t": "Бюджетирование и ROI", "xp": 30, "v2": ""},
            ]},
            {"title": "Аналитика", "pos": 3, "lessons": [
                {"t": "KPI в SMM", "xp": 20, "v2": ""}, {"t": "Инструменты аналитики", "xp": 25, "v2": ""},
                {"t": "Отчётность", "xp": 20, "v2": ""}, {"t": "Оптимизация", "xp": 30, "v2": ""},
            ]},
            {"title": "Продвинутый SMM", "pos": 4, "lessons": [
                {"t": "Работа с блогерами", "xp": 30, "v2": ""}, {"t": "Комьюнити", "xp": 25, "v2": ""},
                {"t": "Кризисные коммуникации", "xp": 25, "v2": ""}, {"t": "Личный бренд", "xp": 30, "v2": ""},
                {"t": "Монетизация", "xp": 35, "v2": ""},
            ]},
        ],
    },
]


async def seed():
    async with async_session() as db:
        # Create admin user if none exist
        r = await db.execute(select(User).limit(1))
        user = r.scalar_one_or_none()
        if not user:
            user = User(id=uuid.uuid4(), email="admin@bars-ai.com", name="Bars AI Admin",
                        password=hash_password("BarsAI2026!Prod"), direction="frontend",
                        assessment_level="advanced", language="ru")
            db.add(user)
            await db.flush()
            print(f"Created admin user: admin@bars-ai.com")

        for c_data in COURSES_DATA:
            existing = await db.execute(select(Course).where(Course.title == c_data["title"]))
            if existing.scalar_one_or_none():
                print(f"  SKIP: {c_data['title']}")
                continue

            course = Course(id=uuid.uuid4(), title=c_data["title"],
                slug=c_data["title"].lower().replace(" ", "-")[:40] + "-" + uuid.uuid4().hex[:6],
                description=c_data["description"], author_id=user.id,
                category=c_data["category"], difficulty=c_data["difficulty"],
                price=0, currency="USD", status="published")
            db.add(course)
            await db.flush()

            positions, gidx = [], 0
            for sd in c_data["sections"]:
                sec = CourseSection(id=uuid.uuid4(), course_id=course.id, title=sd["title"], position=sd["pos"])
                db.add(sec)
                await db.flush()
                for i, ld in enumerate(sd["lessons"]):
                    les = CourseLesson(id=uuid.uuid4(), section_id=sec.id, title=ld["t"], position=i,
                        content_type="interactive", content_markdown=ld["v2"], xp_reward=ld["xp"], steps=None)
                    db.add(les)
                    await db.flush()
                    positions.append({"id": str(les.id), "x": SNAKE_X[gidx % 5] * CANVAS_W, "y": V_PAD + gidx * ROW_H})
                    gidx += 1

            edges = [{"id": f"e-{i}", "source": positions[i-1]["id"], "target": positions[i]["id"]} for i in range(1, len(positions))]
            course.roadmap_nodes = positions
            course.roadmap_edges = edges
            await db.commit()
            print(f"  OK: {c_data['title']} ({gidx} lessons)")

    print("Seed complete!")

if __name__ == "__main__":
    asyncio.run(seed())
