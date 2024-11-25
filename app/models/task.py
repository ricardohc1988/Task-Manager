from sqlalchemy import Column, Integer, String
from app.database import Base


class Task(Base):
    """
    Represents a task in the system.

    Attributes:
        __tablename__ (str): The name of the database table for tasks.
        id (Column): The primary key of the task.
        title (Column): The title of the task.
        description (Column): A brief description of the task.
        priority (Column): The priority level of the task.
        status (Column): The current status of the task.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    priority = Column(String, default="medium")
    status = Column(String, default="pending")

    def __repr__(self):
        """
        Returns a string representation of the task instance.
        """
        return f"<Task(id={self.id}, title='{self.title}', priority='{self.priority}', status='{self.status}')>"
