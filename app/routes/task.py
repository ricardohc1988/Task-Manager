from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse


router = APIRouter()


@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.

    Args:
        task (TaskCreate): Task data (title, description, priority, status).
        db (Session): Database session.

    Returns:
        TaskResponse: The newly created task.
    """
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    """
    Retrieve all tasks.

    Args:
        db (Session): Database session.

    Returns:
        list[TaskResponse]: List of all tasks in the database.
    """
    tasks = db.query(Task).all()
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by its ID.

    Args:
        task_id (int): ID of the task to retrieve.
        db (Session): Database session.

    Returns:
        TaskResponse: The task with the specified ID.

    Raises:
        HTTPException: If the task is not found.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    """
    Update an existing task.

    Args:
        task_id (int): ID of the task to update.
        task (TaskCreate): Updated task data.
        db (Session): Database session.

    Returns:
        TaskResponse: The updated task.

    Raises:
        HTTPException: If the task is not found.
    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.priority = task.priority
    db_task.status = task.status
    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by its ID.

    Args:
        task_id (int): ID of the task to delete.
        db (Session): Database session.

    Returns:
        TaskResponse: The deleted task.

    Raises:
        HTTPException: If the task is not found.
    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return db_task
