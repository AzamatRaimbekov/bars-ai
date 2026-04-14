"""
Updates the Frontend Development course lessons with V2 content IDs
stored in content_markdown field for frontend mapping.

Usage: cd backend && PYTHONPATH=. python -m app.seed_update_v2ids
"""
import asyncio
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database import async_session
from app.models.course import Course, CourseSection, CourseLesson

# Map lesson titles (Russian) to V2 lesson IDs
TITLE_TO_V2 = {
    "Структура документа": "fe-1-1",
    "Основные теги": "fe-1-2",
    "Элементы форм": "fe-2-1",
    "Таблицы": "fe-2-2",
    "Семантические элементы": "fe-3-1",
    "ARIA и доступность": "fe-4-1",
    "Селекторы и блочная модель": "fe-5-1",
    "Цвета и типографика": "fe-5-2",
    "Компоновка Flexbox": "fe-6-1",
    "Компоновка Grid": "fe-7-1",
    "Медиа-запросы": "fe-8-1",
    "Mobile-First подход": "fe-8-2",
    "Анимации и переходы": "fe-9-1",
    "Переменные и типы": "fe-10-1",
    "Управление потоком": "fe-10-2",
    "Функции и замыкания": "fe-11-1",
    "Методы массивов": "fe-12-1",
    "Паттерны объектов": "fe-12-2",
    "DOM API": "fe-13-1",
    "Промисы и Async/Await": "fe-14-1",
    "Fetch API": "fe-14-2",
    "Современные возможности JS": "fe-15-1",
    "JSX и компоненты": "fe-16-1",
    "Props и рендеринг": "fe-16-2",
    "useState и события": "fe-17-1",
    "useEffect": "fe-18-1",
    "Пользовательские хуки": "fe-18-2",
    "Маршрутизация": "fe-19-1",
    "Управление состоянием": "fe-20-1",
    "Основы TypeScript": "fe-21-1",
    "Тестирование React приложений": "fe-22-1",
    "Рабочий процесс Git": "fe-23-1",
    "Оптимизация производительности": "fe-24-1",
    "Сборка и деплой": "fe-25-1",
}


async def update():
    async with async_session() as db:
        result = await db.execute(
            select(Course)
            .options(selectinload(Course.sections).selectinload(CourseSection.lessons))
            .where(Course.title == "Frontend Development")
        )
        course = result.scalar_one_or_none()
        if not course:
            print("Course not found")
            return

        updated = 0
        for section in course.sections:
            for lesson in section.lessons:
                v2_id = TITLE_TO_V2.get(lesson.title)
                if v2_id:
                    lesson.content_markdown = v2_id
                    updated += 1

        await db.commit()
        print(f"Updated {updated} lessons with V2 IDs")


if __name__ == "__main__":
    asyncio.run(update())
