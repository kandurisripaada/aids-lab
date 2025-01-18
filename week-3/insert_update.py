import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sripaada"
)

mycursor = mydb.cursor()

# name = input("Enter your name: ")
# # mycursor.execute("update student set sname='babji' where sid=69")
# mycursor.execute("DELETE FROM student WHERE sname = %s", (name,))

mycursor.execute("select * from student")
student=mycursor.fetchall();
for std in student:
    print(std)
mydb.commit()

