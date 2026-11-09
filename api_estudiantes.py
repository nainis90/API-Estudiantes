
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de estudiantes",
    description="API sencilla para gestionar estudiantes",
    version="1.0"
)

# Lista inicial de estudiantes
estudiantes = [
    {"id": 1, "nombre": "Adrian", "edad": 20},
    {"id": 2, "nombre": "Maria", "edad": 21},
    {"id": 3, "nombre": "Pablo", "edad": 19}
]


# Modelo de datos
class Estudiante(BaseModel):
    nombre: str
    edad: int


# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}


# Obtener todos los estudiantes
@app.get("/estudiantes")
def obtener_estudiantes():
    return estudiantes


# Obtener un estudiante por ID
@app.get("/estudiantes/{id}")
def obtener_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return estudiante

    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado"
    )


# Crear un nuevo estudiante
@app.post("/estudiantes")
def crear_estudiante(estudiante: Estudiante):
    nuevo = {
        "id": max([e["id"] for e in estudiantes], default=0) + 1,
        "nombre": estudiante.nombre,
        "edad": estudiante.edad
    }

    estudiantes.append(nuevo)

    return nuevo
