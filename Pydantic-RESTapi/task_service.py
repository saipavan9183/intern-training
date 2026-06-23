from fastapi import HTTPException
from models import Task

tasks = []


def create_task(task: Task):
    task_id = len(tasks) + 1

    new_task = {
        "id": task_id,
        "title":task.title,
        "completed":task.completed
    }

    tasks.append(new_task)

    return new_task


def get_tasks():
    return tasks


def get_task(task_id: int):

    for task in tasks:
        if task["id"]== task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"     
    )


def update_task(task_id: int,updated_task: Task):

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed

            return task
        
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

#delete task

def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return  {
                "message": "Task deleted"
            }
    
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )