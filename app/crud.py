from sqlmodel import Session, select
from .models import User, Message
from .database import engine


# ---------------------
# Users
# ---------------------

def create_user(username: str, role: str) -> User:
    """
    Create new user
    """
    with Session(engine) as session:
        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def get_user(username: str) -> User | None:
    """
    Search user by name
    """
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        return session.exec(statement).first()


# ---------------------
# Messages / History
# ---------------------

def save_message(username: str, question: str, response: str) -> Message:
    """
    Save question and response
    """
    with Session(engine) as session:
        msg = Message(username=username, question=question, response=response)
        session.add(msg)
        session.commit()
        session.refresh(msg)
        return msg


def get_user_history(username: str) -> list[Message]:
    """
    Get chat history
    """
    with Session(engine) as session:
        statement = select(Message).where(Message.username == username)
        return list(session.exec(statement))
