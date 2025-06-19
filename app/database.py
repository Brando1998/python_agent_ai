from sqlmodel import SQLModel, create_engine

# Route
DATABASE_URL = "sqlite:///./database.db"

# Create connection
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    """
    Create tables if not exist
    """
    SQLModel.metadata.create_all(engine)
