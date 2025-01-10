"""
Recusrion: Recurion is a function which call itself
we define a base condtion in it when will the function return 
"""

def recursivefunction(num):
    if num > 0:
        result = num + recursivefunction( num-1 )  # add the value of num recursively and store in the result  
        return result
    else:
        result = 0
    return result

print("result=",recursivefunction(2))

# find factorial
def factorial(fact):
   if fact == 0 or fact == 1:  # if fact value is 0 or 1 then return 1
       return 1
   return fact * factorial( fact-1 )  # multiply fact value to its fact-1 value, recursively decreasing fact value 

print("factorial=",factorial(4))

# sum of natural numbers
def naturalsum(num):
    if num == 0:  # if number is 0 then reuturn 0
        return 0
    return num + naturalsum(num - 1)  # calculate and return the sum 

print("sum of natural numbers:",naturalsum(5))

# fibonaaci series
def fibonaaci(num):
    if num == 0:  # if number is 0 then return 0
        return 0
    if num == 1 or num == 2:  # if number is 1 or 2 then return 1 
        return 1
    return fibonaaci(num - 1) + fibonaaci(num - 2)  #recuresively call the function and add their value 

print("fibonacci series:")
for index in range (5):
    print(fibonaaci(index),end=" ")