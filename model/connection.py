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

### conection for render postgrest


# import psycopg2
# import pyodbc
# from psycopg2 import OperationalError

# def create_connection():
#     try:
#         server = 'planetmovilserversql.database.windows.net'
#         database = 'bbdplanetmovil'
#         username = 'adminsql'
#         password = 'Di5970791'
#         driver = '{ODBC Driver 17 for SQL Server}'

#         conn = pyodbc.connect(f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}')

#         return conn
#     except OperationalError as e:
#         print("Error connecting to db: " + str(e))
