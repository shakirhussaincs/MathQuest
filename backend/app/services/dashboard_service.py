from typing import List, Dict, Any, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User
from app.models.curriculum import (
    World,
    Topic,
    Mission,
    Question,
    Attempt,
    MissionProgress,
    MissionStatus
)
from app.models.gamification import RewardLedger, Badge, UserBadge

LEVEL_THRESHOLDS = [
    (1, 0, 100, "Novice Numeromancer"),
    (2, 100, 250, "Equation Apprentice"),
    (3, 250, 450, "Algebra Adventurer"),
    (4, 450, 700, "Trig Tactician"),
    (5, 700, 1000, "Calculus Knight"),
    (6, 1000, 1400, "Matrix Mage"),
    (7, 1400, 1900, "Vector Vanguard"),
    (8, 1900, 2500, "Coordinate Champion"),
    (9, 2500, 3200, "Theorem Titan"),
    (10, 3200, 999999, "Math Grandmaster"),
]

def calculate_player_level(total_xp: int) -> Dict[str, Any]:
    """Calculates player level, progress to next level, and RPG rank title based on total XP."""
    for lvl, min_xp, next_xp, title in LEVEL_THRESHOLDS:
        if min_xp <= total_xp < next_xp or lvl == 10:
            range_span = next_xp - min_xp
            earned_in_level = total_xp - min_xp
            pct = min(100.0, max(0.0, (earned_in_level / range_span) * 100.0)) if range_span > 0 else 100.0
            return {
                "level": lvl,
                "current_xp": total_xp,
                "level_min_xp": min_xp,
                "next_level_xp": next_xp,
                "xp_to_next_level": max(0, next_xp - total_xp),
                "progress_percentage": round(pct, 1),
                "rank_title": title
            }
    return {
        "level": 1,
        "current_xp": 0,
        "level_min_xp": 0,
        "next_level_xp": 100,
        "xp_to_next_level": 100,
        "progress_percentage": 0.0,
        "rank_title": "Novice Numeromancer"
    }

