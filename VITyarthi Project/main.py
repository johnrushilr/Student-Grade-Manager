import operations

def main_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        # Error Handling for Input
        if choice == '1':
            operations.add_student()
        elif choice == '2':
            operations.view_students()
        elif choice == '3':
            operations.search_student()
        elif choice == '4':
            operations.delete_student()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()