from fastapi import APIRouter
from sqlmodel import Session
from app.database import engine
from sqlmodel import select

router = APIRouter()

@router.get("/health")
def health_check():
    # Check sqlite connection
    try:
        with Session(engine) as session:
            session.exec(select(1)).one()
        return {
            "status": "ok",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "disconnected",
            "detail": str(e)
        }
