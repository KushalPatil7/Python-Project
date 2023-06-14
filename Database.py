import mysql.connector as c
my_db=c.connect(
    host="localhost",
    user="root",
    password="kpips2423",
)
cursor=my_db.cursor()
query='create database School'
cursor.execute(query)
my_db.close()


import mysql.connector as c
my_db=c.connect(
    host="localhost",
    user="root",
    password="kpips2423"
)
cursor=my_db.cursor()
query='use School'
cursor.execute(query)
cursor1=my_db.cursor()
query="""
create table adm(
  admin_id int ,
  name varchar(50) ,
  password varchar(50)
  )
  """
cursor1.execute(query)

my_db.close()


import mysql.connector as c

my_db = c.connect(
    host="localhost",
    user="root",
    password="kpips2423"
)

cursor = my_db.cursor()


cursor.execute('USE School')

# Insert values into the adm table
query = """INSERT INTO adm VALUES (1390, "Kushal", "kpips2423")"""
cursor.execute(query)


my_db.commit()

my_db.close()


import mysql.connector as c

my_db = c.connect(
    host="localhost",
    user="root",
    password="kpips2423"
)

cursor = my_db.cursor()

# Select the admin database
cursor.execute('USE School')

# Select all rows from the adm table
query = 'SELECT * FROM adm;'

cursor.execute(query)
result = cursor.fetchall()

my_db.close()






# ************************************************************Student*****************************************************
import mysql.connector as c
my_db=c.connect(
    host="localhost",
    user="root",
    password="kpips2423",
)
cursor=my_db.cursor()
cursor.execute("use school")
cursor1=my_db.cursor()
query= """create table student(

     student_id int  ,
    name varchar(50),
    age int  ,
    sex varchar(50),
    standard int ,
    section varchar(1) ,
     pythonMark int,
     DataBaseMark int,
      MathMark int ,
     StatsMar int


)"""
cursor1.execute(query)
my_db.close()



def insert_student( student_id , name, age , sex, standard , section , pythonMark,  DataBaseMark, MathMark , StatsMar):

    import mysql.connector as c
    my_db=c.connect(
        host="localhost",
        user="root",
        password="kpips2423",
    )
    cursor1=my_db.cursor()
    cursor1.execute("use school")
    cursor=my_db.cursor()
    query = f"INSERT INTO student VALUES ({student_id}, '{name}', {age}, '{sex}', {standard}, '{section}', {pythonMark}, {DataBaseMark}, {MathMark}, {StatsMar})"
    cursor.execute(query)
    my_db.commit()
    my_db.close()

def delete_student(Name):
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor1 = my_db.cursor()
    cursor1.execute("USE school")
    cursor = my_db.cursor()
    query = f"DELETE FROM student WHERE name = '{Name}'"
    cursor.execute(query)
    my_db.commit()
    my_db.close()


def update_student():
    field = input("Enter the field to update: ")
    up_value = input("Enter updated value: ")
    std_id = input("Enter Student ID: ")

    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = f'UPDATE student SET {field} = "{up_value}" WHERE student_id = {std_id};'
    cursor.execute(query)
    print("VALUE UPDATED")
    my_db.commit()
    my_db.close()


def read_student():
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = 'SELECT * FROM student;'
    cursor.execute(query)
    res = cursor.fetchall()
    my_db.close()
    return res


# *******************************************************Teacher***************************************************


import mysql.connector as c
my_db=c.connect(
    host="localhost",
    user="root",
    password="kpips2423",
)
cursor=my_db.cursor()
cursor.execute("use school")
cursor1=my_db.cursor()
query= """create table teacher(

     teacher_id int ,
      name  varchar(50),
      age int,
       sex  varchar(1),
       classTeacher int,
        teacher_salary int


)"""
cursor1.execute(query)
my_db.close()



