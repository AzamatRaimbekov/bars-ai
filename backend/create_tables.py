"""Create all tables if they don't exist."""
import asyncio
from app.database import engine, Base
from app.models import *  # noqa
from app.models.course import *  # noqa
from app.models.payment import *  # noqa
from app.models.notification import *  # noqa

async def main():
    from sqlalchemy import text
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # Add missing columns to existing tables
        migrations = [
            "ALTER TABLE users ADD COLUMN IF NOT EXISTS interests JSON DEFAULT '[]'",
            "ALTER TABLE users ADD COLUMN IF NOT EXISTS onboarding_complete BOOLEAN DEFAULT FALSE",
            "ALTER TABLE users ADD COLUMN IF NOT EXISTS assessment_context TEXT",
            "ALTER TABLE courses ADD COLUMN IF NOT EXISTS tags JSON",
        ]
        for sql in migrations:
            try:
                await conn.execute(text(sql))
            except Exception as e:
                print(f"  Migration skipped: {e}")
    print("Tables created/verified")

if __name__ == "__main__":
    asyncio.run(main())
