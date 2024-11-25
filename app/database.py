from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL for the SQLite database file
DATABASE_URL = "sqlite:///./task_manager.db"

# Create an engine instance, with echo=True to log SQL statements
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a session factory used to create new session instances
SessionLocal = sessionmaker(bind=engine)

# Base class for declarative models, which will be used for all models
Base = declarative_base()


def get_db():
    """
    Dependency function that provides a database session for each request.
    
    This function is used in FastAPI routes to ensure that a fresh session is created 
    for each API request, and the session is properly closed after the request is finished.
    
    Yields:
        db: The database session instance to be used in API route functions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
