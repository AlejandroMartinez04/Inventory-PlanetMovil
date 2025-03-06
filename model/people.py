from .connection import query_turso

### para DB en la nube

# def select_by_id(id_persona):
#     conn = create_connection()
#     sql = "SELECT * FROM \"Persona\" WHERE usuario = %s;"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql,(id_persona,))
#         persona = cur.fetchone()
#         return persona
#     except Error as e:
#         print("Error selecting persona by id:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

def select_by_id(id):
    query = f"SELECT * FROM Persona WHERE usuario = '{id}';"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        # print("Resultados:", results)  # Imprimir los resultados
        
        if results['rows']:
            columns = results['columns']
            row = results['rows'][0]
            result_dict = {columns[i]: row[i] for i in range(len(columns))}
            return result_dict  # Devuelve el diccionario
        else:
            print("Error enviando datos a la base de datos")

    return None  # Si no hay resultados, devuelve None