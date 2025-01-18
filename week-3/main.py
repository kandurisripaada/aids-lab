import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sripaada"
)
mycursor=mydb.cursor();
name=input("Enter your name")
id = input("Enter your id")
mycursor.execute("insert into student values(%s,%s)",(id,name))
mydb.commit()