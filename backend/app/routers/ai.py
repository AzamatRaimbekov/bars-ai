import uuid

from fastapi import APIRouter, Depends, Request, UploadFile, File, Form
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
    GenerateCourseRequest, GenerateCourseResponse,
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


@router.post("/generate-course", response_model=GenerateCourseResponse)
async def generate_course(
    topic: str = Form(...),
    language: str = Form("ru"),
    difficulty: str = Form("intermediate"),
    sections_count: int = Form(5),
    prompt: str = Form(""),
    files: list[UploadFile] = File(default=[]),
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    from fastapi import HTTPException
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user or user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    # Extract text from uploaded files
    file_texts = []
    for f in files:
        content = await f.read()
        text = _extract_file_text(content, f.filename or "")
        if text:
            file_texts.append(f"--- {f.filename} ---\n{text[:15000]}")

    file_context = "\n\n".join(file_texts) if file_texts else None

    try:
        return await ai_service.generate_course(
            db, user_id, topic, language, sections_count, difficulty,
            custom_prompt=prompt or None,
            file_context=file_context,
        )
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(f"GENERATE-COURSE ERROR: {type(e).__name__}: {e}\n{tb}")
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")


def _extract_file_text(content: bytes, filename: str) -> str:
    """Extract text from PDF, DOCX, XLSX, or plain text files."""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

    if ext == "pdf":
        try:
            import io
            import PyPDF2
            reader = PyPDF2.PdfReader(io.BytesIO(content))
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception:
            return ""

    if ext in ("docx", "doc"):
        try:
            import io
            import zipfile
            import xml.etree.ElementTree as ET
            with zipfile.ZipFile(io.BytesIO(content)) as z:
                xml_content = z.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            return "\n".join(node.text for node in tree.iter(f"{{{ns['w']}}}t") if node.text)
        except Exception:
            return ""

    if ext in ("xlsx", "xls"):
        try:
            import io
            import zipfile
            import xml.etree.ElementTree as ET
            with zipfile.ZipFile(io.BytesIO(content)) as z:
                # Read shared strings
                shared = []
                if "xl/sharedStrings.xml" in z.namelist():
                    tree = ET.fromstring(z.read("xl/sharedStrings.xml"))
                    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
                    for si in tree.findall(f"{{{ns}}}si"):
                        t = si.find(f".//{{{ns}}}t")
                        shared.append(t.text if t is not None and t.text else "")
                return "\n".join(shared)
        except Exception:
            return ""

    if ext in ("txt", "md", "csv"):
        try:
            return content.decode("utf-8", errors="ignore")
        except Exception:
            return ""

    return ""
