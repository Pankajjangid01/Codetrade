"""
call by value: When we pass the immutable variables to the function then it shows the call by vlaue behavior 
               Any change made to the variable inside the function will not reflect the variable outside the function
"""

def valuefunction(list1):
    del list1
list=('python','c++','c','java','c#')
print("Before funtion call",list)
valuefunction(list)
print("after function call",list)