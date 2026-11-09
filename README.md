
# API de estudiantes

API sencilla desarrollada con Python y FastAPI para gestionar estudiantes.

## Funciones

- Consultar si la API funciona.
- Obtener todos los estudiantes.
- Buscar un estudiante por ID.
- Añadir nuevos estudiantes.

## Tecnologías

- Python
- FastAPI
- Uvicorn
- Docker
- Ngrok

## Ejecutar localmente

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Iniciar la API:

```bash
uvicorn main:app --reload
```

## Documentación

Cuando la API esté funcionando, acceder a:

http://127.0.0.1:8000/docs

## Docker

Construir la imagen:

```bash
docker build -t api-estudiantes .
```

Ejecutar el contenedor:

```bash
docker run -p 8000:8000 api-estudiantes
```
