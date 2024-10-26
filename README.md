# FastAPI Backend

Este es un backend de prueba construido con FastAPI.

## Requisitos

- Python 3.9 o superior
- Docker

## Instalación

1. **Clona el repositorio** o descarga los archivos.

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd fastapi-backend

  python3 -m venv env
  source env/bin/activate

  pip install -r requirements.txt


## Ejecución

  docker build -t fastapi-backend .
  docker run -d -p 8000:8000 --name fastapi-container fastapi-backend
  curl http://localhost:8000/hello


  logs docker logs fastapi-container
