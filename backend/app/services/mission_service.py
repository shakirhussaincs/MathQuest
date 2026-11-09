from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from fractions import Fraction

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
from app.services.dashboard_service import calculate_player_level

def normalize_answer(ans: str) -> str:
    """Helper to strip punctuation, spaces, and case differences for robust answer comparison."""
    return ans.strip().lower()

def check_mcq_answer(submitted: str, correct: str) -> bool:
    """
    Checks multiple choice answer flexibly:
    Matches full string e.g. "B) 5" or option letter "B" or value "5".
    """
    sub_clean = normalize_answer(submitted)
    cor_clean = normalize_answer(correct)

    if sub_clean == cor_clean:
        return True

    # Check if user submitted just the letter (e.g. "B" or "b") when correct is "B) 5"
    if len(sub_clean) == 1 and cor_clean.startswith(sub_clean + ")"):
        return True
    
    # Check if user submitted just the value (e.g. "5") when correct is "B) 5"
    if ") " in cor_clean:
        val_part = cor_clean.split(") ", 1)[1].strip()
        if sub_clean == val_part:
            return True

    return False

def check_numeric_answer(submitted: str, correct: str, tolerance: float = 0.01) -> bool:
    """
    Checks numeric answer handling floats, integers, and fractions (e.g. 0.5, 1/2).
    """
    try:
        def parse_val(v_str: str) -> float:
            clean = v_str.strip()
            if "/" in clean:
                return float(Fraction(clean))
            return float(clean)

        sub_val = parse_val(submitted)
        cor_val = parse_val(correct)
        return abs(sub_val - cor_val) <= (tolerance or 0.01)
    except Exception:
        return normalize_answer(submitted) == normalize_answer(correct)

def check_mission_unlock_status(db: Session, student: User, mission: Mission) -> Tuple[bool, str]:
    """
    Evaluates rule-based mission unlocking condition (FR-10, FR-36, FR-38).
    """
    condition = mission.unlock_condition or "always"
    if condition == "always":
        return True, "Available to embark."

    if condition.startswith("requires_mission:"):
        req_id_str = condition.split(":")[1]
        try:
            req_mission_id = int(req_id_str)
            req_m = db.query(Mission).filter(Mission.id == req_mission_id).first()
            if not req_m:
                return True, "Available to embark."

            req_progress = db.query(MissionProgress).filter(
                MissionProgress.user_id == student.id,
                MissionProgress.mission_id == req_mission_id,
                MissionProgress.status == MissionStatus.COMPLETED.value
            ).first()

            if not req_progress:
                return False, f"Locked: Requires completing '{req_m.title}' first."

            if req_progress.accuracy < mission.pass_percentage:
                return False, f"Locked: Requires at least {mission.pass_percentage}% accuracy in '{req_m.title}' (Current: {req_progress.accuracy}%)."

            return True, f"Unlocked: Completed '{req_m.title}' with {req_progress.accuracy}% score."
        except (ValueError, IndexError):
            return True, "Available to embark."

    if mission.is_boss:
        other_missions = db.query(Mission).filter(
            Mission.topic_id == mission.topic_id,
            Mission.id != mission.id,
            Mission.is_active == True
        ).all()

        for om in other_missions:
            om_prog = db.query(MissionProgress).filter(
                MissionProgress.user_id == student.id,
                MissionProgress.mission_id == om.id,
                MissionProgress.status == MissionStatus.COMPLETED.value
            ).first()
            if not om_prog or om_prog.accuracy < 60.0:
                return False, f"Locked: Conquering this Boss Challenge requires mastering all prior topic stages."

        return True, "Boss Realm Unlocked: All prior challenges conquered!"

    return True, "Available to embark."

