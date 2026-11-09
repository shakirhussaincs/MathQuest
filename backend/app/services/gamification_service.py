from datetime import datetime, date, timedelta, timezone
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.models.user import User, UserRole
from app.models.curriculum import World, Topic, Mission, Question, Attempt, MissionProgress, DifficultyLevel
from app.models.gamification import RewardLedger, Badge, UserBadge, UserStreak
from app.services.dashboard_service import calculate_player_level

def get_or_create_user_streak(db: Session, user_id: int) -> UserStreak:
    """Retrieve or initialize a student's daily streak record.
    """
    streak = db.query(UserStreak).filter(UserStreak.user_id == user_id).first()
    if not streak:
        streak = UserStreak(
            user_id=user_id,
            current_streak=0,
            longest_streak=0,
            last_practice_date=None,
            total_days_practiced=0
        )
        db.add(streak)
        db.commit()
        db.refresh(streak)
    return streak


def list_all_badges(db: Session) -> List[Dict[str, Any]]:
    """Return all badge definitions in the system."""
    badges = db.query(Badge).all()
    return [
        {
            "id": b.id,
            "code": b.code,
            "name": b.name,
            "description": b.description,
            "icon": b.icon,
            "category": b.category,
            "criteria_description": b.criteria_description,
        }
        for b in badges
    ]


def get_user_badges(db: Session, user_id: int) -> List[Dict[str, Any]]:
    """Return badges earned by the specified user."""
    ub_list = db.query(UserBadge).filter(UserBadge.user_id == user_id).all()
    result = []
    for ub in ub_list:
        badge = db.query(Badge).filter(Badge.id == ub.badge_id).first()
        if badge:
            result.append({
                "id": badge.id,
                "code": badge.code,
                "name": badge.name,
                "description": badge.description,
                "icon": badge.icon,
                "awarded_at": ub.awarded_at.isoformat()
            })
    return result

    """Collect comprehensive gamification data for a user.
    Returns total XP, level info, current streak, earned badges.
    """
    # Total XP
    total_xp = db.query(func.coalesce(func.sum(RewardLedger.xp_delta), 0))\
                 .filter(RewardLedger.user_id == student.id)\
                 .scalar() or 0
    # Level calculation
    level_info = calculate_player_level(total_xp)
    # Streak
    streak = get_or_create_user_streak(db, student.id)
    # Earned badges
    earned = db.query(UserBadge).filter(UserBadge.user_id == student.id).all()
    badges = []
    for ub in earned:
        badge = db.query(Badge).filter(Badge.id == ub.badge_id).first()
        if badge:
            badges.append({
                "id": badge.id,
                "code": badge.code,
                "name": badge.name,
                "description": badge.description,
                "icon": badge.icon,
                "awarded_at": ub.awarded_at.isoformat()
            })
    return {
        "user_id": student.id,
        "total_xp": total_xp,
        "level": level_info["level"],
        "rank_title": level_info["rank_title"],
        "xp_to_next_level": level_info["xp_to_next_level"],
        "progress_percentage": level_info["progress_percentage"],
        "streak": {
            "current": streak.current_streak,
            "longest": streak.longest_streak,
            "total_days": streak.total_days_practiced,
            "last_practice_date": streak.last_practice_date.isoformat() if streak.last_practice_date else None
        },
        "badges": badges
    }

    """Retrieves or initializes a student's daily streak record."""
    streak = db.query(UserStreak).filter(UserStreak.user_id == user_id).first()
    if not streak:
        streak = UserStreak(
            user_id=user_id,
            current_streak=0,
            longest_streak=0,
            last_practice_date=None,
            total_days_practiced=0
        )
        db.add(streak)
        db.commit()
        db.refresh(streak)
    return streak

