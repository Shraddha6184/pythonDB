import pymysql as p  

def connect():
    return p.connect(host="localhost", user="root",password="",database='veer_academy',port=3306)

def insert(t):
    con=connect()
    cu=con.cursor()
    q="insert into registration values(%s,%s,%s,%s,%s,%s,%s)"
    cu.execute(q,t)
    con.commit()
    con.close()
    
def select():
    con=connect()
    cu=con.cursor()
    q="select * from registration"
    #RegID=int(input("Enter student RegID:"))
    #q="select * from registration where RegID='{}'".format(RegID)
    
    cu.execute(q)
    data=cu.fetchall()
    #for i in data:
        #print(i)
    print(data)
    con.commit()
    con.close()
    
def update(id):
    con=connect()
    cu=con.cursor()
    RegID=input("Enter Student Registration ID you want to Update:")
    q="select * from registration where RegID='{}'".format(RegID)
    cu.execute(q)
    row=cu.fetchone()
    if row==None:
        print("Record Not Found!")
    else:
        print("RegID:",row[0])
        print("1]FullName:",row[1])
        print("2]Education:",row[2])
        print("3]Course:",row[3])
        print("4]DOB:",row[4])
        print("5]Contact:",row[5])
        print("6]Address:",row[6])
        print("7]Exit")

        ch=int(input("Enter which record you want to Update:"))
        p=""
        if ch==1:
            new_n=input("Enter New Name:")
            p="FullName='{}'".format(new_n)
        elif ch==2:
            new_e=input("Enter Education detail:")
            p="Education='{}'".format(new_e)
        elif ch==3:
            new_c=input("Enter Course Name:")
            p="Course='{}'".format(new_c)  
        elif ch==4:
            new_dt=input("Enter New date:")
            p="DOB='{}'".format(new_dt)  
        elif ch==5:
            new_con=input("Enter New Contact:")
            p="Contact='{}'".format(new_con)
        elif ch==6:
            new_ad=input("Enter New Address:")
            p="Address='{}'".format(new_ad)    
        elif ch==7:
            print("Exit")
        else:
            print("Invalid choice")
        if not p=='':
            qu="update registration set {} where RegID={}".format(p,RegID) 
            print(qu)
            cu.execute(qu)
            con.commit()    
            print("Record updated Successfully!!!")
    con.close()

def delete(RegID):
    con=connect()
    cu=con.cursor()
    q="delete from registration where RegID=%s"
    cu.execute(q,RegID)
    con.commit()
    con.close()
    
print("Click 1 to Insert Record of Student \nClick 2 to Retrieve Student's Data\nClick 3 to Update Student's Data\nClick 4 to Delete Student's data")
c=int(input("Enter your CHOICE:"))

if c==1:
    RegID=int(input("Enter New ID:"))
    FullName=input("Enter Full Name of Student:")
    Education=input("Enter Education Of Student:")
    Course=input("Enter Course Name:")
    DOB=input("Enter Birth Date:")
    contact=int(input("Enter Mobile Number:"))
    Address=input("Enter Address:")

    t=(RegID,FullName,Education,Course,DOB,contact,Address)
    insert(t)
    print("Record Inserted Successfully!!!")
elif c==2:
    
    select()
    
elif c==3:
    update(id)
elif c==4:
    ss=input("Enter id you want to delete")
    delete(ss)
    print("Record Deleted Successfully!!!")
else:
    print("wrong choice!")