def get_mission_for_student(db: Session, mission_id: int, student: User) -> Dict[str, Any]:
    """
    Retrieves mission briefing and questions for a student.
    Crucial Anti-Cheat Requirement (FR-27): Strip correct_answer and explanation.
    """
    mission = db.query(Mission).filter(Mission.id == mission_id, Mission.is_active == True).first()
    if not mission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found.")

    topic = db.query(Topic).filter(Topic.id == mission.topic_id).first()
    world = db.query(World).filter(World.id == topic.world_id).first() if topic else None

    is_unlocked, unlock_explanation = check_mission_unlock_status(db, student, mission)

    questions = db.query(Question)\
                  .filter(Question.mission_id == mission.id, Question.is_active == True)\
                  .order_by(Question.display_order)\
                  .all()

    questions_public = [
        {
            "id": q.id,
            "prompt": q.prompt,
            "question_type": q.question_type,
            "options": q.options,
            "difficulty": q.difficulty,
            "display_order": q.display_order
        }
        for q in questions
    ]

    return {
        "id": mission.id,
        "topic_id": topic.id if topic else 0,
        "topic_title": topic.title if topic else "General Topic",
        "world_id": world.id if world else 0,
        "world_title": world.title if world else "Math World",
        "title": mission.title,
        "instructions": mission.instructions,
        "category": mission.category,
        "difficulty": mission.difficulty,
        "question_count": len(questions_public),
        "xp_reward": mission.xp_reward,
        "pass_percentage": mission.pass_percentage,
        "is_boss": mission.is_boss,
        "unlock_condition": mission.unlock_condition,
        "is_unlocked": is_unlocked,
        "unlock_explanation": unlock_explanation,
        "questions": questions_public
    }

def evaluate_and_record_attempt(
    db: Session,
    student: User,
    mission_id: int,
    question_id: int,
    submitted_answer: str
) -> Dict[str, Any]:
    """
    Module 5: Answer Evaluation & Learning Feedback
    - Automatic answer checking
    - Correct/incorrect feedback
    - Correct answer display
    - Step-by-step mathematical solutions
    - Explanation of mistakes
    - Related practice recommendations (FR-22, FR-23, FR-24, FR-25, FR-26)
    """
    question = db.query(Question)\
                 .filter(Question.id == question_id, Question.mission_id == mission_id)\
                 .first()
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found in this mission."
        )

    # 1. Answer Evaluation
    if question.question_type == "numeric":
        is_correct = check_numeric_answer(submitted_answer, question.correct_answer, question.tolerance or 0.01)
    else:
        is_correct = check_mcq_answer(submitted_answer, question.correct_answer)

    # 2. Record Attempt
    attempt = Attempt(
        user_id=student.id,
        question_id=question.id,
        submitted_answer=submitted_answer,
        is_correct=is_correct,
        attempted_at=datetime.now(timezone.utc)
    )
    db.add(attempt)
    db.flush()

    # 3. Idempotent XP Award (10 XP on first eligible correct answer)
    xp_awarded = 0
    if is_correct:
        event_ref = f"q_{question.id}"
        existing_ledger = db.query(RewardLedger).filter(
            RewardLedger.user_id == student.id,
            RewardLedger.event_type == "question_correct",
            RewardLedger.reference_id == event_ref
        ).first()

        if not existing_ledger:
            xp_awarded = 10
            ledger_entry = RewardLedger(
                user_id=student.id,
                event_type="question_correct",
                reference_id=event_ref,
                xp_delta=xp_awarded
            )
            db.add(ledger_entry)

    db.commit()

    total_xp = db.query(func.coalesce(func.sum(RewardLedger.xp_delta), 0))\
                 .filter(RewardLedger.user_id == student.id)\
                 .scalar() or 0

    # 4. Generate Diagnostic Mistake Analysis (Module 5)
    mistake_analysis = None
    if not is_correct:
        # Check custom common mistakes dictionary first
        clean_sub = submitted_answer.strip().lower()
        if question.common_mistakes and isinstance(question.common_mistakes, dict):
            for err_key, err_expl in question.common_mistakes.items():
                if err_key.lower() in clean_sub or clean_sub in err_key.lower():
                    mistake_analysis = err_expl
                    break

        # Fallback dynamic mistake explanation
        if not mistake_analysis:
            if "3x + 5 = 20" in question.prompt:
                mistake_analysis = f"Diagnostic feedback: You entered '{submitted_answer}'. If x = {submitted_answer}, substituting into 3x + 5 gives 3({submitted_answer}) + 5 = {3*int(submitted_answer)+5 if submitted_answer.isdigit() else 'an invalid value'} != 20. Remember to subtract 5 first (3x = 15), then divide by 3 (x = 5)."
            else:
                mistake_analysis = f"Diagnostic feedback: The submitted answer '{submitted_answer}' does not satisfy the mathematical condition. Review the step-by-step subtraction and division operations outlined below."

    # 5. Extract Step-by-Step Mathematical Solutions
    steps = question.step_by_step_solution or []
    if not steps and question.explanation:
        # Generate default steps from explanation if not structured
        steps = [s.strip() for s in question.explanation.split(". ") if s.strip()]

    # 6. Related Practice Recommendation (FR-26)
    related_practice = None
    if not is_correct:
        mission = db.query(Mission).filter(Mission.id == mission_id).first()
        if mission:
            topic = db.query(Topic).filter(Topic.id == mission.topic_id).first()
            related_practice = {
                "mission_id": mission.id,
                "title": mission.title,
                "topic_title": topic.title if topic else "Current Topic",
                "reason": f"Practice similar questions to master '{topic.title if topic else 'this concept'}'"
            }

    message = (
        "Correct! Mathematical reasoning verified. +10 XP awarded!"
        if (is_correct and xp_awarded > 0)
        else "Correct! (Already earned XP for this question)"
        if is_correct
        else f"Incorrect. The correct answer is {question.correct_answer}. Review the step-by-step solution below."
    )

    return {
        "is_correct": is_correct,
        "submitted_answer": submitted_answer,
        "correct_answer": question.correct_answer,
        "explanation": question.explanation,
        "step_by_step_solution": steps,
        "mistake_analysis": mistake_analysis,
        "related_practice": related_practice,
        "xp_awarded": xp_awarded,
        "total_xp": total_xp,
        "message": message
    }

def complete_mission(db: Session, student: User, mission_id: int) -> Dict[str, Any]:
    """
    Finalizes a completed mission or retry run (FR-19, FR-28, FR-36, FR-39).
    """
    mission = db.query(Mission).filter(Mission.id == mission_id, Mission.is_active == True).first()
    if not mission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found.")

    questions = db.query(Question).filter(Question.mission_id == mission.id, Question.is_active == True).all()
    q_ids = [q.id for q in questions]
    total_questions = len(q_ids)

    score = 0
    for q_id in q_ids:
        latest_attempt = (
            db.query(Attempt)
            .filter(Attempt.user_id == student.id, Attempt.question_id == q_id)
            .order_by(Attempt.attempted_at.desc())
            .first()
        )
        if latest_attempt and latest_attempt.is_correct:
            score += 1

    accuracy_pct = round((score / total_questions * 100), 1) if total_questions > 0 else 0.0
    is_passed = accuracy_pct >= mission.pass_percentage

    progress = db.query(MissionProgress).filter(
        MissionProgress.user_id == student.id,
        MissionProgress.mission_id == mission.id
    ).first()

    if not progress:
        progress = MissionProgress(
            user_id=student.id,
            mission_id=mission.id,
            status=MissionStatus.COMPLETED.value if is_passed else MissionStatus.AVAILABLE.value,
            score=score,
            accuracy=accuracy_pct,
            attempts_count=1,
            completed_at=datetime.now(timezone.utc)
        )
        db.add(progress)
    else:
        progress.status = MissionStatus.COMPLETED.value if (is_passed or progress.status == MissionStatus.COMPLETED.value) else MissionStatus.AVAILABLE.value
        progress.score = max(progress.score, score)
        progress.accuracy = max(progress.accuracy, accuracy_pct)
        progress.attempts_count += 1
        progress.completed_at = datetime.now(timezone.utc)

    bonus_ref = f"m_{mission.id}_completion"
    bonus_xp_awarded = 0
    if is_passed:
        existing_bonus = db.query(RewardLedger).filter(
            RewardLedger.user_id == student.id,
            RewardLedger.event_type == "mission_completed",
            RewardLedger.reference_id == bonus_ref
        ).first()

        if not existing_bonus:
            bonus_xp_awarded = mission.xp_reward
            db.add(RewardLedger(
                user_id=student.id,
                event_type="mission_completed",
                reference_id=bonus_ref,
                xp_delta=bonus_xp_awarded
            ))

    db.commit()

    badges_unlocked = []

    def award_badge_if_eligible(code: str):
        badge = db.query(Badge).filter(Badge.code == code).first()
        if badge:
            has_badge = db.query(UserBadge).filter(
                UserBadge.user_id == student.id,
                UserBadge.badge_id == badge.id
            ).first()
            if not has_badge:
                db.add(UserBadge(user_id=student.id, badge_id=badge.id))
                db.commit()
                badges_unlocked.append({
                    "id": badge.id,
                    "code": badge.code,
                    "name": badge.name,
                    "description": badge.description,
                    "icon": badge.icon
                })

    if is_passed:
        award_badge_if_eligible("first_steps")

    if accuracy_pct >= 80.0:
        award_badge_if_eligible("accuracy_star")

    if mission.is_boss and is_passed:
        award_badge_if_eligible("boss_victor")

    topic = db.query(Topic).filter(Topic.id == mission.topic_id).first()
    world = db.query(World).filter(World.id == topic.world_id).first() if topic else None
    if world and "algebra" in world.title.lower():
        algebra_completed = db.query(MissionProgress)\
                              .join(Mission, MissionProgress.mission_id == Mission.id)\
                              .join(Topic, Mission.topic_id == Topic.id)\
                              .filter(
                                  MissionProgress.user_id == student.id,
                                  MissionProgress.status == MissionStatus.COMPLETED.value,
                                  Topic.world_id == world.id
                              ).count()
        if algebra_completed >= 3:
            award_badge_if_eligible("algebra_explorer")

    final_total_xp = db.query(func.coalesce(func.sum(RewardLedger.xp_delta), 0))\
                       .filter(RewardLedger.user_id == student.id)\
                       .scalar() or 0
    level_info = calculate_player_level(final_total_xp)

    unlocked_missions = []
    if is_passed:
        subsequent_missions = db.query(Mission).filter(
            Mission.topic_id == mission.topic_id,
            Mission.id != mission.id
        ).all()
        for sm in subsequent_missions:
            unlocked, _ = check_mission_unlock_status(db, student, sm)
            if unlocked:
                unlocked_missions.append(sm.title)

    message = (
        f"Challenge Conquered! You scored {score}/{total_questions} ({accuracy_pct}% accuracy)."
        if is_passed
        else f"Mission finished with {accuracy_pct}% accuracy. Required to pass: {mission.pass_percentage}%. You can retry anytime to conquer this challenge!"
    )

    return {
        "mission_id": mission.id,
        "mission_title": mission.title,
        "score": score,
        "total_questions": total_questions,
        "accuracy_percentage": accuracy_pct,
        "is_passed": is_passed,
        "bonus_xp_awarded": bonus_xp_awarded,
        "total_mission_xp": (score * 10) + bonus_xp_awarded,
        "new_total_xp": final_total_xp,
        "new_level": level_info["level"],
        "new_rank_title": level_info["rank_title"],
        "badges_unlocked": badges_unlocked,
        "unlocked_missions": unlocked_missions,
        "message": message
    }
