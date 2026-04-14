"""
Seed script: creates the Frontend Development course in the database
from the existing roadmap data.

Usage: cd backend && PYTHONPATH=. python -m app.seed_frontend_course
"""
import asyncio
import uuid
from sqlalchemy import select
from app.database import async_session
from app.models.course import Course, CourseSection, CourseLesson
from app.models.user import User

COURSE_TITLE = "Frontend Development"
COURSE_DESCRIPTION = (
    "Полный курс по Frontend-разработке: от HTML/CSS до React, TypeScript и деплоя. "
    "Включает интерактивные уроки, квизы и практические задания. "
    "Подходит для начинающих и тех, кто хочет систематизировать знания."
)

SECTIONS = [
    {
        "title": "Junior · HTML",
        "position": 0,
        "lessons": [
            {"title": "Структура документа", "xp": 15, "pos": 0},
            {"title": "Основные теги", "xp": 15, "pos": 1},
            {"title": "Элементы форм", "xp": 15, "pos": 2},
            {"title": "Таблицы", "xp": 10, "pos": 3},
            {"title": "Семантические элементы", "xp": 20, "pos": 4},
            {"title": "ARIA и доступность", "xp": 25, "pos": 5},
        ],
    },
    {
        "title": "Junior · CSS",
        "position": 1,
        "lessons": [
            {"title": "Селекторы и блочная модель", "xp": 20, "pos": 0},
            {"title": "Цвета и типографика", "xp": 15, "pos": 1},
            {"title": "Компоновка Flexbox", "xp": 30, "pos": 2},
            {"title": "Компоновка Grid", "xp": 30, "pos": 3},
            {"title": "Медиа-запросы", "xp": 15, "pos": 4},
            {"title": "Mobile-First подход", "xp": 15, "pos": 5},
            {"title": "Анимации и переходы", "xp": 25, "pos": 6},
        ],
    },
    {
        "title": "Middle · JavaScript",
        "position": 2,
        "lessons": [
            {"title": "Переменные и типы", "xp": 20, "pos": 0},
            {"title": "Управление потоком", "xp": 20, "pos": 1},
            {"title": "Функции и замыкания", "xp": 35, "pos": 2},
            {"title": "Методы массивов", "xp": 20, "pos": 3},
            {"title": "Паттерны объектов", "xp": 15, "pos": 4},
            {"title": "DOM API", "xp": 30, "pos": 5},
            {"title": "Промисы и Async/Await", "xp": 20, "pos": 6},
            {"title": "Fetch API", "xp": 20, "pos": 7},
            {"title": "Современные возможности JS", "xp": 30, "pos": 8},
        ],
    },
    {
        "title": "Middle · React",
        "position": 3,
        "lessons": [
            {"title": "JSX и компоненты", "xp": 20, "pos": 0},
            {"title": "Props и рендеринг", "xp": 20, "pos": 1},
            {"title": "useState и события", "xp": 35, "pos": 2},
            {"title": "useEffect", "xp": 20, "pos": 3},
            {"title": "Пользовательские хуки", "xp": 20, "pos": 4},
            {"title": "Маршрутизация", "xp": 25, "pos": 5},
            {"title": "Управление состоянием", "xp": 35, "pos": 6},
        ],
    },
    {
        "title": "Senior · Про навыки",
        "position": 4,
        "lessons": [
            {"title": "Основы TypeScript", "xp": 40, "pos": 0},
            {"title": "Тестирование React приложений", "xp": 35, "pos": 1},
            {"title": "Рабочий процесс Git", "xp": 30, "pos": 2},
            {"title": "Оптимизация производительности", "xp": 30, "pos": 3},
            {"title": "Сборка и деплой", "xp": 25, "pos": 4},
        ],
    },
]


async def seed():
    async with async_session() as db:
        # Find first user to be the author
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        if not user:
            print("No users in DB. Create a user first.")
            return

        # Check if course already exists
        existing = await db.execute(
            select(Course).where(Course.title == COURSE_TITLE)
        )
        if existing.scalar_one_or_none():
            print(f"Course '{COURSE_TITLE}' already exists. Skipping.")
            return

        # Create course
        course = Course(
            id=uuid.uuid4(),
            title=COURSE_TITLE,
            slug="frontend-development-" + uuid.uuid4().hex[:6],
            description=COURSE_DESCRIPTION,
            author_id=user.id,
            category="Frontend",
            difficulty="Beginner",
            price=0,
            currency="USD",
            status="published",
        )
        db.add(course)
        await db.flush()

        # Create sections and lessons
        all_positions = []
        snake_x = [0.50, 0.75, 0.50, 0.25, 0.50]
        canvas_w = 500
        row_h = 148
        v_pad = 90
        global_idx = 0

        for sec_data in SECTIONS:
            section = CourseSection(
                id=uuid.uuid4(),
                course_id=course.id,
                title=sec_data["title"],
                position=sec_data["position"],
            )
            db.add(section)
            await db.flush()

            for lesson_data in sec_data["lessons"]:
                lesson = CourseLesson(
                    id=uuid.uuid4(),
                    section_id=section.id,
                    title=lesson_data["title"],
                    position=lesson_data["pos"],
                    content_type="interactive",
                    content_markdown="",
                    xp_reward=lesson_data["xp"],
                    steps=None,
                )
                db.add(lesson)
                await db.flush()

                # Compute snake position
                x = snake_x[global_idx % len(snake_x)] * canvas_w
                y = v_pad + global_idx * row_h
                all_positions.append({
                    "id": str(lesson.id),
                    "x": x,
                    "y": y,
                })
                global_idx += 1

        # Build sequential edges
        edges = []
        for i in range(1, len(all_positions)):
            edges.append({
                "id": f"edge-{i}",
                "source": all_positions[i - 1]["id"],
                "target": all_positions[i]["id"],
            })

        course.roadmap_nodes = all_positions
        course.roadmap_edges = edges

        await db.commit()
        print(f"Created course '{COURSE_TITLE}' with {global_idx} lessons, id={course.id}")
        print(f"Author: {user.name} ({user.email})")


if __name__ == "__main__":
    asyncio.run(seed())
