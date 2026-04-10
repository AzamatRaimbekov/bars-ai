from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(pattern=r"^(user|assistant)$")
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1)
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")


class ChatResponse(BaseModel):
    content: str


class AssessRequest(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    answers: list[str] = Field(min_length=1, max_length=10)


class AssessResponse(BaseModel):
    level: str


class TipRequest(BaseModel):
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")
    level: str


class TipResponse(BaseModel):
    tip: str


class ScoreRequest(BaseModel):
    question: str = Field(min_length=1)
    answer: str = Field(min_length=1)
    direction: str = Field(pattern=r"^(frontend|english|callcenter|cib)$")


class ScoreResponse(BaseModel):
    score: int
    feedback: str
    model_answer: str


class TranscribeResponse(BaseModel):
    text: str
    confidence: float


class CheckTranslationRequest(BaseModel):
    sentence: str = Field(min_length=1)
    user_answer: str = Field(min_length=1)
    source_language: str = Field(min_length=2, max_length=5)
    target_language: str = Field(min_length=2, max_length=5)


class CheckTranslationResponse(BaseModel):
    correct: bool
    feedback: str
    suggested: str
