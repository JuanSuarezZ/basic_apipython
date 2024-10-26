# main.py
from fastapi import FastAPI
import logging

# Configura el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/hello")
def read_hello():
    logger.info("Accedieron al endpoint /hello")
    return {"message": "Hello, world!"}
