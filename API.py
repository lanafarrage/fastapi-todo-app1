from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory task storage
tasks = []

# Task model
class Task(BaseModel):
    title: str
    completed: bool = False

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

# POST - Add a new task
@app.post("/tasks")
def create_task(task: Task):
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "title": task.title, "completed": task.completed}
    tasks.append(new_task)
    return new_task

# GET - View all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# PUT - Update a task's completion status
@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE - Remove a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")