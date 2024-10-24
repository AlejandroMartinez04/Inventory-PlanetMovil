import sqlite3 
from sqlite3 import Error
from .connection import create_connection

def insert_product(data):
    conn = create_connection()
    sql = """ INSERT INTO products (Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
    VALUES(?,?,?,?,?,?,?)"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except Error as e:
        print("Error inserting product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def update_product(Id_producto, data):
    conn = create_connection()
    sql = f""" UPDATE Products SET 
                                Nombre = ?, 
                                Cantidad = ?, 
                                Precio_ingreso = ?,
                                Precio = ?,
                                Proveedor = ? 
                WHERE Id_producto = {Id_producto}"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        # print("producto actualizado")
        return True
    except Error as e:
        print("Error updating product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def update_qty_product(Id_producto, data):
    conn = create_connection()
    sql = f""" UPDATE Products SET 
                                Cantidad = {data}
                WHERE Id_producto = {Id_producto}"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # print("producto actualizado")
        return True
    except Error as e:
        print("Error updating qty product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_product(Id_producto):
    conn = create_connection()
    sql = f"DELETE FROM products WHERE Id_producto = {Id_producto}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # print("producto eliminado")
        return True
    except Error as e:
        print("Error removing product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_products():
    conn = create_connection()
    sql = "SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        products = cur.fetchall()
        return products
    except Error as e:
        print("Error selecting all products:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_product_by_id(Id_producto):
    conn = create_connection()
    sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Ganancia FROM products WHERE Id_producto = {Id_producto}"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        products = cur.fetchall()
        return products
    except Error as e:
        print("Error selecting by Id_producto product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_product_by_id_search(Id_producto):
    conn = create_connection()
    sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        products = cur.fetchall()
        return products
    except Error as e:
        print("Error selecting by Id_producto product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_product_by_id_search_priceInt(Id_producto):
    conn = create_connection()
    sql = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        products = cur.fetchall()
        return products
    except Error as e:
        print("Error selecting by Id_producto product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_product_by_name(nombre):
    conn = create_connection()
    sql = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM products WHERE Nombre LIKE '%{nombre}%'"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        products = cur.fetchall()
        return products
    except Error as e:
        print("Error selecting by name product:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


### ------------------para db en la nube ------------------------#####

# import sqlite3 
# from sqlite3 import Error
# from .connection import create_connection

# def insert_product(data):
#     conn = create_connection()
#     #sql = """ INSERT INTO products (Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
#     #VALUES(?,?,?,?,?,?)"""
#     sql = """INSERT INTO public."Products"("Nombre", "Cantidad", "Precio_ingreso", "Precio", "Ganancia", "Proveedor") VALUES (%s,%s,%s,%s,%s,%s)"""
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

# # se elimina 'Id_producto' como parametro que llega, y se agrega el id a la variable data al final
# def update_product(data):
#     conn = create_connection()
#     # sql = f""" UPDATE public."Products" SET 
#     #                             "Nombre" = ?, 
#     #                             "Cantidad" = ?, 
#     #                             "Precio_ingreso" = ?,
#     #                             "Precio" = ?,
#     #                             "Proveedor" = ? 
#     #             WHERE "Id_producto" = {Id_producto}"""
#     sql = """UPDATE public."Products" SET "Nombre"=%s, "Cantidad"=%s, "Precio_ingreso"=%s, "Precio"=%s, "Proveedor"=%s WHERE "Id_producto"=%s;"""
#     try:
#         cur = conn.cursor()
#         cur.execute(sql, data)
#         conn.commit()
#         return True
#     except Error as e:
#         print("Error updating product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def update_qty_product(id,stock):
#     conn = create_connection()
#     # sql = f""" UPDATE Products SET 
#     #                             Cantidad = {data}
#     #             WHERE Id_producto = {Id_producto}"""
#     sql = f'UPDATE public."Products" SET "Cantidad"={stock} WHERE "Id_producto"={id};'
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         conn.commit()
#         return True
#     except Error as e:
#         print("Error updating qty product:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()

# def delete_product(Id_producto):
#     conn = create_connection()
#     # sql = f"""DELETE FROM products WHERE Id_producto = {Id_producto}"""
#     sql = f'DELETE FROM public."Products" WHERE "Id_producto"={Id_producto};'

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
#     sql = f'SELECT "Nombre", "Cantidad", "Precio_ingreso", "Precio", "Id_producto", "Proveedor" FROM public."Products"'
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
#     # sql = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Ganancia FROM products WHERE Id_producto = {Id_producto}"
#     sql = f'SELECT "Nombre", "Cantidad", "Precio_ingreso", "Precio", "Id_producto", "Ganancia" FROM public."Products" WHERE "Id_producto" = {Id_producto}'
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
#     #sql = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM products WHERE Id_producto = {Id_producto}"
#     sql = f'SELECT "Nombre", "Cantidad", "Precio_ingreso", "Precio", "Id_producto", "Proveedor" FROM public."Products" WHERE "Id_producto" = {Id_producto}'
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
#     #sql = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM products WHERE Nombre LIKE '%{nombre}%'"
#     sql = f"""SELECT "Nombre", "Cantidad", "Precio_ingreso", "Precio", "Id_producto", "Proveedor" FROM public."Products" WHERE "Nombre" LIKE '%{nombre}%'"""
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

