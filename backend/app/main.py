from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.redis import redis_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_pool.aclose()


app = FastAPI(title="PathMind API", version="1.0.0", lifespan=lifespan)

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


from app.routers import auth, users, progress

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(progress.router)
