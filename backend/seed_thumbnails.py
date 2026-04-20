"""Set thumbnail_url for all courses that don't have one."""
import asyncio
from sqlalchemy import select, update
from app.database import async_session
from app.models.course import Course

# Mapping: course title substring → Unsplash photo URL (free, no API key needed)
THUMBNAILS = {
    "Frontend": "https://images.unsplash.com/photo-1621839673705-6617adf9e890?w=800&q=80",
    "Python": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=800&q=80",
    "Claude Code Mastery": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80",
    "Claude Code Advanced": "https://images.unsplash.com/photo-1629654297299-c8506221ca97?w=800&q=80",
    "Claude Code — Полный": "https://images.unsplash.com/photo-1587620962725-abab7fe55159?w=800&q=80",
    "Нейросети": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80",
    "ChatGPT": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&q=80",
    "Data Science": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",
    "DevOps": "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=800&q=80",
    "React Native": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=80",
    "Senior Frontend": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "Golang": "https://images.unsplash.com/photo-1515879218367-8466d910auj7?w=800&q=80",
    "SQL": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=800&q=80",
    "QA": "https://images.unsplash.com/photo-1516382799247-87df95d790b7?w=800&q=80",
    "Кибербезопасность": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80",
    "Linux": "https://images.unsplash.com/photo-1629654297299-c8506221ca97?w=800&q=80",
    "No-Code": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
    "Excel": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=800&q=80",
    "Vibe Coding": "https://images.unsplash.com/photo-1550439062-609e1531270e?w=800&q=80",
    "Blender": "https://images.unsplash.com/photo-1617802690992-15d93263d3a9?w=800&q=80",
    "UI/UX": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800&q=80",
    "Графический дизайн": "https://images.unsplash.com/photo-1626785774573-4b799315345d?w=800&q=80",
    "Видеомонтаж": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=800&q=80",
    "Фотография": "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=800&q=80",
    "Копирайтинг": "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&q=80",
    "SMM": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=800&q=80",
    "Таргетированная": "https://images.unsplash.com/photo-1533750349088-cd871a92f312?w=800&q=80",
    "Маркетплейс": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80",
    "Product Management": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&q=80",
    "Предпринимательство": "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800&q=80",
    "Продажи": "https://images.unsplash.com/photo-1556745757-8d76bdb6984b?w=800&q=80",
    "Soft Skills": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    "Финансовая": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&q=80",
    "CIB": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80",
    "Call Center": "https://images.unsplash.com/photo-1534536281715-e28d76689b4d?w=800&q=80",
    "Диджеинг": "https://images.unsplash.com/photo-1571266028243-3716f02d2d4c?w=800&q=80",
    "Popping": "https://images.unsplash.com/photo-1547153760-18fc86324498?w=800&q=80",
    "English": "https://images.unsplash.com/photo-1543109740-4bdb38fda756?w=800&q=80",
    "Испанский": "https://images.unsplash.com/photo-1489945052260-4f21c52571bc?w=800&q=80",
    "Французский": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
    "Китайский": "https://images.unsplash.com/photo-1547981609-4b6bfe67ca0b?w=800&q=80",
    "Корейский": "https://images.unsplash.com/photo-1517154421773-0529f29ea451?w=800&q=80",
    "Кыргыз": "https://images.unsplash.com/photo-1596402184320-417e7178b2cd?w=800&q=80",
    "Қазақ": "https://images.unsplash.com/photo-1565967511849-76a60a516170?w=800&q=80",
    "Турецкий": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800&q=80",
}

# Fallback for unmatched courses
DEFAULT_THUMBNAIL = "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&q=80"


async def main():
    async with async_session() as db:
        result = await db.execute(select(Course))
        courses = result.scalars().all()
        updated = 0

        for course in courses:
            if course.thumbnail_url:
                continue

            thumb = DEFAULT_THUMBNAIL
            for key, url in THUMBNAILS.items():
                if key.lower() in course.title.lower():
                    thumb = url
                    break

            course.thumbnail_url = thumb
            updated += 1
            print(f"  SET {course.title[:50]} → {thumb[:60]}...")

        await db.commit()
        print(f"\nThumbnails: {updated} updated, {len(courses) - updated} already had one")


if __name__ == "__main__":
    asyncio.run(main())