def check_and_update_daily_streak(db: Session, student: User) -> Dict[str, Any]:
    """
    Evaluates and records daily practice streak (FR-34).
    Awards +5 XP once per qualifying practice day.
    """
    today = datetime.now(timezone.utc).date()
    streak = get_or_create_user_streak(db, student.id)
    last_date = streak.last_practice_date

    xp_awarded = 0
    message = "Practice streak active."

    if last_date == today:
        # Already practiced today
        message = "You have already logged your daily practice for today! Keep up the momentum."
    elif last_date == today - timedelta(days=1):
        # Consecutive day! Streak continues
        streak.current_streak += 1
        streak.longest_streak = max(streak.longest_streak, streak.current_streak)
        streak.last_practice_date = today
        streak.total_days_practiced += 1

        # Award 5 XP idempotently
        event_ref = f"streak_{today.isoformat()}"
        existing = db.query(RewardLedger).filter(
            RewardLedger.user_id == student.id,
            RewardLedger.event_type == "daily_streak",
            RewardLedger.reference_id == event_ref
        ).first()

        if not existing:
            xp_awarded = 5
            db.add(RewardLedger(
                user_id=student.id,
                event_type="daily_streak",
                reference_id=event_ref,
                xp_delta=xp_awarded
            ))
        message = f"Streak Extended! You're on a {streak.current_streak}-day practice streak. +5 bonus XP awarded!"
    else:
        # Streak reset (more than 1 day missed or first day)
        streak.current_streak = 1
        streak.longest_streak = max(streak.longest_streak, 1)
        streak.last_practice_date = today
        streak.total_days_practiced += 1

        event_ref = f"streak_{today.isoformat()}"
        existing = db.query(RewardLedger).filter(
            RewardLedger.user_id == student.id,
            RewardLedger.event_type == "daily_streak",
            RewardLedger.reference_id == event_ref
        ).first()

        if not existing:
            xp_awarded = 5
            db.add(RewardLedger(
                user_id=student.id,
                event_type="daily_streak",
                reference_id=event_ref,
                xp_delta=xp_awarded
            ))
        message = "Daily practice recorded! 1-day practice streak initiated. +5 bonus XP awarded!"

    db.commit()

    # Check Practice Champion badge (5 distinct days)
    if streak.total_days_practiced >= 5:
        badge = db.query(Badge).filter(Badge.code == "practice_champion").first()
        if badge:
            has_badge = db.query(UserBadge).filter(
                UserBadge.user_id == student.id,
                UserBadge.badge_id == badge.id
            ).first()
            if not has_badge:
                db.add(UserBadge(user_id=student.id, badge_id=badge.id))
                db.commit()

    return {
        "current_streak": streak.current_streak,
        "longest_streak": streak.longest_streak,
        "total_days_practiced": streak.total_days_practiced,
        "last_practice_date": streak.last_practice_date.isoformat() if streak.last_practice_date else None,
        "xp_awarded": xp_awarded,
        "message": message
    }

