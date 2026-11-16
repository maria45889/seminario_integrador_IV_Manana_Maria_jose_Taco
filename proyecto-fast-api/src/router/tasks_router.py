# app/routers/paso1_path_basico.py
from fastapi import APIRouter

router = APIRouter()

TASKS = [
    {"id": 1, "title": "Comprar leche", "is_completed": False, "priority": "medium"},
    {"id": 2, "title": "Pagar el internet", "is_completed": True, "priority": "high"},
    {"id": 3, "title": "Leer el capítulo 3", "is_completed": False, "priority": "low"},
]


@router.get("/tasks/{task_id}")
def get_task(task_id: int) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            return task
    return {"error": "Tarea no encontrada"}

{
    "detail": [
        {
            "type": "int_parsing",
            "loc": ["path", "task_id"],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "input": "abc"
        }
    ]
}