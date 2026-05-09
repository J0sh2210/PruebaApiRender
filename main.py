#Genera la estructura de una API básica utilizando FastAPI, con un endpoint que devuelve un mensaje de bienvenida.
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a mi API!"}
