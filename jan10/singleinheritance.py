"""
Single Inheritance: Single inheritance allow child class to inherit properites from only single parent class
"""

# Base class 
class College:  # Parent class
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

# Child class 
class Student(College):  # Child class inheriting from College
    def __init__(self, name):
        super().__init__(name)  # Call the parent class's __init__ to set the name

# Create a Student object and print the name
student = Student("Pankaj")
student.print()


# Base class
class Calculate:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sum = 0  # Initialize sum to avoid reference errors

    def add(self):
        self.sum = self.num1 + self.num2       

# Child class
class Print(Calculate):
    def __init__(self, num1, num2):
        super().add
        self.add()  # Call the add method to calculate the sum
    
    def show(self):
        print(self.sum)

math = Print(5, 4)
math.show()
