from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.crud import get_user, save_message
from app.openai_client import get_openai_response

router = APIRouter()

# ------------------------
# Request shema
# ------------------------
class AskRequest(BaseModel):
    username: str
    message: str

# ------------------------
# Response Shema
# ------------------------
class AskResponse(BaseModel):
    response: str

# ------------------------
# Endpoint POST /ask
# ------------------------
@router.post("/ask", response_model=AskResponse)
async def ask_question(data: AskRequest):
    # Search user by name
    user = get_user(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Call open Ai agent
    try:
        answer = await get_openai_response(prompt=data.message, role=user.role)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Save interaction in database
    save_message(username=data.username, question=data.message, response=answer)

    # Return response
    return AskResponse(response=answer)
