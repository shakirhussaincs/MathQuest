from datetime import datetime, date, timezone
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class RewardLedger(Base):
    """
    Immutable ledger of XP rewards to ensure strict idempotency (FR-33, NFR-03).
    A user cannot be awarded XP more than once for the same question attempt,
    mission completion, boss challenge, or daily streak.
    """
    __tablename__ = "reward_ledger"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = Column(String(50), nullable=False)  # "question_correct", "mission_completed", "boss_victory", "daily_streak"
    reference_id = Column(String(100), nullable=False)  # e.g. "q_10", "m_4", "boss_world_1", "streak_2026-11-08"
    xp_delta = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "event_type", "reference_id", name="uq_user_reward_event"),
    )

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=False)
    icon = Column(String(50), default="award", nullable=False)
    category = Column(String(50), default="general", nullable=False)
    criteria_description = Column(String(200), nullable=False)

    user_badges = relationship("UserBadge", back_populates="badge", cascade="all, delete-orphan")

class UserBadge(Base):
    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    badge_id = Column(Integer, ForeignKey("badges.id", ondelete="CASCADE"), nullable=False, index=True)
    awarded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    badge = relationship("Badge", back_populates="user_badges")

    __table_args__ = (
        UniqueConstraint("user_id", "badge_id", name="uq_user_badge"),
    )

class UserStreak(Base):
    """
    Tracks consecutive daily practice streaks (FR-34).
    """
    __tablename__ = "user_streaks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    current_streak = Column(Integer, default=0, nullable=False)
    longest_streak = Column(Integer, default=0, nullable=False)
    last_practice_date = Column(Date, nullable=True)
    total_days_practiced = Column(Integer, default=0, nullable=False)
