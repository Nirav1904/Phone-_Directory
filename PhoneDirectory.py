from mysql.connector import connect
from mysql.connector.errors import IntegrityError
from os import system
from os import name as OS_NAME
from msvcrt import getch

mydb = connect(host = 'localhost',user = 'root',password = '1234' , database = 'phonediary' )
mycursor = mydb.cursor()
def clearScreen():
  
    # for windows
    if OS_NAME == 'nt':
        system('cls')
  
    # for mac and linux(here, os.name is 'posix')  
    else:
        system('clear')
    
clearScreen()
class Phoedirectory:
    def __init__(self,name= None,number1 = None,number2 = None):
        self.name = name
        self.number1 = number1
        self.number2 = number2

    def insert(self,name,num1,num2):
        try:
            mycursor.execute("select * from contacts order by name")
            myresult = mycursor.fetchall()
            exists=False
            for contact in myresult:
                if name.lower()==contact[0] or (num1!=None and num1 in [contact[1],contact[2]]) or (num2!=None and num2 in [contact[2],contact[1]]):
                    print("Contact already exists")
                    exists=True
                    break
            if not exists:
                if num2==None:
                    sql = "INSERT INTO contacts(name,phone_no_1) VALUES (%s, %s)"
                    val = (name.lower(),num1)
                else:
                    sql = "INSERT INTO contacts VALUES (%s, %s , %s)"
                    val = (name.lower(),num1,num2)
                mycursor.execute(sql, val)
                print(f"{mycursor.rowcount} contact added")
                mydb.commit()
        except IntegrityError:
            print("Number you entered is already exist!!!")
    def printlist(self):
        mycursor.execute("select * from contacts order by name")
        myresult = mycursor.fetchall()
        print("{:<15} {:<20} {:<20}".format("Name", "Number1", "Number2"))
        for i in myresult:
            if i[2]==None:
                print("{:<15} {:<20}".format(i[0],i[1]))
            else:
                print("{:<15} {:<20} {:<20}".format(i[0],i[1],i[2]))
            


    def search(self):
        searchdone = False
        st = ""
        char = ""
        while not searchdone:
            char = getch()
            x = char.decode('UTF-8')
            st = st+str(x)
            if char == chr(27).encode():
                break
            if char == chr(8).encode():
                st = st[:-2]
            clearScreen()
            printFormat()
            print("\nSearch :",st,end="\n")
            mycursor.execute("select * from contacts where name LIKE '%"+st+"%' or phone_no_1 LIKE '%"+st+"%' or phone_no_2 LIKE '%"+st+"%'" )
            con = mycursor.fetchall()
            found = False
            for i in con:
                if st in i[0] or i[1] or i[2]:
                    if i[2]==None:
                        print("{:<15} {:<20}".format(i[0],i[1]))
                    else:
                        print("{:<15} {:<20} {:<20}".format(i[0],i[1],i[2]))
                    found = True
            if found == False:
                print("\nContact Not found !!!")


    def delete(self,dl):
        dl = dl.lower()
        mycursor.execute("select * from contacts")
        con = mycursor.fetchall()
        found = False
        for i in con:
            if dl in i[0] or i[1] or i[2]:
                mycursor.execute("DELETE FROM contacts WHERE name like '%" + dl + "%' or phone_no_1 LIKE '%" + dl + "%' OR phone_no_2 LIKE '%" + dl + "%'")
                mydb.commit()
                print(mycursor.rowcount, "record(s) deleted")
                found = True
                break
        if found == False:
            print("Contact not found !!!")


def printFormat():
    print("---------THIS IS PHONEDIRECTORY--------------")
    print("{:<15} {:<20}".format("Operation ID","Operation"))
    print("{:<15} {:<25}".format("    1","  insert"))
    print("{:<15} {:<25}".format("    2","  search"))
    print("{:<15} {:<25}".format("    3","  delete"))
    print("{:<15} {:<25}".format("    4","  Print List"))
printFormat()
qt = True
k = Phoedirectory()

while qt:
    op = int(input("\n\nEnter the operations ID you want to perform : "))
    if op==1:
        name1=input("Enter Name : ")
        n1=input("Enter number1 :")
        n2=None
        if input(f"Do you want to add another number of {name1}? Y/n :")=="Y":
            n2=input("Enter number2 : ")
        k.insert(name1,n1,n2)
        ask = int(input("enter 1 to continue and 0 to quit : "))
        clearScreen()
        printFormat()
        if ask == 1:
            continue
        else:
            break
    if op==2:
        k.search()
        ask = int(input("enter 1 to continue and 0 to quit : "))
        clearScreen()
        printFormat()
        if ask == 1:
            continue
        else:
            break

    if op==3:
        dl = input("Enter name or number you want to delete : ")
        k.delete(dl)
        ask = int(input("enter 1 to continue and 0 to quit : "))
        clearScreen()
        printFormat()
        if ask == 1:
            continue
        else:
            break
    if op == 4:
        k.printlist()
        ask = int(input("enter 1 to continue and 0 to quit : "))
        clearScreen()
        printFormat()
        if ask == 1:
            continue
        else:
            break