from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.curriculum import Mission, Topic, World
from app.schemas.curriculum import (
    MissionDetailResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
    CompleteMissionResponse
)
from app.services.auth_service import get_current_user
from app.services.mission_service import (
    get_mission_for_student,
    evaluate_and_record_attempt,
    complete_mission,
    check_mission_unlock_status
)

router = APIRouter(prefix="/missions", tags=["Missions & Questions"])

@router.get("/{mission_id}", response_model=MissionDetailResponse)
def get_mission(
    mission_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-11, FR-12, FR-27, FR-38:
    Retrieves mission briefing, unlock status explanation, and questions (MCQs & Numeric).
    Stripped of answers/explanations prior to submission.
    """
    mission = db.query(Mission).filter(Mission.id == mission_id, Mission.is_active == True).first()
    if not mission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found.")

    topic = db.query(Topic).filter(Topic.id == mission.topic_id).first()
    world = db.query(World).filter(World.id == topic.world_id).first() if topic else None

    # FR-11: Prevent student from accessing missions outside their enrolled grade
    if current_user.role.value == "student" and world and current_user.grade:
        if world.grade != current_user.grade:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"This mission belongs to Grade {world.grade}. Your active profile is set to Grade {current_user.grade}."
            )

    return get_mission_for_student(db, mission_id, current_user)

@router.post("/{mission_id}/attempt", response_model=SubmitAnswerResponse)
def submit_question_attempt(
    mission_id: int,
    attempt_in: SubmitAnswerRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-14, FR-15, FR-17, FR-18, FR-22, FR-23, FR-24, FR-28, FR-33:
    Submits answer (MCQ or Numeric with tolerance). Checks correctness, returns step-by-step
    teacher explanation, and awards 10 XP idempotently.
    """
    mission = db.query(Mission).filter(Mission.id == mission_id, Mission.is_active == True).first()
    if not mission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found.")

    # Check if student is allowed to attempt this mission
    is_unlocked, unlock_reason = check_mission_unlock_status(db, current_user, mission)
    if not is_unlocked and current_user.role.value == "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Cannot attempt locked mission: {unlock_reason}"
        )

    return evaluate_and_record_attempt(
        db=db,
        student=current_user,
        mission_id=mission_id,
        question_id=attempt_in.question_id,
        submitted_answer=attempt_in.submitted_answer
    )

@router.post("/{mission_id}/complete", response_model=CompleteMissionResponse)
def finalize_mission(
    mission_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    FR-19, FR-28, FR-31, FR-36, FR-39:
    Finalizes the mission attempt or retry run. Calculates accuracy %, awards completion bonus XP,
    evaluates newly unlocked missions and achievement badges.
    """
    return complete_mission(db=db, student=current_user, mission_id=mission_id)
