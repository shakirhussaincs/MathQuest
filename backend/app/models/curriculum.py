import enum
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class DifficultyLevel(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    BOSS = "boss"

class MissionCategory(str, enum.Enum):
    CONCEPT_EXPLORATION = "concept_exploration"
    PRACTICE = "practice"
    BOSS_CHALLENGE = "boss_challenge"
    REVISION = "revision"

class MissionStatus(str, enum.Enum):
    LOCKED = "locked"
    AVAILABLE = "available"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    grade = Column(Integer, nullable=False, index=True)
    icon = Column(String(50), default="compass", nullable=False)
    theme_color = Column(String(30), default="emerald", nullable=False)
    unlock_condition = Column(String(100), default="grade_match", nullable=False)
    display_order = Column(Integer, default=1, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    topics = relationship("Topic", back_populates="world", cascade="all, delete-orphan", order_by="Topic.display_order")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    learning_objectives = Column(JSON, nullable=True)
    grade = Column(Integer, nullable=False)
    display_order = Column(Integer, default=1, nullable=False)

    world = relationship("World", back_populates="topics")
    missions = relationship("Mission", back_populates="topic", cascade="all, delete-orphan", order_by="Mission.display_order")

class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(150), nullable=False)
    instructions = Column(Text, nullable=False)
    category = Column(String(50), default=MissionCategory.PRACTICE.value, nullable=False)
    difficulty = Column(String(20), default=DifficultyLevel.EASY.value, nullable=False)
    question_count = Column(Integer, default=5, nullable=False)
    xp_reward = Column(Integer, default=20, nullable=False)
    pass_percentage = Column(Integer, default=60, nullable=False)
    unlock_condition = Column(String(150), default="always", nullable=False)
    display_order = Column(Integer, default=1, nullable=False)
    is_boss = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    topic = relationship("Topic", back_populates="missions")
    questions = relationship("Question", back_populates="mission", cascade="all, delete-orphan", order_by="Question.display_order")
    progress_records = relationship("MissionProgress", back_populates="mission", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id", ondelete="CASCADE"), nullable=False, index=True)
    prompt = Column(Text, nullable=False)
    question_type = Column(String(30), default="multiple_choice", nullable=False)  # "multiple_choice" or "numeric"
    options = Column(JSON, nullable=True)
    correct_answer = Column(String(100), nullable=False)
    explanation = Column(Text, nullable=False)
    step_by_step_solution = Column(JSON, nullable=True)  # List of ordered steps
    common_mistakes = Column(JSON, nullable=True)  # Diagnostic mapping of wrong answers to mistake explanations
    difficulty = Column(String(20), default=DifficultyLevel.EASY.value, nullable=False)
    tolerance = Column(Float, nullable=True, default=0.01)
    display_order = Column(Integer, default=1, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    mission = relationship("Mission", back_populates="questions")
    attempts = relationship("Attempt", back_populates="question", cascade="all, delete-orphan")

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    submitted_answer = Column(String(200), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    attempted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    question = relationship("Question", back_populates="attempts")

class MissionProgress(Base):
    __tablename__ = "mission_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id", ondelete="CASCADE"), nullable=False, index=True)
    status = Column(String(20), default=MissionStatus.AVAILABLE.value, nullable=False)
    score = Column(Integer, default=0, nullable=False)
    accuracy = Column(Float, default=0.0, nullable=False)
    attempts_count = Column(Integer, default=0, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    mission = relationship("Mission", back_populates="progress_records")
