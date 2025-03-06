# import sqlite3 
# from sqlite3 import Error
# from .connection import create_connection

# def insert_product(data):
#     conn = create_connection()
#     sql = """ INSERT INTO products (Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
#     VALUES(?,?,?,?,?,?,?)"""

#     try:
#         cur = conn.cursor()
#         cur.execute(sql, data)
#         conn.commit()
#         return True
#     except Error as e:
#         print("Error inserting product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def update_product(Id_producto, data):
#     conn = create_connection()
#     sql = f""" UPDATE Products SET 
#                                 Nombre = ?, 
#                                 Cantidad = ?, 
#                                 Precio_ingreso = ?,
#                                 Precio = ?,
#                                 Proveedor = ? 
#                 WHERE Id_producto = {Id_producto}"""

#     try:
#         cur = conn.cursor()
#         cur.execute(sql, data)
#         conn.commit()
#         # print("producto actualizado")
#         return True
#     except Error as e:
#         print("Error updating product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def update_qty_product(Id_producto, data):
#     conn = create_connection()
#     sql = f""" UPDATE Products SET 
#                                 Cantidad = {data}
#                 WHERE Id_producto = {Id_producto}"""
    
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         conn.commit()
#         # print("producto actualizado")
#         return True
#     except Error as e:
#         print("Error updating qty product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def delete_product(Id_producto):
#     conn = create_connection()
#     sql = f"DELETE FROM products WHERE Id_producto = {Id_producto}"

#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         conn.commit()
#         # print("producto eliminado")
#         return True
#     except Error as e:
#         print("Error removing product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def select_all_products():
#     conn = create_connection()
#     sql = "SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products"

#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         products = cur.fetchall()
#         return products
#     except Error as e:
#         print("Error selecting all products:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def select_product_by_id(Id_producto):
#     conn = create_connection()
#     sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Ganancia FROM products WHERE Id_producto = {Id_producto}"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         products = cur.fetchall()
#         return products
#     except Error as e:
#         print("Error selecting by Id_producto product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def select_product_by_id_search(Id_producto):
#     conn = create_connection()
#     sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         products = cur.fetchall()
#         return products
#     except Error as e:
#         print("Error selecting by Id_producto product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def select_product_by_id_search_priceInt(Id_producto):
#     conn = create_connection()
#     sql = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         products = cur.fetchall()
#         return products
#     except Error as e:
#         print("Error selecting by Id_producto product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def select_product_by_name(nombre):
#     conn = create_connection()
#     sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Nombre LIKE '%{nombre}%'"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         products = cur.fetchall()
#         return products
#     except Error as e:
#         print("Error selecting by name product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()


### ------------------para db en la nube ------------------------#####

import sqlite3 
from sqlite3 import Error
from .connection import query_turso, query_turso2

def select_all_products():
    query = "SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía


def select_product_by_id(Id_producto):
    query = f"SELECT Nombre, Cantidad, Precio, Id_producto, Ganancia FROM products WHERE Id_producto = {Id_producto}"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía


def select_product_by_id_search(Id_producto):
    query = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def select_product_by_name(nombre):
    query = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Nombre LIKE '%{nombre}%'"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def insert_product(data):
    sql = f""" INSERT INTO products (Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
    VALUES(?,?,?,?,?,?,?)"""

    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto insertado correctamente.")
            return True
        else:
            print("Error al insertar el producto.")
    except Error as e:
        print("Error inserting product: " + str(e))
        return False  # Devolver False en caso de error
    
def delete_product(Id_producto):
    sql = f"DELETE FROM products WHERE Id_producto = {Id_producto}"
   
    try:
        delete_success = query_turso(sql)
        if delete_success:
            print("Producto eliminado correctamente.")
            return True
        else:
            print("Error al eliminar el producto.")
    except Error as e:
        print("Error removing product:" + str(e))
        return False

def update_product(Id_producto, data):
    sql = f""" UPDATE Products SET 
                                Nombre = ?, 
                                Cantidad = ?, 
                                Precio_ingreso = ?,
                                Precio = ?,
                                Proveedor = ? 
                WHERE Id_producto = {Id_producto}"""
    
    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False  # Devolver False en caso de error
    
def update_qty_product(Id_producto, data):
    sql = f""" UPDATE Products SET 
                                Cantidad = {data}
                WHERE Id_producto = {Id_producto}"""
    
    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso(sql)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False  # Devolver False en caso de error