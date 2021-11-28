import sqlite3
from sqlite3 import Error

def create_connection(path):  # Path must be an SQLite database
    connection = None
    
    try:
        connection = sqlite3.connect(path)  # If database does not exist, it will create one
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


# For queries that don't require printing output
def execute_query(connection, query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
        
# To read from the database, must use the .fetchall() method.
def execute_read_query(connection, query):
    
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")