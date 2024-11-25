# Task-Manager API

A simple API built with **FastAPI** for managing tasks. It allows users to perform CRUD operations (Create, Read, Update, Delete) on tasks. The API is backed by **SQLAlchemy** for database management and **Pydantic** for data validation.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: SQL toolkit and ORM for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server for serving FastAPI applications.
- **Python**: Programming language used to build the API.

## Installation

Follow these steps to install and run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ricardohc1988/Task-Manager.git
   cd task-api

2. **Create and activate a virtual environment:**
    ```bash
    pipenv install
    pipenv shell

3. **Run the application:**
    ```bash
    uvicorn app.main:app --reload

**Your API will be available at http://127.0.0.1:8000**


## API Endpoints
- POST /tasks: Create a new task.
- GET /tasks: Get all tasks.
- GET /tasks/{task_id}: Get a task by ID.
- PUT /tasks/{task_id}: Update a task by ID.
- DELETE /tasks/{task_id}: Delete a task by ID.
