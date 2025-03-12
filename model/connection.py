import os
import requests
import sys
from dotenv import load_dotenv

def resource_path(relative_path):
    """Devuelve la ruta absoluta de un recurso, empaquetado o no."""
    try:
        base_path = sys._MEIPASS  # Cuando está empaquetado
    except AttributeError:
        base_path = os.path.abspath(".")  # En desarrollo
    return os.path.join(base_path, relative_path)

env_path = resource_path(".env")

load_dotenv(dotenv_path=env_path)

TURSO_DB_AUTH_TOKEN = os.getenv("TURSO_DB_AUTH_TOKEN")
TURSO_DB_URL = os.getenv("TURSO_DB_URL")

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