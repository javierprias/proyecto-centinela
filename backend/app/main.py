from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Backend de Centinela operando - Estado: Seguro"}

# --- ZONA DE PELIGRO ---
# Esto es una vulnerabilidad intencional para probar el pipeline
def connect_to_aws():
    # Gitleaks detectará este patrón de clave AKIA...
    aws_access_key_id = "AKIAIMW666S7BELOWKEY" 
    return "Conectado"