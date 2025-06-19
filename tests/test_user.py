from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db

client = TestClient(app)


def setup_module(module):
    # Init Db
    init_db()


def test_create_user():
    """
    Test user creation
    """
    response = client.post("/init_user", json={
        "username": "user_test",
        "role": "expert_security"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "user_test"
    assert data["role"] == "expert_security"
    assert "Usuario creado correctamente" in data["message"]


def test_user_history_empty():
    """
    Check empty history for recently created user
    """
    response = client.get("/history/expert_security")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
