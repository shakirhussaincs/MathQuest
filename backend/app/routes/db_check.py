from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/db", tags=["Database"])

@router.get("/ping", summary="Simple DB connectivity test")
def db_ping(db: Session = Depends(get_db)):
    """Execute a trivial SELECT to guarantee the DB connection works.
    Returns ``{"ok": true}`` if the query succeeds.
    """
    # ``SELECT 1`` works on both SQLite and PostgreSQL
    db.execute("SELECT 1")
    return {"ok": True}