def get_student_dashboard_data(db: Session, student: User) -> Dict[str, Any]:
    """
    Assembles the complete Student Dashboard payload according to SRS v1.0 and Module 2 features:
    - Welcome screen and profile
    - Current player level & Total XP
    - Learning progress summary
    - Available mathematics worlds with completion stats
    - Recently completed missions
    - Recommended next mission (Rule-based recommendation)
    - Achievement summary (earned & available badges)
    """
    user_grade = student.grade or 11

    # 1. Total XP from RewardLedger (strictly idempotent)
    total_xp = db.query(func.coalesce(func.sum(RewardLedger.xp_delta), 0))\
                 .filter(RewardLedger.user_id == student.id)\
                 .scalar() or 0
    level_info = calculate_player_level(total_xp)

    # 2. Total missions for student's grade & completed count
    total_grade_missions_q = db.query(Mission)\
                               .join(Topic, Mission.topic_id == Topic.id)\
                               .join(World, Topic.world_id == World.id)\
                               .filter(World.grade == user_grade, Mission.is_active == True)
    total_missions_count = total_grade_missions_q.count()

    completed_progress = db.query(MissionProgress)\
                           .join(Mission, MissionProgress.mission_id == Mission.id)\
                           .join(Topic, Mission.topic_id == Topic.id)\
                           .join(World, Topic.world_id == World.id)\
                           .filter(
                               MissionProgress.user_id == student.id,
                               MissionProgress.status == MissionStatus.COMPLETED.value,
                               World.grade == user_grade
                           ).all()
    completed_missions_count = len(completed_progress)

    completion_percentage = (
        round((completed_missions_count / total_missions_count) * 100, 1)
        if total_missions_count > 0 else 0.0
    )

    # Overall questions attempted and accuracy
    attempts = db.query(Attempt).filter(Attempt.user_id == student.id).all()
    total_attempts = len(attempts)
    correct_attempts = sum(1 for a in attempts if a.is_correct)
    overall_accuracy = (
        round((correct_attempts / total_attempts) * 100, 1)
        if total_attempts > 0 else 0.0
    )

    # 3. Available Mathematics Worlds for student's grade
    worlds = db.query(World)\
               .filter(World.grade == user_grade, World.is_active == True)\
               .order_by(World.display_order)\
               .all()
    
    worlds_data = []
    completed_mission_ids = {p.mission_id for p in completed_progress}

    for idx, world in enumerate(worlds):
        # Count missions in this world
        world_missions = db.query(Mission)\
                           .join(Topic, Mission.topic_id == Topic.id)\
                           .filter(Topic.world_id == world.id, Mission.is_active == True)\
                           .all()
        world_mission_count = len(world_missions)
        world_completed_count = sum(1 for m in world_missions if m.id in completed_mission_ids)
        world_pct = (
            round((world_completed_count / world_mission_count) * 100, 1)
            if world_mission_count > 0 else 0.0
        )

        # Unlock rule: First world is always unlocked; subsequent worlds unlock if at least 1 mission in previous is completed or order == 1
        is_unlocked = (idx == 0) or (len(completed_mission_ids) > 0)

        worlds_data.append({
            "id": world.id,
            "title": world.title,
            "description": world.description,
            "grade": world.grade,
            "icon": world.icon,
            "theme_color": world.theme_color,
            "is_unlocked": is_unlocked,
            "total_missions": world_mission_count,
            "completed_missions": world_completed_count,
            "completion_percentage": world_pct
        })

    # 4. Recently completed missions
    recent_progress = db.query(MissionProgress)\
                        .filter(
                            MissionProgress.user_id == student.id,
                            MissionProgress.status == MissionStatus.COMPLETED.value
                        )\
                        .order_by(MissionProgress.completed_at.desc())\
                        .limit(5)\
                        .all()

    recently_completed = []
    for rp in recent_progress:
        mission = db.query(Mission).filter(Mission.id == rp.mission_id).first()
        if mission:
            topic = db.query(Topic).filter(Topic.id == mission.topic_id).first()
            world = db.query(World).filter(World.id == topic.world_id).first() if topic else None
            recently_completed.append({
                "progress_id": rp.id,
                "mission_id": mission.id,
                "mission_title": mission.title,
                "topic_title": topic.title if topic else "General Topic",
                "world_title": world.title if world else "Math World",
                "score": rp.score,
                "accuracy": round(rp.accuracy, 1),
                "completed_at": rp.completed_at.isoformat() if rp.completed_at else None,
                "xp_earned": mission.xp_reward + (rp.score * 10)
            })

    # 5. Rule-Based Recommended Next Mission (SRS FR-51)
    recommended_mission = None

    # Check for weak topic first (accuracy < 70%)
    topic_accuracies: Dict[int, List[float]] = {}
    for rp in completed_progress:
        m = db.query(Mission).filter(Mission.id == rp.mission_id).first()
        if m:
            topic_accuracies.setdefault(m.topic_id, []).append(rp.accuracy)

    weak_topic_id = None
    for t_id, acc_list in topic_accuracies.items():
        avg_acc = sum(acc_list) / len(acc_list)
        if avg_acc < 70.0:
            weak_topic_id = t_id
            break

    if weak_topic_id:
        # Find an uncompleted or revision mission in this weak topic
        weak_m = db.query(Mission)\
                   .filter(Mission.topic_id == weak_topic_id, Mission.is_active == True)\
                   .first()
        if weak_m:
            topic = db.query(Topic).filter(Topic.id == weak_m.topic_id).first()
            world = db.query(World).filter(World.id == topic.world_id).first() if topic else None
            recommended_mission = {
                "mission_id": weak_m.id,
                "title": weak_m.title,
                "instructions": weak_m.instructions,
                "difficulty": weak_m.difficulty,
                "xp_reward": weak_m.xp_reward,
                "topic_title": topic.title if topic else "",
                "world_title": world.title if world else "",
                "recommendation_reason": "Revision Practice: Topic accuracy was below 70%"
            }

    # If no weak topic, pick the next uncompleted mission in student's grade
    if not recommended_mission:
        next_uncompleted = (
            db.query(Mission)
            .join(Topic, Mission.topic_id == Topic.id)
            .join(World, Topic.world_id == World.id)
            .filter(
                World.grade == user_grade,
                Mission.is_active == True,
                ~Mission.id.in_(completed_mission_ids) if completed_mission_ids else True
            )
            .order_by(World.display_order, Topic.display_order, Mission.display_order)
            .first()
        )
        if next_uncompleted:
            topic = db.query(Topic).filter(Topic.id == next_uncompleted.topic_id).first()
            world = db.query(World).filter(World.id == topic.world_id).first() if topic else None
            recommended_mission = {
                "mission_id": next_uncompleted.id,
                "title": next_uncompleted.title,
                "instructions": next_uncompleted.instructions,
                "difficulty": next_uncompleted.difficulty,
                "xp_reward": next_uncompleted.xp_reward,
                "topic_title": topic.title if topic else "",
                "world_title": world.title if world else "",
                "recommendation_reason": "Next in Curriculum: Continue your adventure path"
            }
        elif total_missions_count > 0:
            # Completed all missions
            first_m = total_grade_missions_q.first()
            topic = db.query(Topic).filter(Topic.id == first_m.topic_id).first()
            world = db.query(World).filter(World.id == topic.world_id).first() if topic else None
            recommended_mission = {
                "mission_id": first_m.id,
                "title": first_m.title,
                "instructions": first_m.instructions,
                "difficulty": first_m.difficulty,
                "xp_reward": first_m.xp_reward,
                "topic_title": topic.title if topic else "",
                "world_title": world.title if world else "",
                "recommendation_reason": "All Missions Mastered! Replay to practice speed & accuracy"
            }

    # 6. Achievement / Badges Summary
    all_badges = db.query(Badge).all()
    user_badge_map = {
        ub.badge_id: ub.awarded_at
        for ub in db.query(UserBadge).filter(UserBadge.user_id == student.id).all()
    }

    badges_data = []
    for b in all_badges:
        is_earned = b.id in user_badge_map
        badges_data.append({
            "id": b.id,
            "code": b.code,
            "name": b.name,
            "description": b.description,
            "icon": b.icon,
            "category": b.category,
            "criteria_description": b.criteria_description,
            "is_earned": is_earned,
            "awarded_at": user_badge_map[b.id].isoformat() if is_earned else None
        })

    return {
        "student_profile": {
            "id": student.id,
            "display_name": student.display_name,
            "email": student.email,
            "grade": student.grade,
            "avatar": student.avatar,
            "bio": student.bio,
            "role": student.role.value
        },
        "gamification": level_info,
        "learning_progress": {
            "total_missions": total_missions_count,
            "completed_missions": completed_missions_count,
            "completion_percentage": completion_percentage,
            "total_questions_attempted": total_attempts,
            "correct_answers": correct_attempts,
            "overall_accuracy_percentage": overall_accuracy
        },
        "worlds": worlds_data,
        "recently_completed_missions": recently_completed,
        "recommended_next_mission": recommended_mission,
        "achievements": {
            "total_badges": len(all_badges),
            "earned_badges_count": len(user_badge_map),
            "badges": badges_data
        }
    }

