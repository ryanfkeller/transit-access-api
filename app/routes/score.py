# app/routes/score.py

from fastapi import APIRouter
from pydantic import BaseModel, field_validator

from app.models.score import ScoreResult
from app.services.score import get_mock_score

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
    result: ScoreResult = get_mock_score(request.address)
    return ScoreResponse(score=result.score, notes=result.notes)