import uuid

from pydantic import BaseModel


class LeaderboardEntry(BaseModel):
    rank: int
    user_id: uuid.UUID
    name: str
    avatar_url: str | None
    xp: int
    level: str
    direction: str


class LeaderboardResponse(BaseModel):
    period: str
    entries: list[LeaderboardEntry]


class MyRankEntry(BaseModel):
    period: str
    rank: int | None
    total_users: int


class MyRankResponse(BaseModel):
    weekly: MyRankEntry
    monthly: MyRankEntry
    all_time: MyRankEntry
