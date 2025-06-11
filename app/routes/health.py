# app/routes/health.py

from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/health")
def health_check() :
    return {
        "status": "ok",
        "db_url_loaded": bool(os.getenv("DATABASE_URL"))
        }