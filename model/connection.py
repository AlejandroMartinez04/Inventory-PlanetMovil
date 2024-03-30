import sqlite3
from sqlite3 import Error

def create_connection():

    try:
        conn = sqlite3.connect('databaseProducts.db')
        return conn
    except Error as e:
        print("Error connecting to db: " + str(e))


# import psycopg2
# from psycopg2 import OperationalError

# def create_connection():
#     try:
#         conn = psycopg2.connect(
#             dbname='planetmovil',
#             user='camilom',
#             password='bRzdSOHMExIew7Ce6TWIfgLcOpxzXX01',
#             host='dpg-cj0oj5h8g3n9brpl1bhg-a.oregon-postgres.render.com',
#             port='5432'
#         )
#         return conn
#     except OperationalError as e:
#         print("Error connecting to db: " + str(e))



### conection for azure
        
# import pyodbc
# server = 'dbplanetmovil.database.windows.net'
# database = 'dbplanetmovil'
# username = 'adminplanet'
# password = 'diegomartinez24*'
# driver= '{ODBC Driver 17 for SQL Server}'

# def create_connection():
#     with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#         with conn.cursor() as cursor:
#             cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
#             row = cursor.fetchone()
#             while row:
#                 print (str(row[0]) + " " + str(row[1]))
#                 row = cursor.fetchone()
#     return conn



