# app/routers/paso1_bienvenida.py
from fastapi import APIRouter, FastAPI, FastAPI
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
def bienvenida() -> dict[str, str]:
    return {"mensaje": "Bienvenido al curso de FastAPI + uv", "paso": "1"}



class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str
    
@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv!",
            "author": "Maria Jose Taco",
            "version": "1.0.0"
            }

@app.get("/Maria")
def endpoint_maria() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno="Este es un mensaje de Maria")


@app.get("/Taco", response_model=Mensaje)
def endpoint_taco():
    return {"texto": "Hola Naria", "prioridad": 5, "campo_interno": "no debería salir"}


@app.get("/Campo-interno", response_model=Mensaje)
def endpoint_campo_interno():
    return {"texto": "Hola Naria", "prioridad": 5, "campo_interno": "Este es el campo interno"}

@app.get("/Campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Naria", "prioridad": 5, "campo_interno": "no debería salir", "campo_extra": "Este campo no está en el modelo"}
