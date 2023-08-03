import sqlite3 
from sqlite3 import Error
from .connection import create_connection

def insert_product(data):
    conn = create_connection()
    sql = """ INSERT INTO products (Nombre, Cantidad, Precio_ingreso, Precio, Ganancia) 
    VALUES(?,?,?,?,?)"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        # print("nuevo producto agregado")
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
                                Precio = ? 
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
    sql = "SELECT * FROM products"

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
    sql = f"SELECT * FROM products WHERE Id_producto = {Id_producto}"
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
    sql = f"SELECT * FROM products WHERE Nombre LIKE '%{nombre}%'"
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

