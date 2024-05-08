import sqlite3
from sqlite3 import Error

def create_connection():

    try:
        conn = sqlite3.connect('databaseProducts.db')
        return conn
    except Error as e:
        print("Error connecting to db: " + str(e))


### ------------------para db en la nube ------------------------#####

# import psycopg2
# from psycopg2 import OperationalError

# def create_connection():
#     try:
#         conn = psycopg2.connect(
#             dbname='planetmovil',
#             user='AscencoDB_owner',
#             password='HZQoDy9nBx3l',
#             host='ep-cool-art-a4bj09uf.us-east-1.aws.neon.tech',
#             port='5432'
#         )
#         return conn
#     except OperationalError as e:
#         print("Error connecting to db: " + str(e))



