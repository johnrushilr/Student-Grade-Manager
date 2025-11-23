from student import Student
import database

def add_student():
    print("\n--- Add New Student ---")
    s_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    data = database.load_data()
    
    # Check for duplicate ID
    for item in data:
        if item["id"] == s_id:
            print("Error: Student ID already exists!")
            return

    new_student = Student(s_id, name, grade)
    data.append(new_student.to_dict())
    database.save_data(data)
    print("Student added successfully!")

def view_students():
    print("\n--- List of Students ---")
    data = database.load_data()
    if not data:
        print("No records found.")
    else:
        print(f"{'ID':<10} {'Name':<20} {'Grade':<10}")
        print("-" * 40)
        for s in data:
            print(f"{s['id']:<10} {s['name']:<20} {s['grade']:<10}")

def search_student():
    print("\n--- Search Student ---")
    target_id = input("Enter ID to search: ")
    data = database.load_data()
    
    found = False
    for s in data:
        if s["id"] == target_id:
            print(f"Found: {s['name']} (Grade: {s['grade']})")
            found = True
            break
    
    if not found:
        print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    target_id = input("Enter ID to delete: ")
    data = database.load_data()
    
    new_data = [s for s in data if s["id"] != target_id]
    
    if len(data) == len(new_data):
        print("ID not found, nothing deleted.")
    else:
        database.save_data(new_data)
        print("Student deleted successfully.")