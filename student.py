students = {}

# Function to create a new student entry
def create_student(student_id, name, age, grades):
    students[student_id] = {'Name': name, 'Age': age, 'Grades': grades}
    print(f"Student {name} added successfully.")

# Function to read student data by student_id
def read_student(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Grades: {student['Grades']}")
    else:
        print(f"No student found with ID: {student_id}")

# Function to update student data
def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]['Name'] = name
        if age:
            students[student_id]['Age'] = age
        if grades:
            students[student_id]['Grades'] = grades
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"No student found with ID: {student_id}")

# Function to delete a student entry
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"No student found with ID: {student_id}")
            
create_student(1, 'Alice', 20, {'Math': 90, 'English': 85})
create_student(2, 'Bob', 22, {'Math': 75, 'English': 78})

read_student(1)
read_student(2)

update_student(1, age=21, grades={'Math': 92, 'English': 88})

read_student(1)


delete_student(2)

read_student(2)
