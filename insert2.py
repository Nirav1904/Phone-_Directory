import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='phonediary',
                                         user='root',
                                         password='1234')

    name=input("Enter the name: ")
    p1=input("Enter the phone_no_1: ")
    p2=input("Enter the phone_no_2: ")                                     


    cursor = connection.cursor()
    cursor.execute(f'insert into contacts(name,phone_no_1,phone_no_2) values("{name}","{p1}","{p2}")')
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into contacts table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into contacts table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
        