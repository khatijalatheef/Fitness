from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_booking():
    response = client.post("/book", json={
        "class_id": 999,
        "client_name": "Test User",
        "client_email": "user@example.com"
    })
    assert response.status_code == 400
