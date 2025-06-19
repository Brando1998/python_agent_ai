from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.crud import get_user, create_user, get_user_history


router = APIRouter()

# Create user
class InitUserRequest(BaseModel):
    username: str
    role: str

# Create user response
class InitUserResponse(BaseModel):
    username: str
    role: str
    message: str

@router.post("/init_user", response_model=InitUserResponse)
def init_user(data: InitUserRequest):
    # Check if user exist
    existing_user = get_user(data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exist.")

    user = create_user(data.username, data.role)
    return InitUserResponse(
        username=user.username,
        role=user.role,
        message="User created"
    )


# Hystory response
class MessageItem(BaseModel):
    question: str
    response: str

@router.get("/history/{username}", response_model=list[MessageItem])
def get_history(username: str):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    messages = get_user_history(username)
    return [{"question": m.question, "response": m.response} for m in messages]

