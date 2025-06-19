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

