"""Create all tables if they don't exist."""
import asyncio
from app.database import engine, Base
from app.models import *  # noqa
from app.models.course import *  # noqa
from app.models.payment import *  # noqa

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created/verified")

if __name__ == "__main__":
    asyncio.run(main())
