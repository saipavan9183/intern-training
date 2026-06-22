from fastapi import APIRouter
from models import Task
import task_service

router = APIRouter()

@router.post("/tasks", status_code=201)
def create_task(task: Task):
    return task_service.create_task(task)


@router.get("/tasks")
def get_tasks():
    return task_service.get_tasks()


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return task_service.get_task(task_id)


@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    return task_service.update_task(task_id, updated_task)


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return task_service.delete_task(task_id)