from fastapi import FastAPI
from app.database import Base, SessionLocal, engine
from app.routes import task

# Initialize the FastAPI application
app = FastAPI()

# Create all the tables in the database if they don't exist yet
Base.metadata.create_all(bind=engine)

app.include_router(task.router, prefix="/tasks", tags=["tasks"])

