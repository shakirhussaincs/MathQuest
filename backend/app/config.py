from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "MathQuest"
    API_V1_STR: str = "/api/v1"
    
    # 32+ byte secure key for JWT HMAC-SHA256
    SECRET_KEY: str = "mathquest-super-secure-secret-key-at-least-32-chars-stream-2026-27"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite:///./mathquest.db"
    
    # Environment
    ENVIRONMENT: str = "development"

    # Fixed demo‑admin credentials (used only by the provisioning routine)
    # These values are read from the .env file (or the host environment).
    # Example .env entries (do **not** commit this file to source control):
    #   FIXED_ADMIN_EMAIL=alishbaM@gmail.com
    #   FIXED_ADMIN_PASSWORD=123456
    FIXED_ADMIN_EMAIL: str | None = None
    FIXED_ADMIN_PASSWORD: str | None = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

