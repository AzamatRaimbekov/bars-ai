from pydantic import BaseModel


class DailyQuest(BaseModel):
    id: str
    title: dict[str, str]
    description: dict[str, str]
    xp_reward: int
    target: int
    progress: int
    completed: bool


class DailyQuestsResponse(BaseModel):
    quests: list[DailyQuest]
    date: str
