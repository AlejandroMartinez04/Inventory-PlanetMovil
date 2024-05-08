import sqlite3 
from sqlite3 import Error
from .connection import create_connection

def insert_sell(data):
    conn = create_connection()
    sql = """ INSERT INTO Ventas (Fecha, Tipo_pago, Monto_total, Ganancia_neta, Detalle_venta) 
    VALUES(?,?,?,?,?)"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        # print("nueva venta agregada")
        return True
    except Error as e:
        print("Error inserting sell:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_sells():
    conn = create_connection()
    sql = "SELECT * FROM Ventas"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        sells = cur.fetchall()
        return sells
    except Error as e:
        print("Error selecting all sells:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_sell_by_date(date):
    conn = create_connection()
    sql = f"SELECT * FROM Ventas WHERE Fecha LIKE '%{date}%'"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        sell = cur.fetchall()
        return sell
    except Error as e:
        print("Error selecting by date sell:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_sell_by_date_with_product(Id_product):
    conn = create_connection()
    sql = f"SELECT p.nombre AS nombre_producto FROM Products p JOIN Ventas v ON p.Id_producto = v.Id_producto WHERE v.codigo = '{Id_product}';"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        sell = cur.fetchall()
        return sell
    except Error as e:
        print("Error selecting by date sell:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

### ------------------para db en la nube ------------------------#####

# import sqlite3 
# from sqlite3 import Error
# from .connection import create_connection

# def insert_sell(data):
#     conn = create_connection()
#     # sql = """ INSERT INTO Ventas (Fecha, Tipo_pago, Monto_total, Ganancia_neta, Detalle_venta) 
#     # VALUES(?,?,?,?,?)"""
#     sql = """INSERT INTO public."Ventas"("Fecha", "Tipo_pago", "Monto_total", "Ganancia_neta", "Detalle_venta") VALUES (%s,%s,%s,%s,%s)"""
#     try:
#         cur = conn.cursor()
#         cur.execute(sql, data)
#         conn.commit()
#         return True
#     except Error as e:
#         print("Error inserting sell:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()


# def select_all_sells():
#     conn = create_connection()
#     sql = 'SELECT * FROM public."Ventas"'

#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         sells = cur.fetchall()
#         return sells
#     except Error as e:
#         print("Error selecting all sells:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()


# def select_sell_by_date(date):
#     conn = create_connection()
#     #sql = f"SELECT * FROM Ventas WHERE Fecha LIKE '%{date}%'" 
#     sql = f"""SELECT * FROM public."Ventas" WHERE "Fecha" LIKE '%{date}%'"""
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         sell = cur.fetchall()
#         return sell
#     except Error as e:
#         print("Error selecting by date sell:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()


# def select_sell_by_date_with_product(Id_product):
#     conn = create_connection()
#     sql = f"SELECT p.nombre AS nombre_producto FROM Products p JOIN Ventas v ON p.Id_producto = v.Id_producto WHERE v.codigo = '{Id_product}';"
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         sell = cur.fetchall()
#         return sell
#     except Error as e:
#         print("Error selecting by date sell:" + str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
