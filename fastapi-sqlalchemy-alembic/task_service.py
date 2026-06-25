from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import TaskDB
from schemas import TaskCreate


def create_task(task: TaskCreate, db: Session):

    db_task = TaskDB(
        title=task.title,
        completed=task.completed
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(db: Session):

    return db.query(TaskDB).all()


def get_task(task_id: int, db: Session):

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


def update_task(task_id: int, updated_task: TaskCreate, db: Session):

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = updated_task.title
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task


def delete_task(task_id: int, db: Session):

    task = db.query(TaskDB).filter(
        TaskDB.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}