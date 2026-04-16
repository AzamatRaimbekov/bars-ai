import uuid
from datetime import date, datetime

from sqlalchemy import Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Progress(Base):
    __tablename__ = "progress"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    xp: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[str] = mapped_column(String(20), default="Novice")
    streak: Mapped[int] = mapped_column(Integer, default=0)
    longest_streak: Mapped[int] = mapped_column(Integer, default=0)
    last_active_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    completed_nodes: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    completed_lessons: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    league: Mapped[str] = mapped_column(String(20), default="bronze")
    xp_this_week: Mapped[int] = mapped_column(Integer, default=0)
    xp_this_month: Mapped[int] = mapped_column(Integer, default=0)
    week_reset_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    month_reset_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user: Mapped["User"] = relationship(back_populates="progress")
