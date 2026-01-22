# tests/test_api.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    payload = {
        "age": 30,
        "bmi": 25.0,
        "children": 1,
        "smoker": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "premium_class" in response.json()
