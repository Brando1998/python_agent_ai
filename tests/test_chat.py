from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.database import init_db

client = TestClient(app)


def setup_module(module):
    # Create user in db
    init_db()
    client.post("/init_user", json={
        "username": "lucas",
        "role": "experto en riesgos laborales"
    })


def test_ask_question():
    response = client.post("/ask", json={
        "username": "lucas",
        "message": "¿Qué es un riesgo laboral?"
    })
    print(response.json())
    assert response.status_code == 200
