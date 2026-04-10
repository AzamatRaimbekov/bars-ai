import uuid

from fastapi import APIRouter, Depends, Request, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dependencies import get_db, get_current_user_id
from app.schemas.ai import (
    ChatRequest, ChatResponse,
    AssessRequest, AssessResponse,
    TipRequest, TipResponse,
    ScoreRequest, ScoreResponse,
    TranscribeResponse,
    CheckTranslationRequest, CheckTranslationResponse,
)
from app.services import ai_service
from app.utils.rate_limiter import rate_limit
from app.models.user import User

router = APIRouter(prefix="/api/ai", tags=["ai"])


async def _get_user_language(db: AsyncSession, user_id: uuid.UUID) -> str:
    result = await db.execute(select(User.language).where(User.id == user_id))
    return result.scalar_one_or_none() or "ru"


@router.post("/chat", response_model=ChatResponse)
async def chat(body: ChatRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    language = await _get_user_language(db, user_id)
    messages = [{"role": m.role, "content": m.content} for m in body.messages]
    content = await ai_service.chat(messages, body.direction, language)
    return ChatResponse(content=content)


@router.post("/assess", response_model=AssessResponse)
async def assess(body: AssessRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    level = await ai_service.assess(body.direction, body.answers)
    return AssessResponse(level=level)


@router.post("/tip", response_model=TipResponse)
async def tip_endpoint(body: TipRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await ai_service.tip(body.direction, body.level, str(user_id))
    return TipResponse(tip=result)


@router.post("/score", response_model=ScoreResponse)
async def score_answer(body: ScoreRequest, request: Request, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    language = await _get_user_language(db, user_id)
    result = await ai_service.score(body.question, body.answer, body.direction, language)
    return ScoreResponse(**result)


@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe(
    audio: UploadFile = File(...),
    request: Request = None,
    user_id: uuid.UUID = Depends(get_current_user_id),
):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    audio_bytes = await audio.read()
    result = await ai_service.transcribe(audio_bytes, audio.filename or "recording.webm")
    return TranscribeResponse(**result)


@router.post("/check-translation", response_model=CheckTranslationResponse)
async def check_translation(
    body: CheckTranslationRequest,
    request: Request,
    user_id: uuid.UUID = Depends(get_current_user_id),
):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await ai_service.check_translation(
        body.sentence, body.user_answer, body.source_language, body.target_language
    )
    return CheckTranslationResponse(**result)
