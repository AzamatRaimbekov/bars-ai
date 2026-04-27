"""Create all tables if they don't exist."""
import asyncio
from app.database import engine, Base
from app.models import *  # noqa
from app.models.course import *  # noqa
from app.models.payment import *  # noqa
from app.models.notification import *  # noqa

CATEGORY_TAGS = {
    "Frontend": ["Frontend", "Web", "JavaScript", "Programming"],
    "Programming": ["Programming", "Python", "Backend"],
    "English": ["English", "Languages"],
    "Languages": ["Languages"],
    "Data Science": ["Data Science", "Python", "Analytics"],
    "AI": ["AI", "ChatGPT", "Productivity"],
    "AI-Assisted Development": ["AI", "Programming", "Productivity"],
    "Design": ["Design", "UI/UX", "Creative"],
    "DevOps": ["DevOps", "Backend", "Infrastructure"],
    "Database": ["Database", "SQL", "Backend"],
    "Mobile": ["Mobile", "React Native", "Programming"],
    "Security": ["Security", "Cybersecurity"],
    "QA": ["QA", "Testing", "Programming"],
    "Go": ["Go", "Backend", "Programming"],
    "SysAdmin": ["Linux", "SysAdmin", "Infrastructure"],
    "Product": ["Product Management", "Business"],
    "Finance": ["Finance", "Business"],
    "Business": ["Business", "Startup"],
    "Soft Skills": ["Soft Skills", "Career"],
    "Dance": ["Dance", "Creative"],
    "Music": ["Music", "DJ", "Creative"],
    "Photography": ["Photography", "Creative"],
    "3D": ["3D", "Blender", "Creative"],
    "Video": ["Video Editing", "Creative"],
    "Marketing": ["Marketing", "Copywriting", "Business"],
    "Ads": ["Ads", "Marketing", "Business"],
    "Sales": ["Sales", "Business"],
    "E-commerce": ["E-commerce", "Marketplace", "Business"],
    "Call Center": ["Call Center", "Sales", "Career"],
    "No-Code": ["No-Code", "Web", "Productivity"],
    "Productivity": ["Productivity", "Excel"],
    "Vibe Coding": ["AI", "Programming", "Vibe Coding"],
    "management": ["Management", "Business"],
    "Other": ["Programming", "Tools"],
}

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

        # Backfill tags for courses that have none
        for category, tags in CATEGORY_TAGS.items():
            import json
            tags_json = json.dumps(tags)
            await conn.execute(
                text("UPDATE courses SET tags = :tags WHERE category = :cat AND (tags IS NULL OR tags::text = 'null' OR tags::text = '[]' OR json_array_length(tags) = 0)"),
                {"tags": tags_json, "cat": category},
            )
        print("Tables created/verified, tags backfilled")

if __name__ == "__main__":
    asyncio.run(main())
