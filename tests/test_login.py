from server import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check():
    response = client.post("/login")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}