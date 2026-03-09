from __future__ import annotations

from typing import Generator

from sqlmodel import SQLModel, Session, create_engine

from .models import Todo


DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)


def init_db() -> None:
    SQLModel.metadata.create_all(bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

