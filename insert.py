import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="phonediary",auth_plugin="mysql_native_password")
myCursor=mydb.cursor()
name=input("Enter the name")
p1=input("Enter the phone_no_1")
p2=input("Enter the phone_no_2")
myCursor.execute(f'insert into contacts(name,phone_no_1,phone_no_2) values("{name}","{p1}","{p2}")')
result=myCursor.fetchall()
print(myCursor.rowcount)