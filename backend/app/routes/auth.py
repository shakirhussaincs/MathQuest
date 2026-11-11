from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole
from app.schemas.user import (
    UserRegister,
    UserLogin,
    TokenResponse,
    UserResponse,
    PasswordResetRequest,
    PasswordResetConfirm,
    MessageResponse
)
from app.services.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_password_reset_token,
    verify_password_reset_token
)
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db: Session = Depends(get_db)):
    """
    Registers a new student, teacher, or admin account.
    - Validates email uniqueness.
    - Validates grade selection (1 to 12).
    - Returns authentication token and user profile.
    """
    existing_user = db.query(User).filter(User.email == user_in.email.lower()).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists."
        )

    # Hash password securely
    hashed_pw = hash_password(user_in.password)

    new_user = User(
        email=user_in.email.lower(),
        display_name=user_in.display_name.strip(),
        password_hash=hashed_pw,
        role=user_in.role,
        grade=user_in.grade,
        avatar=user_in.avatar or "avatar_explorer_1",
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate JWT token with user_id as sub
    access_token = create_access_token(data={"sub": str(new_user.id), "role": new_user.role.value})

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(new_user)
    )

@router.post("/login", response_model=TokenResponse)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticates a registered user and issues a JWT token.
    """
    user = db.query(User).filter(User.email == credentials.email.lower()).first()
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This account has been deactivated. Please contact an administrator."
        )

    access_token = create_access_token(data={"sub": str(user.id), "role": user.role.value})

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )

@router.post("/logout", response_model=MessageResponse)
def logout(current_user: User = Depends(get_current_user)):
    """
    Logs out the current user session.
    """
    return MessageResponse(
        message="Successfully logged out.",
        detail=f"Session terminated for user {current_user.display_name}."
    )

@router.post("/forgot-password", response_model=MessageResponse)
def forgot_password(req: PasswordResetRequest, db: Session = Depends(get_db)):
    """
    Initiates a password reset request. Generates a secure, signed time-limited token.
    """
    user = db.query(User).filter(User.email == req.email.lower()).first()
    if not user:
        # Prevent account enumeration by returning a generic success message
        return MessageResponse(
            message="If an account with that email exists, a password reset link has been dispatched."
        )

    reset_token = create_password_reset_token(user.email)
    
    # In prototype/development mode, return token in detail for testing and evaluation
    # Removed token disclosure for security. In production, an email should be sent with the reset link.
    return MessageResponse(
        message="If an account with that email exists, a password reset link has been dispatched."
    )

@router.post("/reset-password", response_model=MessageResponse)
def reset_password(req: PasswordResetConfirm, db: Session = Depends(get_db)):
    """
    Completes password reset using a verified reset token.
    """
    email = verify_password_reset_token(req.reset_token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password reset token is invalid or has expired."
        )

    user = db.query(User).filter(User.email == email.lower()).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User associated with token not found."
        )

    user.password_hash = hash_password(req.new_password)
    db.commit()

    return MessageResponse(message="Password has been successfully reset. You may now log in.")

