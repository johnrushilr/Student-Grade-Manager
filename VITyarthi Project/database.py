import json
import os

DB_FILE = "students_data.json"

def load_data():
    # Check if file exists, if not return empty list
    if not os.path.exists(DB_FILE):
        return []
    
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except:
        return [] # Return empty if file is corrupt

def save_data(students_list):
    # Saves the list of students to the JSON file
    with open(DB_FILE, "w") as file:
        json.dump(students_list, file, indent=4)