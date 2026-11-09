from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base, SessionLocal
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.dashboard import router as dashboard_router
from app.routes.worlds import router as worlds_router
from app.routes.missions import router as missions_router
from app.routes.gamification import router as gamification_router
from app.models.user import User, UserRole
from app.services.security import hash_password
from app.services.curriculum_seed import seed_curriculum_and_badges

def seed_initial_demo_users(db):
    """Seeds default demo accounts if database is empty."""
    if db.query(User).first() is None:
        demo_users = [
            User(
                email="admin@mathquest.edu",
                display_name="Project Admin",
                password_hash=hash_password("Admin@12345"),
                role=UserRole.ADMIN,
                grade=None,
                avatar="avatar_admin",
                bio="Platform Administrator & Content Coordinator",
                is_active=True
            ),
            User(
                email="teacher@mathquest.edu",
                display_name="Ms. Fatima (Math Teacher)",
                password_hash=hash_password("Teacher@12345"),
                role=UserRole.TEACHER,
                grade=11,
                avatar="avatar_teacher",
                bio="Grade 11 & 12 Mathematics Lead Teacher",
                is_active=True
            ),
            User(
                email="student11@mathquest.edu",
                display_name="Zayd Ali",
                password_hash=hash_password("Student@12345"),
                role=UserRole.STUDENT,
                grade=11,
                avatar="avatar_explorer_1",
                bio="Grade 11 Math Adventurer",
                is_active=True
            ),
            User(
                email="student12@mathquest.edu",
                display_name="Amina Khan",
                password_hash=hash_password("Student@12345"),
                role=UserRole.STUDENT,
                grade=12,
                avatar="avatar_explorer_2",
                bio="Grade 12 Calculus Seeker",
                is_active=True
            )
        ]
        db.add_all(demo_users)
        db.commit()
        print("Successfully seeded demo accounts (Admin, Teacher, Student 11, Student 12).")

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
app.include_router(gamification_router, prefix=settings.API_V1_STR)

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
