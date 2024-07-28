import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '125436',
    database = 'mydb'
)
print(mydb.get_server_info())