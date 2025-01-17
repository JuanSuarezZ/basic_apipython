# Dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn

# Expon el puerto 8000, que usará Uvicorn
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
