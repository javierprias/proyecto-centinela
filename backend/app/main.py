from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Backend de Centinela operando - Estado: Seguro"}