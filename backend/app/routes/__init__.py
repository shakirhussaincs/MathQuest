from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.dashboard import router as dashboard_router
from app.routes.worlds import router as worlds_router
from app.routes.missions import router as missions_router
from app.routes.gamification import router as gamification_router

__all__ = [
    "auth_router",
    "users_router",
    "dashboard_router",
    "worlds_router",
    "missions_router",
    "gamification_router"
]
