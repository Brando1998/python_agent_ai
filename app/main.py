from fastapi import FastAPI
from app.database import init_db
from app.routes import chat_routes, user_routes, health_routes

app = FastAPI(title="Chatbot de Evaluación de Riesgos")

@app.on_event("startup")
def startup():
    init_db()

# Routes
app.include_router(user_routes.router)
app.include_router(chat_routes.router)
app.include_router(health_routes.router)
