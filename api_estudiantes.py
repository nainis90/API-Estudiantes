
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(
    title="API de estudiantes",
    description="API sencilla para gestionar estudiantes",
    version="1.0"
)

estudiantes = [
    {"id": 1, "nombre": "Adrian", "edad": 20},
    {"id": 2, "nombre": "Maria", "edad": 21},
    {"id": 3, "nombre": "Pablo", "edad": 19}
]

class Estudiante(BaseModel):
    nombre: str
    edad: int

@app.get("/")
def inicio():
    return FileResponse("index.html")

@app.get("/estudiantes")
def obtener_estudiantes():
    return estudiantes

@app.get("/estudiantes/{id}")
def obtener_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return estudiante
    raise HTTPException(404, "Estudiante no encontrado")

@app.post("/estudiantes")
def crear_estudiante(estudiante: Estudiante):
    nuevo = {
        "id": max([e["id"] for e in estudiantes], default=0) + 1,
        "nombre": estudiante.nombre,
        "edad": estudiante.edad
    }
    estudiantes.append(nuevo)
    return nuevo
