import mysql.connector

CREATE DATABASE IF NOT EXISTS alx_book_store

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '125436',
    database = 'mydb'
)
print(mydb.get_server_info())
except mysql.connector.Error