def insert_teacher( teacher_id ,name ,age ,sex, classTeacher, teacher_salary):

    import mysql.connector as c
    my_db=c.connect(
        host="localhost",
        user="root",
        password="kpips2423",
    )
    cursor1=my_db.cursor()
    cursor1.execute("use school")
    cursor=my_db.cursor()
    query = f"INSERT INTO teacher VALUES ({teacher_id}, '{name}', {age}, '{sex}', {classTeacher}, {teacher_salary})"
    cursor.execute(query)
    my_db.commit()
    my_db.close()

def delete_teacher(Name):
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor1 = my_db.cursor()
    cursor1.execute("USE school")
    cursor = my_db.cursor()
    query = f"DELETE FROM teacher WHERE name = '{Name}'"
    cursor.execute(query)
    my_db.commit()
    my_db.close()


def update_teacher():
    field = input("Enter the field to update: ")
    up_value = input("Enter updated value: ")
    std_id = input("Enter Teacher ID: ")

    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = f'UPDATE teacher SET {field} = "{up_value}" WHERE teacher_id = {std_id};'
    cursor.execute(query)
    print("VALUE UPDATED")
    my_db.commit()
    my_db.close()


def read_teacher():
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = 'SELECT * FROM teacher;'
    cursor.execute(query)
    res = cursor.fetchall()
    my_db.close()
    return res

# ****************************************************************Principal**********************************************************

import mysql.connector as c
my_db=c.connect(
    host="localhost",
    user="root",
    password="kpips2423",
)
cursor=my_db.cursor()
cursor.execute("use school")
cursor1=my_db.cursor()
query= """create table principal(

     principal_id int,
      name varchar(50),
       age int,
        sex varchar(1),
         teacher_id int,
          principal_salary int


)"""
cursor1.execute(query)
my_db.close()



def insert_principal( principal_id, name, age ,sex ,teacher_id, principal_salary):

    import mysql.connector as c
    my_db=c.connect(
        host="localhost",
        user="root",
        password="kpips2423",
    )
    cursor1=my_db.cursor()
    cursor1.execute("use school")
    cursor=my_db.cursor()
    query = f"INSERT INTO principal VALUES ({principal_id}, '{name}', {age}, '{sex}', {teacher_id}, {principal_salary})"
    cursor.execute(query)
    my_db.commit()
    my_db.close()

def delete_principal(Name):
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor1 = my_db.cursor()
    cursor1.execute("USE school")
    cursor = my_db.cursor()
    query = f"DELETE FROM principal WHERE name = '{Name}'"
    cursor.execute(query)
    my_db.commit()
    my_db.close()


def update_principal():
    field = input("Enter the field to update: ")
    up_value = input("Enter updated value: ")
    std_id = input("Enter Principal ID: ")

    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = f'UPDATE principal SET {field} = "{up_value}" WHERE principal_id = {std_id};'
    cursor.execute(query)
    print("VALUE UPDATED")
    my_db.commit()
    my_db.close()


def read_principal():
    import mysql.connector as c
    my_db = c.connect(
        host="localhost",
        user="root",
        password="kpips2423"
    )
    cursor = my_db.cursor()
    cursor.execute("USE school")
    query = 'SELECT * FROM principal;'
    cursor.execute(query)
    res = cursor.fetchall()
    my_db.close()
    return res
