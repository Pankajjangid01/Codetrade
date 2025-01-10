"""
Hierarchical Inheritance: In Hierarchical Inheritance there are more then one derved class which inherit properties from one base class 
"""

class Shape:
    def _init_(self):
        self.area = 0

    def display_area(self):
        print(f"The area is: {self.area}")

# Derived class 1
class Rectangle(Shape):
    def calculate_area(self, length, width):
        self.area = length * width  # Calculate and assign area for Rectangle

# Derived class 2
class Circle(Shape):
    def calculate_area(self, radius):
        self.area = 3.14 * radius ** 2  # Calculate and assign area for Circle

# Create Rectangle object
rect = Rectangle()
rect.calculate_area(10, 5) 
rect.display_area()         

# Create Circle object
circle = Circle()
circle.calculate_area(7) 
circle.display_area()      
