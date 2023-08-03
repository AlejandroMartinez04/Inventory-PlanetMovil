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