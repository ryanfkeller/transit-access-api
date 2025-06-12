# app/routes/score.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from app.models.score import ScoreResult
from app.services.score import get_mock_score
from app.core.logging import logger

router = APIRouter()

class ScoreRequest(BaseModel):
    address: str

    @field_validator("address")
    @classmethod
    def must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Address must not be empty")
        return v

class ScoreResponse(BaseModel):
    score: int
    notes: str

@router.post("/score", response_model=ScoreResponse)
def score_address(request: ScoreRequest):
    logger.info(f"Received score request for address: {request.address}")

    try:
        result: ScoreResult = get_mock_score(request.address)
        logger.info(f"Returning score: {result.score} for address: {request.address}")
        return ScoreResponse(score=result.score, notes=result.notes)
    except Exception as e :
        logger.error(f"Unexpected error in /score: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")