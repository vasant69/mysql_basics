import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Vasant@123.com")
print(mydb)
cursor= mydb.cursor()
#cursor.execute("create database test11")
#s = "create table test1.t1(s_id int(10), ename Varchar(20), esalary int(10))"
#cursor.execute(s)
a=cursor.execute("select * from test1.t1")
#aa="insert into  test1.t1 values(1 , 'vasant vyas' , 26163)"
#cursor.execute(aa)
#print(aa)
#mydb.commit()
l=[]
for i in cursor.fetchall():
    l.append(i)
    print(l)