import mysql.connector

connection = mysql.connector.connect(host='localhost',database='phonediary',user='root',password='1234')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")