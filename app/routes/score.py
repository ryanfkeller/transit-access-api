# app/routes/score.py

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, field_validator

from app.models.score import ScoreResult
from app.services.score import get_mock_score
from app.core.log_utils import get_logger

logger = get_logger(__name__)
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
def score_address(score_request: ScoreRequest, http_request: Request):
    logger.info(f"Received score request for address: {score_request.address}")

    # TEMP: Validate if GTFS feed is accessible
    try:
        feeds = http_request.app.state.gtfs_feeds
        rail_feed = feeds["la_metro"]["rail"]
        bus_feed = feeds["la_metro"]["bus"]
        logger.info(f"GTFS check: {len(rail_feed.stops)} rail stops, {len(bus_feed.stops)} bus stops loaded")
    except KeyError as e:
        logger.error(f"GTFS feed not found in state: {e}")
        raise HTTPException(status_code=500, detail="Internal GTFS config error")
    except Exception as e:
        logger.exception(f"Unexpected error accessing GTFS feed: {e}")
        raise HTTPException(status_code=500, detail="Error accessing GTFS feeds")

    # TEMP: Placeholder scoring logic
    try:
        result: ScoreResult = get_mock_score(score_request.address)
        logger.info(f"Returning score: {result.score} for address: {score_request.address}")
        return ScoreResponse(score=result.score, notes=result.notes)
    except Exception as e :
        logger.error(f"Unexpected error in /score: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")