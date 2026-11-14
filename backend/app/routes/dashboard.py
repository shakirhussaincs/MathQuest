from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth_service import get_current_user, require_teacher, require_admin
from app.services.dashboard_service import (
    get_student_dashboard_data,
    get_teacher_dashboard_data,
    get_admin_dashboard_data
)

router = APIRouter(prefix="/dashboard", tags=["Dashboards"])

@router.get("/student")
def get_student_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Returns the comprehensive Student Dashboard for the authenticated student:
    - Welcome screen and profile
    - Current player level and XP threshold breakdown
    - Learning progress summary and overall question accuracy
    - Available mathematics worlds for user's grade with completion tracking
    - Recently completed missions with timestamps and scores
    - Rule-based recommended next mission (revision or curriculum advancement)
    - Achievement summary with earned and locked badges
    """
    return get_student_dashboard_data(db, current_user)

@router.get("/teacher")
def get_teacher_dashboard(
    grade: Optional[int] = Query(None, ge=1, le=12),
    current_user: User = Depends(require_teacher),
    db: Session = Depends(get_db)
):
    """
    Returns the Educator Workspace for authenticated teachers and admins:
    - Teacher profile and assigned grade
    - Grade Learning Insights (aggregate student count, attempts, accuracy)
    - Mathematics Curriculum Explorer (worlds, topics, missions)
    - Grade 1-12 curriculum coverage summary
    """
    return get_teacher_dashboard_data(db, current_user, grade=grade)

@router.get("/admin")
def get_admin_dashboard(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    Returns the Platform Command Console for authenticated administrators:
    - User stats and distribution by role
    - Curriculum stats and Grade 1-12 coverage matrix
    - System health, environment, and active attempt sessions
    """
    return get_admin_dashboard_data(db, current_user)


