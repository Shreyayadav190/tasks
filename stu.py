class Student:
    def __init__(self, name, age, grades):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.grades = grades
    
    def display_details(self):
        # Method to display student details
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
    
    def calculate_average(self):
        # Method to calculate the average grade
        if len(self.grades) > 0:
            average = sum(self.grades) / len(self.grades)
            return average
        else:
            return 0

# Example usage
student1 = Student("Mohan",20, [85, 95, 65, 32])
# Display student details
student1.display_details()

# Calculate and display average grade
average_grade = student1.calculate_average()
print(f"Average Grade: {average_grade:.2f}")
