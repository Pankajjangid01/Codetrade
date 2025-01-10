"""
Multilevel Inheritance: In multilevel inheritance the properties of derived class and base class are inherited by another class
"""

# Base class
class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

# Intermediate class
class PermanentEmployee(Employee):
    def assign_base_salary(self, base_salary):
        self.salary = base_salary  # Assign base salary

# Final derived class
class Manager(PermanentEmployee):
    def calculate_bonus(self, bonus):
        self.salary += bonus  # Add bonus to salary

# Create Manager object
manager = Manager("Pankaj")
manager.assign_base_salary(50000)  
manager.calculate_bonus(10000)     
print(f"{manager.name}'s total salary is: ${manager.salary}")