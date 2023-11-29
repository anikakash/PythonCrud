from student import Student
from student_manager import StudentManager

if __name__ == "__main__":
    student_manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Update Student")
        print("3. Show Students")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            roll = input("Enter student roll: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            new_student = Student(roll, name, age, grade)
            student_manager.add_student(new_student)

        elif choice == "2":
            student_roll = input("Enter student roll to update: ")
            name = input("Enter updated name: ")
            age = int(input("Enter updated age: "))
            grade = input("Enter updated grade: ")
            updated_student = Student(student_roll, name, age, grade)
            student_manager.update_student(student_roll, updated_student)

        elif choice == "3":
            student_manager.show_students()

        elif choice == "4":
            student_roll = input("Enter student roll to delete: ")
            student_manager.delete_student(student_roll)

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
