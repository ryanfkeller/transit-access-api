# tests/test_score.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_score_valid_address():
    VALID_ADDRESS = "123 Rural Drive"

    response = client.post("/score", json={"address":VALID_ADDRESS})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "score" in data
    assert isinstance(data["score"], int)
    assert "notes" in data
    assert isinstance(data["notes"], str)

def test_score_empty_address():
    response = client.post("/score", json={"address":""})
    assert response.status_code == 422
    details = response.json()["detail"]
    assert any(
        "Address must not be empty" in detail["msg"]
        for detail in details
    )
    
