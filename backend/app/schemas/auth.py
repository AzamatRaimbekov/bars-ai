from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    name: str = Field(min_length=1, max_length=100)
    direction: str = Field(default="", max_length=20)
    assessment_level: str = Field(default="beginner", pattern=r"^(beginner|intermediate|advanced)$")
    language: str = Field(default="ru", pattern=r"^(ru|en)$")


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
