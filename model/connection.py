import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL y el token de autenticación
TURSO_DB_URL = os.getenv("TURSO_DB_URL")
TURSO_DB_AUTH_TOKEN = os.getenv("TURSO_DB_AUTH_TOKEN")

# TURSO_DB_URL = "https://variedadesla40-alejandromp.turso.io"
# TURSO_DB_AUTH_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3Mzk2MzQ3OTksImlkIjoiZGUzMDI1NDAtYWRmOC00MjVjLTkyMjItZTg3NmUwZGIwNzJiIn0.jeZpOe2GiHE7qA_J4lfJMtU3NLYZCQJsLkqfE1ejOwKbEWKpcV6dbRmZLTc2jgw_d759VUPMgMWsAoZ2TjvFCA"

if not TURSO_DB_URL or not TURSO_DB_AUTH_TOKEN:
    raise ValueError("Las variables de entorno TURSO_DB_URL y TURSO_DB_AUTH_TOKEN deben estar definidas")

def create_connection():
     return TURSO_DB_URL, TURSO_DB_AUTH_TOKEN

def query_turso(query):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Estructura correcta del cuerpo de la solicitud
    body = {
        "statements": [
            {
                "q": query
            }
        ]
    }
    
    response = requests.post(TURSO_DB_URL, headers=headers, json=body)
    
    if response.status_code == 200:
        print("Conexion a la base de datos exitosa", response.status_code)
        return response.json()  # Devuelve el resultado de la consulta
    else:
        print("Error en la consulta:", response.status_code, response.text)
        return None    

def query_turso2(query, data):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Estructura correcta del cuerpo de la solicitud
    body = {
        "statements": [
            {
                "q": query,
                "params": data  # Agregar los argumentos de la consulta aquí
            }
        ]
    }
    
    response = requests.post(TURSO_DB_URL, headers=headers, json=body)
    
    if response.status_code == 200:
        print("Conexion a la base de datos exitosa", response.status_code)
        return response.json()  # Devuelve el resultado de la consulta
    else:
        print("Error en la consulta:", response.status_code, response.text)
        return None