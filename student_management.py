students = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for name, marks in students.items():
            print("Name:", name, "| Marks:", marks)

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        print("Marks:", students[name])
    else:
        print("Student not found.")

def update_student():
    name = input("Enter name to update: ")
    if name in students:
        marks = int(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated!")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted!")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")