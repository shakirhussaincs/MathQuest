import os
from typing import Optional
from pydantic import AliasChoices, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "MathQuest"
    API_V1_STR: str = "/api/v1"
    
    # Environment
    ENVIRONMENT: str = Field(
        default="development",
        validation_alias=AliasChoices("ENVIRONMENT", "environment"),
    )
    VERCEL_ENV: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices("VERCEL_ENV", "vercel_env"),
    )
    
    # 32+ byte secure key for JWT HMAC-SHA256
    SECRET_KEY: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices("SECRET_KEY", "secret_key", "JWT_SECRET_KEY"),
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite:///./mathquest.db"

    # Fixed demo‑admin credentials (used only by the provisioning routine)
    # Supports FIXED_ADMIN_EMAIL, fixed_Email, fixed_email, FIXED_EMAIL
    FIXED_ADMIN_EMAIL: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "FIXED_ADMIN_EMAIL",
            "fixed_admin_email",
            "fixed_Email",
            "fixed_email",
            "FIXED_EMAIL",
        ),
    )
    # Supports FIXED_ADMIN_PASSWORD, Fixed_Password, fixed_password, FIXED_PASSWORD
    FIXED_ADMIN_PASSWORD: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "FIXED_ADMIN_PASSWORD",
            "fixed_admin_password",
            "Fixed_Password",
            "fixed_password",
            "FIXED_PASSWORD",
        ),
    )
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def is_production(self) -> bool:
        v_env = (self.VERCEL_ENV or os.getenv("VERCEL_ENV") or "").strip().lower()
        if v_env in ("production", "preview"):
            return True
        env = (self.ENVIRONMENT or os.getenv("ENVIRONMENT") or "development").strip().lower()
        return env == "production"

    @property
    def effective_environment(self) -> str:
        v_env = (self.VERCEL_ENV or os.getenv("VERCEL_ENV") or "").strip().lower()
        if v_env:
            return v_env
        return (self.ENVIRONMENT or os.getenv("ENVIRONMENT") or "development").strip().lower()

    @model_validator(mode="after")
    def validate_production_security(self):
        if self.is_production:
            raw_secret = self.SECRET_KEY
            if not raw_secret or not raw_secret.strip():
                raise RuntimeError(
                    "CRITICAL CONFIGURATION ERROR: SECRET_KEY environment variable is required in production."
                )
            insecure_samples = {
                "mathquest-super-secure-secret-key-at-least-32-chars-stream-2026-27",
                "mathquest-dev-only-insecure-secret-key-32chars!",
                "changeme",
                "secret",
            }
            if raw_secret.strip() in insecure_samples:
                raise RuntimeError(
                    "CRITICAL CONFIGURATION ERROR: Production SECRET_KEY cannot use an insecure sample or default key."
                )
            if len(raw_secret.strip().encode("utf-8")) < 32:
                raise RuntimeError(
                    "CRITICAL CONFIGURATION ERROR: Production SECRET_KEY must contain at least 32 bytes of secure randomness."
                )

            # Fix H-03: Require fixed-admin configuration in production
            email = (
                self.FIXED_ADMIN_EMAIL
                or os.getenv("fixed_Email")
                or os.getenv("FIXED_ADMIN_EMAIL")
                or os.getenv("fixed_email")
                or os.getenv("FIXED_EMAIL")
                or ""
            ).strip()
            raw_pw = (
                self.FIXED_ADMIN_PASSWORD
                or os.getenv("Fixed_Password")
                or os.getenv("FIXED_ADMIN_PASSWORD")
                or os.getenv("fixed_password")
                or os.getenv("FIXED_PASSWORD")
            )
            if not email or not raw_pw:
                raise RuntimeError(
                    "CRITICAL CONFIGURATION ERROR: Fixed admin credentials (email and password) must be configured in production."
                )
        else:
            # Dedicated development-only fallback when running outside of production
            if not self.SECRET_KEY:
                self.SECRET_KEY = "mathquest-dev-only-insecure-secret-key-32chars!"
        return self

settings = Settings()


