import hashlib
import uuid
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(user_id: str, org_id: str | None = None, is_superadmin: bool = False) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_EXPIRE_MINUTES)
    payload = {
        "sub": user_id,
        "exp": expire,
        "type": "access",
    }
    if org_id:
        payload["org_id"] = org_id
    if is_superadmin:
        payload["is_superadmin"] = True
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)


def create_refresh_token() -> tuple[str, str]:
    """Returns (raw_token, token_hash) — store hash in DB, send raw to client."""
    raw = uuid.uuid4().hex + uuid.uuid4().hex
    token_hash = hashlib.sha256(raw.encode()).hexdigest()
    return raw, token_hash


def hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def decode_access_token(token: str) -> dict | None:
    """Returns payload dict with sub, org_id, is_superadmin or None if invalid."""
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            return None
        return {
            "sub": payload.get("sub"),
            "org_id": payload.get("org_id"),
            "is_superadmin": payload.get("is_superadmin", False),
        }
    except JWTError:
        return None
