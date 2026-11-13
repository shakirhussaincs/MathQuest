from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.config import settings

router = APIRouter(prefix="/db", tags=["Database"])

@router.get("/ping", summary="Database connectivity test")
def db_ping(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        if settings.is_production:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Database service unavailable."
            )
        raise

    if settings.is_production:
        return {"ok": True, "status": "connected"}

    bind = db.get_bind()
    return {
        "ok": True,
        "database": bind.dialect.name,
        "driver": bind.dialect.driver,
    }

    
