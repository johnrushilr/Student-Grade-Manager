class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        # Converts the object to a dictionary for saving to JSON
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }