from __future__ import annotations

from typing import List

from sqlmodel import Session

from . import repository
from .models import Todo, TodoCreate, TodoRead, TodoUpdate


class TodoService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_todos(self) -> List[TodoRead]:
        todos = repository.get_todos(self.session)
        return [TodoRead.model_validate(todo) for todo in todos]

    def get_todo(self, todo_id: int) -> TodoRead | None:
        todo = repository.get_todo(self.session, todo_id)
        if not todo:
            return None
        return TodoRead.model_validate(todo)

    def create_todo(self, todo_in: TodoCreate) -> TodoRead:
        todo = repository.create_todo(self.session, todo_in)
        return TodoRead.model_validate(todo)

    def update_todo(self, todo_id: int, todo_in: TodoUpdate) -> TodoRead | None:
        todo = repository.update_todo(self.session, todo_id, todo_in)
        if not todo:
            return None
        return TodoRead.model_validate(todo)

    def delete_todo(self, todo_id: int) -> bool:
        return repository.delete_todo(self.session, todo_id)

