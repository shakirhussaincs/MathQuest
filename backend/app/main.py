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

    Reads ``settings.FIXED_ADMIN_EMAIL`` and ``settings.FIXED_ADMIN_PASSWORD``.
    - If either variable is missing, the function returns silently.
    - Email lookup is case‑insensitive.
    - If a user with that email exists **and** is not an ADMIN, a ``RuntimeError`` is raised.
    - If an ADMIN exists and is active, nothing is done (idempotent).
    - If an ADMIN exists but is inactive, the function does not reactivate it.
    - Otherwise a new ADMIN user is created with a securely hashed password.
    """
    email = (settings.FIXED_ADMIN_EMAIL or "").strip().lower()
    raw_pw = settings.FIXED_ADMIN_PASSWORD
    if not email or not raw_pw:
        return

    existing = db.query(User).filter(User.email == email).first()
    if existing:
        if existing.role != UserRole.ADMIN:
            raise RuntimeError(
                f"Fixed‑admin email '{email}' already exists with role '{existing.role.value}'."
            )
        # Admin exists – respect its current active state.
        return

    admin_user = User(
        email=email,
        display_name="Alishba Mahesar",
        password_hash=hash_password(raw_pw),
        role=UserRole.ADMIN,
        grade=None,
        avatar="avatar_admin",
        bio="Designated demo administrator",
        is_active=True,
    )
    db.add(admin_user)
    db.commit()

def deactivate_demo_accounts(db):
    """Set ``is_active=False`` for the historic demo accounts.
    This helper is **not** invoked automatically.
    """
    demo_emails = [
        "admin@mathquest.edu",
        "teacher@mathquest.edu",
        "student11@mathquest.edu",
        "student12@mathquest.edu",
    ]
    lowered = [e.lower() for e in demo_emails]
    db.query(User).filter(User.email.in_(lowered)).update({"is_active": False}, synchronize_session=False)
    db.commit()

    """Deprecated demo‑account seeding function – no longer creates demo users."""
    pass

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables and seed default users, curriculum and badges
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_initial_demo_users(db)
        seed_curriculum_and_badges(db)
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
app.include_router(db_check_router, prefix=settings.API_V1_STR)

@app.get("/api/v1/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "platform": settings.PROJECT_NAME,
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    }

@app.get("/", tags=["Root"])
def root():
    return {
        "message": f"Welcome to the {settings.PROJECT_NAME} API!",
        "docs": "/docs",
        "health": "/api/v1/health"
    }
