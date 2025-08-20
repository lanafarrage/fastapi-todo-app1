# FastAPI To-Do App

A simple To-Do List API built with **FastAPI** to manage tasks using CRUD operations (Create, Read, Update, Delete).

## Features

- **Add a task** (`POST /tasks`)
- **View all tasks** (`GET /tasks`)
- **Update task status** (`PUT /tasks/{task_id}`)
- **Delete a task** (`DELETE /tasks/{task_id}`)

## Requirements

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic

Install dependencies:

```bash
python3 -m pip install fastapi "uvicorn[standard]" pydantic