def get_leaderboard_data(
    db: Session,
    grade: Optional[int] = None,
    timeframe: str = "all_time",
    limit: int = 50
) -> List[Dict[str, Any]]:
    """
    Generates privacy-compliant leaderboard rankings (FR-43, FR-44, FR-45, FR-46).
    - Strict privacy: display names only, never emails.
    - Tie-breaking: equal rank for equal XP.
    - Filterable by Grade (11, 12, or All) and Timeframe (all_time, weekly).
    """
    # 1. Base query for users
    user_query = db.query(User).filter(User.is_active == True, User.role == UserRole.STUDENT)
    if grade:
        user_query = user_query.filter(User.grade == grade)

    students = user_query.all()
    student_ids = [s.id for s in students]

    if not student_ids:
        return []

    # 2. XP Aggregation
    ledger_query = db.query(
        RewardLedger.user_id,
        func.coalesce(func.sum(RewardLedger.xp_delta), 0).label("total_xp")
    ).filter(RewardLedger.user_id.in_(student_ids))

    if timeframe == "weekly":
        seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
        ledger_query = ledger_query.filter(RewardLedger.created_at >= seven_days_ago)

    xp_results = dict(ledger_query.group_by(RewardLedger.user_id).all())

    # 3. Badges & Streaks mappings
    badge_counts = dict(
        db.query(UserBadge.user_id, func.count(UserBadge.id))
        .filter(UserBadge.user_id.in_(student_ids))
        .group_by(UserBadge.user_id)
        .all()
    )

    streaks = {
        st.user_id: st.current_streak
        for st in db.query(UserStreak).filter(UserStreak.user_id.in_(student_ids)).all()
    }

    # 4. Construct leaderboard list
    leaderboard = []
    for s in students:
        s_xp = xp_results.get(s.id, 0)
        level_info = calculate_player_level(s_xp)
        leaderboard.append({
            "user_id": s.id,
            "display_name": s.display_name,
            "avatar": s.avatar,
            "grade": s.grade,
            "total_xp": s_xp,
            "level": level_info["level"],
            "rank_title": level_info["rank_title"],
            "badges_count": badge_counts.get(s.id, 0),
            "current_streak": streaks.get(s.id, 0)
        })

    # Sort descending by XP, then badges count, then streak
    leaderboard.sort(key=lambda x: (x["total_xp"], x["badges_count"], x["current_streak"]), reverse=True)

    # 5. Assign equal rank for equal XP (FR-45)
    ranked_leaderboard = []
    current_rank = 1
    for idx, entry in enumerate(leaderboard[:limit]):
        if idx > 0 and entry["total_xp"] < leaderboard[idx - 1]["total_xp"]:
            current_rank = idx + 1

        ranked_leaderboard.append({
            "rank": current_rank,
            **entry
        })

    return ranked_leaderboard

def get_adaptive_difficulty_recommendation(
    db: Session,
    student: User,
    topic_id: int
) -> Dict[str, Any]:
    """
    FR-40, FR-41, FR-42: Rule-Based Adaptive Difficulty Engine.
    - If attempts >= 3 in topic:
      - Accuracy >= 80%: step up difficulty to 'hard' / 'boss'.
      - Accuracy < 40%: step down difficulty to 'easy' to reinforce basics.
      - Otherwise: 'medium'.
    - Deterministic, explainable, and educational without labeling students.
    """
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found.")

    topic_missions = db.query(Mission).filter(Mission.topic_id == topic.id, Mission.is_active == True).all()
    m_ids = [m.id for m in topic_missions]

    # Find student attempts across questions in these missions
    attempts = db.query(Attempt)\
                 .join(Question, Attempt.question_id == Question.id)\
                 .filter(Question.mission_id.in_(m_ids), Attempt.user_id == student.id)\
                 .all()

    total_attempts = len(attempts)
    correct_count = sum(1 for a in attempts if a.is_correct)
    accuracy_pct = round((correct_count / total_attempts * 100), 1) if total_attempts > 0 else 0.0

    if total_attempts < 3:
        recommended_difficulty = DifficultyLevel.EASY.value
        reason = "Initial topic exploration: Building foundational mastery."
    elif accuracy_pct >= 80.0:
        recommended_difficulty = DifficultyLevel.HARD.value
        reason = f"High proficiency demonstrated ({accuracy_pct}% accuracy). Ready for Advanced / Boss challenges."
    elif accuracy_pct < 40.0:
        recommended_difficulty = DifficultyLevel.EASY.value
        reason = f"Concept reinforcement recommended ({accuracy_pct}% accuracy). Practice foundational exercises."
    else:
        recommended_difficulty = DifficultyLevel.MEDIUM.value
        reason = f"Solid progress ({accuracy_pct}% accuracy). Recommended standard curriculum practice."

    return {
        "topic_id": topic.id,
        "topic_title": topic.title,
        "total_attempts": total_attempts,
        "accuracy_percentage": accuracy_pct,
        "recommended_difficulty": recommended_difficulty,
        "explanation": reason
    }

