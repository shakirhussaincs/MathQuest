from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.user import (
    UserResponse,
    UserProfileUpdate,
    PasswordChange,
    AdminUserRoleUpdate,
    AdminUserStatusUpdate,
    MessageResponse
)
from app.services.security import hash_password, verify_password
from app.services.auth_service import get_current_user, require_admin

router = APIRouter(prefix="/users", tags=["Users & Profiles"])

# ---------------- Student / Authenticated User Profile Endpoints ----------------

@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user: User = Depends(get_current_user)):
    """
    Returns the authenticated student's or user's current profile.
    """
    return UserResponse.model_validate(current_user)

@router.patch("/me", response_model=UserResponse)
def update_my_profile(
    profile_data: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Updates the authenticated student's profile:
    - Display Name
    - Grade (1 to 12)
    - Avatar
    - Bio
    """
    if profile_data.display_name is not None:
        current_user.display_name = profile_data.display_name.strip()
    
    if profile_data.grade is not None:
        current_user.grade = profile_data.grade
        
    if profile_data.avatar is not None:
        current_user.avatar = profile_data.avatar
        
    if profile_data.bio is not None:
        current_user.bio = profile_data.bio

    db.commit()
    db.refresh(current_user)
    return UserResponse.model_validate(current_user)

@router.post("/me/change-password", response_model=MessageResponse)
def change_my_password(
    password_data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Changes the authenticated user's password after verifying the old password.
    """
    if not verify_password(password_data.old_password, current_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password entered is incorrect."
        )

    if password_data.old_password == password_data.new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from current password."
        )

    current_user.password_hash = hash_password(password_data.new_password)
    db.commit()

    return MessageResponse(message="Password successfully updated.")

# ---------------- Administrator Role-Based Management Endpoints ----------------

@router.get("/", response_model=List[UserResponse])
def admin_list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    role: Optional[UserRole] = None,
    grade: Optional[int] = Query(None, ge=1, le=12),
    db: Session = Depends(get_db),
    admin_user: User = Depends(require_admin)
):
    """
    Admin-only endpoint to list all users, with optional filtering by role or grade.
    """
    query = db.query(User)
    if role:
        query = query.filter(User.role == role)
    if grade:
        query = query.filter(User.grade == grade)

    users = query.offset(skip).limit(limit).all()
    return [UserResponse.model_validate(u) for u in users]

@router.get("/{user_id}", response_model=UserResponse)
def admin_get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    admin_user: User = Depends(require_admin)
):
    """
    Admin-only endpoint to inspect a specific user account.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return UserResponse.model_validate(user)

@router.patch("/{user_id}/role", response_model=UserResponse)
def admin_update_user_role(
    user_id: int,
    role_update: AdminUserRoleUpdate,
    db: Session = Depends(get_db),
    admin_user: User = Depends(require_admin)
):
    """
    Admin-only endpoint to grant or revoke roles (student, teacher, admin).
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    user.role = role_update.role
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

@router.patch("/{user_id}/status", response_model=UserResponse)
def admin_update_user_status(
    user_id: int,
    status_update: AdminUserStatusUpdate,
    db: Session = Depends(get_db),
    admin_user: User = Depends(require_admin)
):
    """
    Admin-only endpoint to activate or deactivate an account.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    # Guard against admin deactivating own account
    if user.id == admin_user.id and not status_update.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You cannot deactivate your own administrative account."
        )

    user.is_active = status_update.is_active
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

