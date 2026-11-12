from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter(prefix="/db", tags=["Database"])

@router.get("/ping", summary="Database connectivity test")
def db_ping(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    bind = db.get_bind()
    return {
        "ok": True,
        "database": bind.dialect.name,
        "driver": bind.dialect.driver,
    }
    
