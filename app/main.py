from __future__ import annotations

from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session

from .database import get_session, init_db
from .models import TodoCreate, TodoRead, TodoUpdate
from .service import TodoService


app = FastAPI(title="FastAPI TODO CRUD", version="1.0.0")


def get_todo_service(session: Session = Depends(get_session)) -> TodoService:
    return TodoService(session)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/todos", response_model=List[TodoRead])
def list_todos(service: TodoService = Depends(get_todo_service)) -> List[TodoRead]:
    return service.list_todos()


@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(
    todo_id: int, service: TodoService = Depends(get_todo_service)
) -> TodoRead:
    todo = service.get_todo(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return todo


@app.post("/todos", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_in: TodoCreate, service: TodoService = Depends(get_todo_service)
) -> TodoRead:
    return service.create_todo(todo_in)


@app.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: int,
    todo_in: TodoUpdate,
    service: TodoService = Depends(get_todo_service),
) -> TodoRead:
    todo = service.update_todo(todo_id, todo_in)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(
    todo_id: int, service: TodoService = Depends(get_todo_service)
) -> dict:
    deleted = service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return {"detail": "Todo deleted"}


