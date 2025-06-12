from fastapi import APIRouter
from .health import router as health_router
from .score import router as score_router

router = APIRouter()
router.include_router(health_router)
router.include_router(score_router)