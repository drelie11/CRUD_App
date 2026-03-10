from __future__ import annotations

from typing import Optional

from datetime import datetime

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TodoRead(TodoBase):
    id: int


class StockEODData(SQLModel):
    symbol: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: Optional[float] = None

