import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.schemas.user import UserWithProgressResponse, UserUpdateRequest, PublicUserResponse, ChangePasswordRequest
from app.services import user_service

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/me", response_model=UserWithProgressResponse)
async def get_me(user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await user_service.get_me(db, user_id)


@router.patch("/me", response_model=UserWithProgressResponse)
async def update_me(body: UserUpdateRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await user_service.update_me(db, user_id, body.model_dump(exclude_none=True))


@router.post("/me/password", status_code=204)
async def change_password(body: ChangePasswordRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    await user_service.change_password(db, user_id, body.current_password, body.new_password)


@router.get("/{target_id}", response_model=PublicUserResponse)
async def get_user(target_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await user_service.get_public_profile(db, target_id)
