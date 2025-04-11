from student_manager import StudentManager
 
def print_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Delete Student")
    print("5. Exit")
 
def main():
    manager = StudentManager()
 
    while True:
        print_menu()
        choice = input("Enter your choice: ")
 
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            
            
            manager.add_student(name, age, grade)
 
        elif choice == '2':
            students = manager.get_all_students()
            for student in students:
                print(student)
 
        elif choice == '3':
            student_id = int(input("Enter student ID to search: "))
            student = manager.get_student_by_id(student_id)
            if student:
                print(student)
            else:
                print("Student not found.")
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            if manager.delete_student(student_id):
                print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()