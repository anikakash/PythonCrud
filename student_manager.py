import mysql.connector
from student import Student

class StudentManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
        )
        self.cursor = self.db.cursor()

    def add_student(self, student):
        query = "INSERT INTO students (roll, name, age, grade) VALUES (%s, %s, %s, %s)"
        values = (student.roll, student.name, student.age, student.grade)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Student added successfully!")

    def update_student(self, student_roll, student):
        query = "UPDATE students SET roll=%s, name=%s, age=%s, grade=%s WHERE roll=%s"
        values = (student.roll, student.name, student.age, student.grade, student_roll)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Student updated successfully!")

    def show_students(self):
        query = "SELECT * FROM students"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if not result:
            print("No students found.")
        else:
            for row in result:
                print(row)

    def delete_student(self, student_roll):
        query = "DELETE FROM students WHERE roll=%s"
        value = (student_roll,)
        self.cursor.execute(query, value)
        self.db.commit()
        print("Student deleted successfully!")
