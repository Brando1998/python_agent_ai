from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.routes import chat_routes, user_routes, health_routes
from app.config import USE_OPENAI_MOCK

print(f"🔁 Usando {'mock' if USE_OPENAI_MOCK else 'cliente real'} de OpenAI")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init app
    init_db()
    yield

app = FastAPI(
    title="Chatbot de Evaluación de Riesgos",
    lifespan=lifespan
)

# Routes
app.include_router(user_routes.router)
app.include_router(chat_routes.router)
app.include_router(health_routes.router)
