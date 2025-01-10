"""
Multpile inheritance: Multiple inheritance allow the derived class to inherit the properties from multiple parent class 
"""

# Parent class 1
class Animal:
    def __init__(self):
        pass

    def display(self):
        print("Animal class")

    
# Parent class 2
class Dog:
    def __init__(self):
        pass

    def show(self):
        print("Dog class")

# Child class
class Eat(Animal,Dog):
    def __init__(self):
        Animal().__init__()  # inherit the properties of Animal Class 
        Dog().__init__()  #inherit the properties of Dog Class 

eat=Eat()
eat.show()
eat.display()


class Vehical:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def print_details(self):
        print(f"Vehicle: {self.name}, Model: {self.model}")

class Car:
    def __init__(self, holdername, date):
        self.holdername = holdername
        self.date = date

    def display(self):
        print(f"Holder Name: {self.holdername}, Date: {self.date}, Name:{self.name}")

class Person(Vehical, Car):
    def __init__(self, name, model, holdername, date):
        self.name = name
        self.model = model
        self.holdername = holdername
        self.date = date
        # Vehical.__init__(self, name, model)  # inherit the properties of Vehical Class 
        # Car.__init__(self, holdername, date)  # inherit the properties of Car Class

# Create an object of Person
details = Person("Toyota", 2020, "Pankaj", 2012)

# Access methods
details.print_details() 
details.display()        