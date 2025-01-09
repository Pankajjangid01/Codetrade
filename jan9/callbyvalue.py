"""
call by value: When we pass the immutable variables to the function then it shows the call by vlaue behavior 
               Any change made to the variable inside the function will not reflect the variable outside the function
"""

def valuefunction(list1):
    del list1
# R&D on del in pass by value on list 
    # del list1  #deleting list inside the function will only delete list inside the function 

list=('python','c++','c','java','c#')
print("Before funtion call",list)
print(valuefunction(list))  #function called
print("after function call",list)  #Changes on list inside the function will not reflect outside the function