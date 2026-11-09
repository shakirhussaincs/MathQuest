from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, model_validator, ConfigDict
from app.models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    display_name: str = Field(..., min_length=2, max_length=50)

class UserRegister(UserBase):
    password: str = Field(..., min_length=6, max_length=128, description="Minimum 6 characters")
    role: UserRole = Field(default=UserRole.STUDENT)
    grade: Optional[int] = Field(None, ge=1, le=12, description="Grade from 1 to 12")
    avatar: Optional[str] = "avatar_explorer_1"

    @model_validator(mode="after")
    def check_student_grade(self):
        if self.role == UserRole.STUDENT and self.grade is None:
            raise ValueError("Grade is required for student registration (grades 1-12).")
        return self

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    role: UserRole
    grade: Optional[int] = None
    avatar: str
    bio: Optional[str] = ""
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserProfileUpdate(BaseModel):
    display_name: Optional[str] = Field(None, min_length=2, max_length=50)
    grade: Optional[int] = Field(None, ge=1, le=12)
    avatar: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)

class PasswordChange(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=6, max_length=128)

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    reset_token: str
    new_password: str = Field(..., min_length=6, max_length=128)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class AdminUserRoleUpdate(BaseModel):
    role: UserRole

class AdminUserStatusUpdate(BaseModel):
    is_active: bool

class MessageResponse(BaseModel):
    message: str
    detail: Optional[str] = None

