"""
Class: A Class is like an object constructor, or a "blueprint" for creating objects.
       To create a class we use "class" keyword
"""

#class creation
class MyClass:
    name="This is first class"

obj=MyClass()  #created object of MyClass
print(obj.name) #Accessing class property


# __init__() -->All classess have __init__ function, which is always executed when class is initaited
class Solve:
    # def __init__(self,name,age):   #__init__ function assign memory to class
    #     """self if the reffrence to the current object of the class and use to assign values to the properties of class"""
    #     self.name=name             #assinging value to the name 
    #     self.age=age               #assigning value to the age
    def fun(self):
        return "helo"
solveobj=Solve()        #created object of Solve class
# solveobj.age=22  #we can also update object properties
print(solveobj.fun())
import pdb
pdb.set_trace()

print(solveobj.name)  #accessing the name property
print(solveobj.age)   #accessing the age property

del solveobj.age # we can delete object property 
# print(solveobj.age)  #now it will give error 
         
#__str__()--> this function controls what should be returned when the class object is represented as string 
class StringClass:
    def __init__(self,id,name):    #__init__ function to assign values for name and id
        self.id=id                 #assigning value to the id 
        self.name=name             #assinging the value to the name  
    def __str__(self):             #creating the __str__ function 
        return f"{self.name}({self.id})"  #return the name and id 
    
strobj=StringClass(4,"Rahul")      #object creation of the StringClass
print(strobj)
print(strobj.name)
print(strobj.id)


#object methods
class Greet:
    def __init__(self,name):
        self.name=name   #assigning value to the name
    def hello(self,id):   
        self.id=id
        print(f"Hello {self.name}@{self.id}")

greetobj=Greet("Pankaj")
greetobj.hello(320)  #called function of class using object of the class 



#pass statement
class Empty:
    pass   #class definition can not be empty, if we dont have any content to write in the class then we can write "pass" to avoid error  


# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehical:
    def __init__(self,milage,max_speed):
        self.milage=milage
        self.max_speed=max_speed

car=Vehical("30kmph",200)
print(car.max_speed,car.milage)
