"""
Inheritance: Inheritance allow us to create a child class theat inherit all the methods and properties of its parent class 
"""

# class Vehical:
#     def __init__(self,milage,max_speed):
#         self.milage=milage
#         self.max_speed=max_speed

# class Car(Vehical):
#     pass
# gaadi=Car("30kmph",200)
# print(gaadi.max_speed,gaadi.milage)



# class Mahindra(Vehical):
#     def __init__(self, fname, lname):   #writing __init__ in the chile class will no longer inherit the properties of parent class it will overried inheritance
#         self.fname=fname
#         self.lname=lname
# gaadi2=Mahindra("30kmph",200)
# print(gaadi2.fname,gaadi2.lname)
# print(gaadi2.max_speed,gaadi2.milage)  #this will give error because we are inheriting the properties of Parent class with the object of child class


# class Scorpio(Vehical):
#     def __init__(self, fname, lname):   
#         Vehical.__init__(self,fname,lname) # to inherit the parents properties we have to add a call to parent's __init__
# gaadi3=Scorpio("30kmph",200)
# print(gaadi3.max_speed,gaadi3.milage) 


# super() function allow the child class to inherit all the mehtods and properties of parent class 
class College:
    def __init__(self,fname,lname,branch):
        self.fname=fname
        self.lname=lname
        self.branch=branch
    
    def printdetails(self):
        print("First name:",self.fname,"\nLast name:",self.lname,"\nBranch:",self.branch)
    
class Student(College):
    def __init__(self, fname, lname, branch,mobile):
        super().__init__(fname, lname, branch)
        self.mobile=mobile  #Adding new properrty in child class
#taking input from user
mobile=(input("Enter mobile no."))   
fname=(input("Enter Fist name:"))
lname=(input("Enter Last name:"))
Branch=(input("Enter Branch name:"))
studentobj=Student(fname,lname,Branch,mobile)
studentobj.printdetails()
print("Mobile No.",studentobj.mobile)