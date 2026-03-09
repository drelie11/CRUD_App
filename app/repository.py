from __future__ import annotations

from typing import List, Optional

from sqlmodel import Session, select

from .models import Todo, TodoCreate, TodoUpdate


def get_todos(session: Session) -> List[Todo]:
    statement = select(Todo)
    results = session.exec(statement)
    return results.all()


def get_todo(session: Session, todo_id: int) -> Optional[Todo]:
    return session.get(Todo, todo_id)


def create_todo(session: Session, todo_in: TodoCreate) -> Todo:
    todo = Todo.from_orm(todo_in)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def update_todo(session: Session, todo_id: int, todo_in: TodoUpdate) -> Optional[Todo]:
    todo = session.get(Todo, todo_id)
    if not todo:
        return None

    todo_data = todo_in.model_dump(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(todo, key, value)

    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def delete_todo(session: Session, todo_id: int) -> bool:
    todo = session.get(Todo, todo_id)
    if not todo:
        return False

    session.delete(todo)
    session.commit()
    return True

