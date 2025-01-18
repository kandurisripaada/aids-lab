import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sripaada"
)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS student1 (id INT PRIMARY KEY, name VARCHAR(255), age INT, score INT, city VARCHAR(20));")


def insert_student():
    print("\n\nStarting insert_student function")
    n = int(input("Enter the number of inputs: "))

    if n == 0:
        print("Skipping the insert operation.")
        return

    for i in range(n):
        id = int(input("Enter your id: "))
        name = input("Enter a name: ")
        age = int(input("Enter the age: "))
        score = int(input("Enter the score: "))
        city = input("Enter the city: ")
        sql = "INSERT INTO student1 (id, name, age, score, city) VALUES (%s, %s, %s, %s, %s)"
        val = (id, name, age, score, city)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Student inserted successfully.")


def delete_student(name):
    print("\n\nStarting delete_student function\n")
    sql = "DELETE FROM student1 WHERE name = %s"
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(f"Student {name} deleted successfully.")


def update_student(id, name, age, score):
    print("\n\nStarting update_student function")
    sql = "UPDATE student1 SET name = %s, age = %s, score = %s WHERE id = %s"
    val = (name, age, score, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Student updated successfully.")


def display_students():
    print("\n\nStarting display_students function")
    mycursor.execute("SELECT * FROM student1")
    result = mycursor.fetchall()
    for row in result:
        print(row)


def display_students_asc():
    print("\n\nStarting display_students_asc function")
    mycursor.execute("SELECT * FROM student1 ORDER BY name ASC")
    result = mycursor.fetchall()
    for row in result:
        print(row)


def display_students_score():
    print("\n\nStarting display_students_score function")
    mycursor.execute("SELECT * FROM student1 WHERE score > 70 AND score < 90")
    result = mycursor.fetchall()
    for row in result:
        print(row)


def display_students_city():
    print("\n\nStarting display_students_city function")
    mycursor.execute("SELECT * FROM student1 WHERE city = 'hyderabad'")
    result = mycursor.fetchall()
    for row in result:
        print(row)


insert_student()
update_student(1, "John Doe", 21, 88)
display_students()
delete_student("John Doe")
display_students()
display_students_asc()
display_students_score()
display_students_city()

mydb.close()
