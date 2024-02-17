import sqlite3 
from sqlite3 import Error
from .connection import create_connection

def select_by_id(id_persona):
    conn = create_connection()
    sql = f"SELECT * FROM Persona WHERE usuario = '{id_persona}';"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        persona = cur.fetchone()
        return persona
    except Error as e:
        print("Error selecting by persona:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()