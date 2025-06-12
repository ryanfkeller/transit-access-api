# app/services/score.py

from app.services.geocoder import geocode_address
from app.models.score import ScoreResult
from app.core.log_utils import get_logger

logger = get_logger(__name__)

def get_mock_score(address:str) -> ScoreResult :
    coords = geocode_address(address)

    if coords is None :
        return ScoreResult(score=0, notes="Could not geocode address")
    
    lat, lon = coords
    logger.debug(f"Address has the following coords -- lat: {lat}, lon: {lon}")

    # Pretend that we actually use these...
    if lat > 34.0:
        return ScoreResult(score=75, notes="Address is in a well-served region")
    else :
        return ScoreResult(score=40, notes="Limited transit access in this region")