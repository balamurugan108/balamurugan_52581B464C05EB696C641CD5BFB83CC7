class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number}, CGPA: {self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of students
if __name__ == "__main__":
    students = [
        Student("Alice", "001", 3.8),
        Student("Bob", "002", 3.9),
        Student("Charlie", "003", 3.7),
        Student("David", "004", 3.95),
    ]

    sorted_students = sort_students(students)

    print("Sorted Students by CGPA (Descending Order):")
    for student in sorted_students:
        print(student)

