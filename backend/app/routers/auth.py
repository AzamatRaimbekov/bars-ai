from fastapi import APIRouter, Depends, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])

COOKIE_KEY = "refresh_token"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60


def _set_refresh_cookie(response: Response, raw_token: str):
    response.set_cookie(
        key=COOKIE_KEY,
        value=raw_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=COOKIE_MAX_AGE,
        path="/api/auth",
    )


@router.post("/register", response_model=TokenResponse)
async def register(body: RegisterRequest, response: Response, db: AsyncSession = Depends(get_db)):
    user, access_token, raw_refresh = await auth_service.register(
        db, body.email, body.password, body.name, body.direction, body.assessment_level, body.language,
    )
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, response: Response, db: AsyncSession = Depends(get_db)):
    user, access_token, raw_refresh = await auth_service.login(db, body.email, body.password)
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(response: Response, refresh_token: str | None = Cookie(None, alias=COOKIE_KEY), db: AsyncSession = Depends(get_db)):
    if not refresh_token:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="No refresh token")
    access_token, new_raw = await auth_service.refresh(db, refresh_token)
    _set_refresh_cookie(response, new_raw)
    return TokenResponse(access_token=access_token)


@router.post("/logout", status_code=204)
async def logout(response: Response, refresh_token: str | None = Cookie(None, alias=COOKIE_KEY), db: AsyncSession = Depends(get_db)):
    if refresh_token:
        await auth_service.logout(db, refresh_token)
    response.delete_cookie(COOKIE_KEY, path="/api/auth")
