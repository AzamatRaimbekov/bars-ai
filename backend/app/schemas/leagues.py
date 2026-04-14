import uuid

from pydantic import BaseModel


LEAGUE_THRESHOLDS = {
    "bronze": 0,
    "silver": 500,
    "gold": 2000,
    "platinum": 5000,
    "diamond": 10000,
}

LEAGUE_ORDER = ["bronze", "silver", "gold", "platinum", "diamond"]


class LeagueInfo(BaseModel):
    league: str  # bronze, silver, gold, platinum, diamond
    xp_this_week: int
    next_league: str | None
    xp_to_next: int
    rank_in_league: int


class LeagueMember(BaseModel):
    user_id: uuid.UUID
    name: str
    avatar_url: str | None
    xp_this_week: int
    rank: int
