from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base, SessionLocal
from app.routes.auth import router as auth_router
from app.routes.db_check import router as db_check_router
from app.routes.users import router as users_router
from app.routes.dashboard import router as dashboard_router
from app.routes.worlds import router as worlds_router
from app.routes.missions import router as missions_router
from app.routes.gamification import router as gamification_router
from app.models.user import User, UserRole
from app.services.security import hash_password
from app.services.curriculum_seed import seed_curriculum_and_badges
from sqlalchemy import func

def ensure_fixed_admin(db):
    """Create the fixed admin account if it does not already exist.

    Reads ``settings.FIXED_ADMIN_EMAIL`` and ``settings.FIXED_ADMIN_PASSWORD``,
    with direct environment variable fallbacks for 'fixed_Email' and 'Fixed_Password'.
    - In production, missing credentials raise a RuntimeError to prevent unprovisioned deployments.
    - In local development, missing credentials log and return safely.
    - Email lookup is case‑insensitive.
    - If a user with that email exists **and** is not an ADMIN, a ``RuntimeError`` is raised.
    - If an ADMIN exists and is active, nothing is done (idempotent).
    - If an ADMIN exists but is inactive, the function does not reactivate it.
    - Otherwise a new ADMIN user is created with a securely hashed password.
    """
    import os
    is_prod = settings.is_production
    email = (
        settings.FIXED_ADMIN_EMAIL
        or os.getenv("fixed_Email")
        or os.getenv("FIXED_ADMIN_EMAIL")
        or os.getenv("fixed_email")
        or os.getenv("FIXED_EMAIL")
        or ""
    ).strip().lower()
    raw_pw = (
        settings.FIXED_ADMIN_PASSWORD
        or os.getenv("Fixed_Password")
        or os.getenv("FIXED_ADMIN_PASSWORD")
        or os.getenv("fixed_password")
        or os.getenv("FIXED_PASSWORD")
    )
    if not email or not raw_pw:
        if is_prod:
            raise RuntimeError(
                "Fixed admin credentials (email and password) must be configured in production."
            )
        print("Admin provisioning skipped: fixed admin credentials not set in development environment.")
        return

    existing = db.query(User).filter(func.lower(User.email) == email).first()
    if existing:
        if existing.role != UserRole.ADMIN:
            raise RuntimeError(
                f"Fixed-admin email '{email}' already exists with role '{existing.role.value}'."
            )
        # Admin exists – respect its current active state (do not reactivate or modify).
        print(f"Fixed admin '{email}' already exists (active={existing.is_active}).")
        return

    try:
        admin_user = User(
            email=email,
            display_name="Alishba Mahesar",
            password_hash=hash_password(raw_pw),
            role=UserRole.ADMIN,
            grade=None,
            avatar="avatar_admin",
            bio="MathQuest Platform Administrator",
            is_active=True,
        )
        db.add(admin_user)
        db.commit()
        print(f"Fixed admin account provisioned successfully for '{email}'.")
    except Exception as exc:
        db.rollback()
        raise RuntimeError(f"Failed to create fixed admin account: {exc}") from exc

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables and seed default users, curriculum and badges
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_curriculum_and_badges(db)
        # Provision fixed admin
        try:
            ensure_fixed_admin(db)
        except Exception as exc:
            print(f"Admin provisioning error: {exc}")
            if settings.is_production:
                raise
    finally:
        db.close()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Gamified Mathematics Learning Platform API - Sindh STREAM Activities 2026–27",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(users_router, prefix=settings.API_V1_STR)
app.include_router(dashboard_router, prefix=settings.API_V1_STR)
app.include_router(worlds_router, prefix=settings.API_V1_STR)
app.include_router(missions_router, prefix=settings.API_V1_STR)
app.include_router(gamification_router, prefix=settings.API_V1_STR)
app.include_router(db_check_router, prefix=settings.API_V1_STR)

@app.get("/api/v1/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "platform": settings.PROJECT_NAME,
        "version": "1.0.0",
        "environment": settings.effective_environment
    }

@app.get("/", tags=["Root"])
def root():
    return {
        "message": f"Welcome to the {settings.PROJECT_NAME} API!",
        "docs": "/docs",
        "health": "/api/v1/health"
    }
