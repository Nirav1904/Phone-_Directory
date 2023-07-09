import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="phonediary",auth_plugin="mysql_native_password")
myCursor=mydb.cursor()
myCursor.execute("select * from contacts")
result=myCursor.fetchall()
for i in result:
    print(i)