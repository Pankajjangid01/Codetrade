"""
call by value: When we pass the immutable variables to the function then it shows the call by vlaue behavior 
               Any change made to the variable inside the function will not reflect the variable outside the function
"""

def valuefunction(list1):
    """ here List1 is the local variable which has object refrence to the list so on deleting list1 will delete the refrence to the object not the originial list"""
    del list1   

list = ['python', 'c++', 'c', 'java', 'c#']

print(valuefunction(list))  
print("after function call",list)  



