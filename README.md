# FastAPI TODO CRUD App

This is a simple TODO list CRUD API built with **FastAPI**, **SQLModel**, and **SQLite**, running inside a Python virtual environment.

It supports:

- View existing todos
- Add new todo
- Update todo title, description, or completed flag
- Delete todo

---

## Prerequisites

- Python 3.10+ installed and available as `python` on your PATH

---

## Setup

From the project root (`CRUD_App`):

1. **Create virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**

   On **Windows (PowerShell)**:

   ```bash
   .\venv\Scripts\Activate.ps1
   ```

   On **Windows (cmd)**:

   ```bash
   .\venv\Scripts\activate.bat
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the app

From the project root with the virtual environment activated:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The first run will create a local SQLite database file named `todo.db` in the project root.

---

## API Overview

### List todos

- **Method**: `GET`
- **URL**: `/todos`

Example (PowerShell):

```bash
curl http://127.0.0.1:8000/todos
```

### Get a single todo

- **Method**: `GET`
- **URL**: `/todos/{id}`

```bash
curl http://127.0.0.1:8000/todos/1
```

### Create a new todo

- **Method**: `POST`
- **URL**: `/todos`
- **Body (JSON)**:

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

Example (PowerShell):

```bash
curl -X POST "http://127.0.0.1:8000/todos" `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Buy groceries\",\"description\":\"Milk, eggs, bread\",\"completed\":false}"
```

### Update a todo

- **Method**: `PUT`
- **URL**: `/todos/{id}`
- **Body (JSON)** – all fields optional:

```json
{
  "title": "Buy groceries (updated)",
  "description": "Milk, eggs, bread, cheese",
  "completed": true
}
```

Example:

```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Buy groceries (updated)\",\"description\":\"Milk, eggs, bread, cheese\",\"completed\":true}"
```

You can send only the fields you want to change, for example:

```json
{
  "title": "New title only"
}
```

### Delete a todo

- **Method**: `DELETE`
- **URL**: `/todos/{id}`

```bash
curl -X DELETE "http://127.0.0.1:8000/todos/1"
```

If the todo does not exist, the API returns `404 Not Found`.

---

## Notes

- The database is a simple SQLite file (`todo.db`) suitable for development or demos.
- Data is persisted between runs as long as you keep the `todo.db` file.
- You can inspect the DB with any SQLite browser if desired.

