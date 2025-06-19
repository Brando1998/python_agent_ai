from fastapi import FastAPI
from app.database import init_db

app = FastAPI(title="Chatbot de Evaluación de Riesgos")

@app.on_event("startup")
def startup():
    init_db()
