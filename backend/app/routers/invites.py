import os
import uuid

from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user, CurrentUser
from app.permissions import require_permission
from app.schemas.invite import CreateInviteRequest, InviteResponse, AcceptInviteRequest
from app.schemas.auth import TokenResponse
from app.services import invite_service

router = APIRouter(prefix="/api/invites", tags=["invites"])

COOKIE_KEY = "refresh_token"
COOKIE_MAX_AGE = 7 * 24 * 60 * 60


def _set_refresh_cookie(response: Response, raw_token: str):
    response.set_cookie(
        key=COOKIE_KEY,
        value=raw_token,
        httponly=True,
        secure=os.getenv("ENV", "dev") != "dev",
        samesite="lax",
        max_age=COOKIE_MAX_AGE,
        path="/",
    )


@router.post("/", response_model=InviteResponse)
async def create_invite(
    body: CreateInviteRequest,
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await invite_service.create_invite(
        db, user.org_id, user.id, body.department_id, body.role_id, body.max_uses, body.expires_in_days,
    )


@router.get("/", response_model=list[InviteResponse])
async def list_invites(
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await invite_service.list_invites(db, user.org_id)


@router.delete("/{invite_id}", status_code=204)
async def deactivate_invite(
    invite_id: uuid.UUID,
    user_id=Depends(require_permission("users.invite")),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await invite_service.deactivate_invite(db, user.org_id, invite_id)


@router.post("/join/{code}", response_model=TokenResponse)
async def accept_invite(
    code: str,
    body: AcceptInviteRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    user, access_token, raw_refresh = await invite_service.accept_invite(
        db, code, body.email, body.password, body.name,
    )
    _set_refresh_cookie(response, raw_refresh)
    return TokenResponse(access_token=access_token)
