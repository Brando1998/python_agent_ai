from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db

client = TestClient(app)
username = "b"

def setup_module(module):
    # Init Db
    init_db()


def test_create_user():
    """
    Test user creation
    """
    response = client.post("/init_user", json={
        "username": username,
        "role": "experto en riesgos laborales"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username
    assert data["role"] == "experto en riesgos laborales"
    assert "User created" in data["message"]


def test_user_history_empty():
    """
    Check empty history for recently created user
    """
    response = client.get("/history/a")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
