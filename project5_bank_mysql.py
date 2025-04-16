import mysql.connector
import random
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database="bank"

)
print(con)
cur=con.cursor()
# cur.execute('create database bank')
# cur.execute("create table bank(acc_no int,name varchar(20),amount int)")

print("Welcome to XYZ bank")

def start():
    print("\nPress 1 if you are New user")
    print ("Press 2 if you are Existing user\n")
    a=int(input())
    if a == 1:
        name=input("Enter your name : ")
        b=int(input("Enter openinh balance : "))
        acc=random.randint(1000,9999)
        print("\n Account successfuly created with account no. : ",acc)
        sql=f"INSERT INTO bank(acc_no,name,amount) values(%s,%s,%s)"
        values=(acc,name,b)
        cur.execute(sql,values)
        con.commit()
        menu()
    elif a==2:
        menu()

def menu():
    print("\nPress 1 for credit")
    print("Press 2 for withdrawl")
    print("Press 3 to delete your account")
    print("Press 4 to get info. of your account\n")
    a=int(input())
    if a==1:
        b=int(input("Enter your account no. : "))
        check(b)
        c=int(input("Enter amount : "))
        cur.execute(f'update bank set amount=amount+{c} where acc_no={b}')
        con.commit()
        cur.execute(f'select amount from bank where acc_no={b}')
        for i in cur:
            print("\nAmount successfully credited")
            print('Updated balance : ',i[0])
        ask()
        # con.commit()

    elif a==2:
        b=int(input("Enter your account no. : "))
        check(b)
        c=int(input("Enter amount : "))
        cur.execute(f'select amount from bank where acc_no={b}')
        for i in cur:
            if i[0]>=c:
              cur.execute(f'update bank set amount=amount-{c} where acc_no={b}')
              con.commit()
              cur.execute(f'select amount from bank where acc_no={b}')
              for j in cur:
                print("\nAmount successfully withdrawn")
                print('Updated balance : ',j[0])
            else:
                print("\nYour account balance is less then the amount you want to withdraw")
            break
        ask()

    elif a==3:
        b=int(input("Enter your account no. : "))
        check(b)
        cur.execute(f'select amount from bank')
        for i in cur:
            if i[0]==b:
                cur.execute(f'delete from bank where acc_no={b}')
                con.commit()
                print("Account sccessfully deleted")
            
    elif a==4:
        b=int(input("Enter your account no. : "))
        check(b)
        cur.execute(f'select * from bank where acc_no={b}')
        for i in cur:
            print("\nA/C NO. = ",i[0])
            print("NAME = ",i[1].upper())
            print("BALANCE = ",i[2],'\n')
            ask()
    else:
        print("\ninvalid input")
        menu()

def ask():
    print("Press 1 for main menu")
    print('Press 2 for sub menu')
    print('Press 3 to exit')
    a=int(input())
    if a == 1:
        start()
    elif a==2:
        menu()
    elif a==3:
        print("\nThank you for visiting skill circle bank")
    else:
        print('\ninvalid input')
        ask()


def check(b):
    list1=[]
    cur.execute('select * from bank')
    for i in cur:
        list1.append(i[0])
    if b in list1:
        return b
    else:
        print("\nAccount not found")
        print("\nStarting the session again.........")
        start()
            
    
        
    


con.commit()
start()
# cur.execute('select * from bank')
# for i in cur:
#     print(i)
