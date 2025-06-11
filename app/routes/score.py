# app/routes/score.py

from fastapi import APIRouter
from pydantic import BaseModel

from app.models.score import ScoreResult
from app.services.score import get_mock_score

router = APIRouter()

class ScoreRequest(BaseModel):
    address: str

class ScoreResponse(BaseModel):
    score: int
    notes: str

@router.post("/score", response_model=ScoreResponse)
def score_address(request: ScoreRequest):
    result: ScoreResult = get_mock_score(request.address)
    return ScoreResponse(result.score, result.notes)