# app/services/score.py

from app.models.score import ScoreResult

def get_mock_score(address:str) -> ScoreResult :
    if "metro" in address.lower():
        return ScoreResult(score=85, notes="Close to metro stops")
    elif "rural" in address.lower():
        return ScoreResult(score=20, notes="Low transit availability")
    else :
        return ScoreResult(score=50, notes="Average transit access")