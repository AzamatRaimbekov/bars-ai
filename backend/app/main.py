import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.redis import redis_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_pool.aclose()


app = FastAPI(title="Bars AI API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health():
    return {"status": "ok"}


from app.routers import auth, users, progress, ai, quests, leaderboard, leagues, courses, mentor, sprint, admin, payments, notifications

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(progress.router)
app.include_router(ai.router)
app.include_router(quests.router)
app.include_router(leaderboard.router)
app.include_router(leagues.router)
app.include_router(courses.router)
app.include_router(mentor.router)
app.include_router(sprint.router)
app.include_router(admin.router)
app.include_router(payments.router)
app.include_router(notifications.router)

# Serve frontend static files in production
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
if STATIC_DIR.is_dir():
    app.mount("/assets", StaticFiles(directory=str(STATIC_DIR / "assets")), name="assets")
    app.mount("/images", StaticFiles(directory=str(STATIC_DIR / "images")), name="images")

    @app.get("/{full_path:path}")
    async def serve_spa(request: Request, full_path: str):
        # Don't catch /api routes
        if full_path.startswith("api"):
            return {"detail": "Not found"}
        file_path = STATIC_DIR / full_path
        if file_path.is_file():
            return FileResponse(str(file_path))
        return FileResponse(str(STATIC_DIR / "index.html"))
