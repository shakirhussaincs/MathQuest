from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth_service import get_current_user
from app.services.dashboard_service import get_student_dashboard_data

router = APIRouter(prefix="/dashboard", tags=["Student Dashboard"])

@router.get("/student")
def get_student_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns the comprehensive Student Dashboard for the authenticated user (Module 2):
    - Welcome screen and profile
    - Current player level and XP threshold breakdown
    - Learning progress summary and overall question accuracy
    - Available mathematics worlds for user's grade with completion tracking
    - Recently completed missions with timestamps and scores
    - Rule-based recommended next mission (revision or curriculum advancement)
    - Achievement summary with earned and locked badges
    """
    return get_student_dashboard_data(db, current_user)

