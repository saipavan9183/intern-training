from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import TaskCreate
import task_service

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/tasks", status_code=201)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return task_service.create_task(task, db)


@router.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db)
):
    return task_service.get_tasks(db)


@router.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return task_service.get_task(task_id, db)


@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    updated_task: TaskCreate,
    db: Session = Depends(get_db)
):
    return task_service.update_task(
        task_id,
        updated_task,
        db
    )


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return task_service.delete_task(task_id, db)