def main():
    admin_ID = int(input("Enter admin ID:"))
    admin_name = input("Enter admin name:")
    admin_password = input("Enter admin password:")

    if (admin_name == result[0][1] and admin_ID == result[0][0] and admin_password == result[0][2]):
        while True:
            print("Enter 1 for student")
            print("Enter 2 for teacher")
            print("Enter 3 for principal")
            print("Enter 4 for innerjoin of teacher and student")
            print("Enter 5 for innerjoin of teacher and principal")
            print("Enter 6 to exit")


            ch = int(input("Enter your choice:"))

            if ch == 1:
                print("Enter 1 to add a student")
                print("Enter 2 to delete a student")
                print("Enter 3 to update the database")
                print("Enter 4 to read the database")
                ch1 = int(input("Enter your choice:"))

                if ch1 == 1:
                    n=int(input("Enter no of students to enter:"))
                    for i in range(n):
                        print("Add details of student ",i,"\n")
                        student_id = input("Enter student ID:")
                        name = input("Enter name:")
                        age = int(input("Enter age:"))
                        sex = input("Enter sex:")
                        standard = int(input("Enter standard:"))
                        section = input("Enter section:")
                        pythonMark = int(input("Enter Python marks:"))
                        DataBaseMark = int(input("Enter Database marks:"))
                        MathMark = int(input("Enter Math marks:"))
                        StatsMar = int(input("Enter Statistics marks:"))

                        insert_student(student_id, name, age, sex, standard, section, pythonMark, DataBaseMark,
                                       MathMark, StatsMar)
                        print("Student added successfully.")


                elif ch1 == 2:
                    name = input("Enter student name to delete:")
                    delete_student(name)
                    print("Student deleted successfully.")

                elif ch1 == 3:
                    update_student()
                    print("Database updated successfully.")

                elif ch1 == 4:
                    data = read_student()
                    print("Student data:")
                    for row in data:
                        print(row)

            elif ch == 2:
                print("Enter 1 to add a teacher")
                print("Enter 2 to delete a teacher")
                print("Enter 3 to update the database")
                print("Enter 4 to read the database")
                ch1 = int(input("Enter your choice:"))

                if ch1 == 1:
                    teacher_id = input("Enter teacher ID:")
                    name = input("Enter name:")
                    age = int(input("Enter age:"))
                    sex = input("Enter sex:")
                    classTeacher = int(input("Enter class teacher:"))
                    teacher_salary = int(input("Enter teacher salary:"))

                    insert_teacher(teacher_id, name, age, sex, classTeacher, teacher_salary)
                    print("Teacher added successfully.")

                elif ch1 == 2:
                    name = input("Enter teacher name to delete:")
                    delete_teacher(name)
                    print("Teacher deleted successfully.")

                elif ch1 == 3:
                    update_teacher()
                    print("Database updated successfully.")

                elif ch1 == 4:
                    data = read_teacher()
                    print("Teacher data:")
                    for row in data:
                        print(row)

            elif ch == 3:
                print("Enter 1 to add a principal")
                print("Enter 2 to delete a principal")
                print("Enter 3 to update the database")
                print("Enter 4 to read the database")
                ch1 = int(input("Enter your choice:"))

                if ch1 == 1:
                    principal_id = input("Enter principal ID:")
                    name = input("Enter name:")
                    age = int(input("Enter age:"))
                    sex = input("Enter sex:")
                    teacher_id = int(input("Enter teacher id:"))
                    principal_salary=int(input("Enter principal salary"))

                    insert_principal(principal_id, name, age, sex,teacher_id,principal_salary )
                    print("Principal added successfully.")

                elif ch1 == 2:
                    name = input("Enter principal name to delete:")
                    delete_principal(name)
                    print("Principal deleted successfully.")

                elif ch1 == 3:
                    update_principal()
                    print("Database updated successfully.")

                elif ch1 == 4:
                    data = read_principal()
                    print("Principal data:")
                    for row in data:
                        print(row)

            elif ch == 4:
                import mysql.connector as c
                my_db=c.connect(
                    host="localhost",
                    user="root",
                    password="kpips2423",
                )
                cursor1 = my_db.cursor()
                cursor1.execute("use school")
                cursor=my_db.cursor()
                query='select *  from teacher inner join student on   teacher.classTeacher =student.standard;'
                cursor.execute(query)
                res=cursor.fetchall()
                print(res)

                my_db.close()
            elif ch == 5:
                import mysql.connector as c
                my_db = c.connect(
                    host="localhost",
                    user="root",
                    password="kpips2423",
                )
                cursor1=my_db.cursor()
                cursor1.execute("use school")
                cursor = my_db.cursor()
                query = 'select *from teacher inner join principal on principal.teacher_id=teacher.teacher_id;'
                cursor.execute(query)
                res = cursor.fetchall()
                print(res)

                my_db.close()
            elif ch==6:
                print("Thank You")
                break


if __name__ == "__main__":
    main()
