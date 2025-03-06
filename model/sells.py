import sqlite3 
from sqlite3 import Error
from .connection import query_turso2 ,query_turso

### ------------------para db en la nube ------------------------#####

def insert_sell(data):
    sql = """ INSERT INTO Ventas (Fecha, Tipo_pago, Monto_total, Ganancia_neta, Detalle_venta) 
    VALUES(?,?,?,?,?)"""

    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Venta insertada correctamente.")
            return True
        else:
            print("Error al insertar la venta.")
    except Error as e:
        print("Error inserting product: " + str(e))
        return False  # Devolver False en caso de error
    
def select_all_sells():
    sql = "SELECT * FROM Ventas"
    data = query_turso(sql)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def select_sell_by_date(date):
    sql = f"SELECT * FROM Ventas WHERE Fecha LIKE '%{date}%'"
    data = query_turso(sql)

    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def select_sell_by_date_with_product(Id_product):
    sql = f"SELECT p.nombre AS nombre_producto FROM Products p JOIN Ventas v ON p.Id_producto = v.Id_producto WHERE v.codigo = '{Id_product}';"
    data = query_turso(sql)

    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía