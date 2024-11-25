from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):
    """
    Schema for creating a new task.

    Attributes:
        title (str): The title of the task.
            - Max length: 255 characters.
        description (Optional[str]): A brief description of the task.
            - Max length: 255 characters.
            - Default: None.
        priority (Optional[str]): The priority level of the task.
            - Must be one of: 'low', 'medium', or 'high'.
            - Default: 'medium'.
        status (Optional[str]): The current status of the task.
            - Must be one of: 'pending' or 'completed'.
            - Default: 'pending'.
    """

    title: str = Field(..., max_length=255, description="The title of the task.")
    description: Optional[str] = Field(
        None, max_length=255, description="A brief description of the task."
    )

    priority: Optional[str] = Field(
        default="medium",
        pattern="^(low|medium|high)$",
        description="The priority of the task (low, medium, high).",
    )

    status: Optional[str] = Field(
        default="pending",
        pattern="^(pending|completed)$",
        description="The status of the task (pending, completed).",
    )


class TaskResponse(BaseModel):
    """
    Schema for returning task data in responses.

    Attributes:
        id (int): The unique identifier of the task.
        title (str): The title of the task.
        description (Optional[str]): A brief description of the task.
        priority (str): The priority level of the task.
        status (str): The current status of the task.
    """

    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str

    class Config:
        from_attributes = True
