from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.database import init_db

client = TestClient(app)


def setup_module(module):
    # Inicializa la BD y crea un usuario de prueba
    init_db()
    client.post("/init_user", json={
        "username": "usuario_chat",
        "role": "experto en riesgos laborales"
    })


def test_ask_question():
    response = client.post("/ask", json={
        "username": "usuario_chat",
        "message": "¿Qué es un riesgo laboral?"
    })
    print(response.json())
    assert response.status_code == 200
