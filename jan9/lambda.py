"""
Description: A lambda funtion is a small annonymous function that can have multiple arguments, but only have single expression
"""

number = lambda num:num + 10
print(number(9))

def multiply(value):
    return lambda digit : digit * value  # here the value is multiplied by the unkown number 

mynum = multiply(3)
print(mynum(10))