from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """
    User model
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    role: str


class Message(SQLModel, table=True):
    """
    Message model
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    question: str
    response: str
