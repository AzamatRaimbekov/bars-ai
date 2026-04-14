"""
Run this script to create the course marketplace tables.

Usage:
    cd backend && python -m app.migrate_courses
"""

import asyncio

from app.database import engine, Base

# Import all models so they are registered with Base.metadata
from app.models import (  # noqa: F401
    User, Progress, UserBadge, RefreshToken,
    Course, CourseSection, CourseLesson,
    CourseEnrollment, CourseLessonProgress, CourseReview,
)


async def migrate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Course marketplace tables created successfully.")


if __name__ == "__main__":
    asyncio.run(migrate())
