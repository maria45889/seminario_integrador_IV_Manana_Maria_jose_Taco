# app/main.py
from fastapi import FastAPI
from src.router.hello_wrld import router
from src.tasks.router import
app = FastAPI(title="Curso FastAPI + uv")


app.include_router(router)