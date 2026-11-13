from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.gamification import RewardLedger
from app.services.auth_service import get_current_user
from app.services.gamification_service import (
    get_or_create_user_streak,
    check_and_update_daily_streak,
    get_leaderboard_data,
    get_adaptive_difficulty_recommendation
)

router = APIRouter(prefix="/gamification", tags=["Gamification, Streaks & Leaderboards"])

# New endpoint: Get reward history for the current user
@router.get("/rewards")
def get_reward_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Return a list of reward ledger entries for the user, sorted by most recent.
    Each entry includes event type, reference id, XP delta and timestamp.
    """
    rewards = db.query(RewardLedger).filter(RewardLedger.user_id == current_user.id).order_by(RewardLedger.created_at.desc()).all()
    return [
        {
            "event_type": r.event_type,
            "reference_id": r.reference_id,
            "xp_delta": r.xp_delta,
            "created_at": r.created_at.isoformat()
        }
        for r in rewards
    ]

@router.get("/profile")
def get_gamification_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Returns total XP, player level, streak info, and earned badges.
    Utilises get_user_profile from gamification_service.
    """
    from app.services.gamification_service import get_user_profile
    return get_user_profile(db, current_user)


@router.get("/leaderboard")
def get_leaderboard(
    grade: Optional[int] = Query(None, ge=1, le=12, description="Filter by student grade (e.g. 11 or 12)"),
    timeframe: str = Query("all_time", pattern="^(all_time|weekly)$"),
    limit: int = Query(50, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-43, FR-44, FR-45, FR-46:
    Returns the friendly competition leaderboard.
    - Anonymized display names only.
    - Filterable by Grade (Grade 11, Grade 12, or All) and Timeframe (all_time, weekly).
    - Preserves ties: equal rank for equal XP.
    """
    return get_leaderboard_data(db=db, grade=grade, timeframe=timeframe, limit=limit)

@router.get("/streak")
def get_streak_status(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-34: Returns the student's active practice streak.
    """
    streak = get_or_create_user_streak(db, current_user.id)
    return {
        "current_streak": streak.current_streak,
        "longest_streak": streak.longest_streak,
        "total_days_practiced": streak.total_days_practiced,
        "last_practice_date": streak.last_practice_date.isoformat() if streak.last_practice_date else None
    }

@router.post("/streak/claim")
def claim_daily_streak(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-34: Logs qualifying daily practice and awards +5 XP daily bonus.
    """
    return check_and_update_daily_streak(db, current_user)

@router.get("/adaptive/{topic_id}")
def get_adaptive_difficulty(
    topic_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-40, FR-41, FR-42:
    Rule-based difficulty recommendation for a topic based on student's rolling accuracy.
    """
    return get_adaptive_difficulty_recommendation(db, current_user, topic_id)

