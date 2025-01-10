# Operators - used to perform operations on variable or value
"""
Types of operator
1. Arithmetic operators
2. Assignment operators
3. Logical operators
4. Bitwise operators
5. Comparison operator 
6. Identity operator 
7. Membership operator
 """


num1=2
num2=3

# Arithmetic operations
print(num1 + num2)  # addition
print(num2 - num1)  # subtraction
print(num1 * num2)  # multiplication
print(num2 / num1)  # division
print(num2 ** num1)  # exponential 
print(num2 % num1)  # modulus
print(num2 // num1)  # floor division

# assignment operators
num1 += num2  # num1 = num1 + num2
print("Value of num1 is updated:",num1)

num2 -= num1 # num2 = num2 - num1
print("updated value of num2 is:",num2)

num2 = 5
num2 *= num1 # num2 = num2 * num1
print("after multiplying num2 to num1:",num2)

num2 /= num1 # num2 = num2 / num1
print("after dividing num2 by num1:",num2)

num2 = int(num2)  # type casted to integer value
num2 &= num1  # perform bitwise AND on operands and assign value to left operand 
print("After performing bitwise AND:",num2)

num1 = 3
num2 |= num1  # perform bitwise OR on operands and assign value to left operand 
print("After performing bitwise OR:",num2)

num2 ^= num1  # perform bitwise XOR on operands and assign value to left operand 
print("After performing bitwise X-OR:",num2)

num2 >>= num1  # perform bitwise right shift on operands and assign value to left operand 
print("After performing right shift:",num2)

num2 = 2
num1 <<= num2  # perform bitwise left shift on operands and assign value to left operand 
print("After performing left shift:",num1)

# Comparision operators -> return boolean value
value1 = 10
value2 = 20
value3 = 10.0
value4 = "10"
print(value1 == value2)  # Equal-> return false 
print(value1 == value3)  # return true 
print(value3 == value1)  # return true
print(value1 == value4)  # return false
print(value4 == value3)  # return false

print(value2 > value1)  # Greater Than ->return true
print(value1 < value2)  # Less Than ->return true
print(value1 >= value3)  # Greater than or equal to -> return true 
print(value2 <= value1)  # Less than or equal to ->return false
print(value2 != value4)  # Not equal -> return true


# Logical operators 

print(value1 < 50 and value2 < 30)  # and- return true of both statements are ture
print(value1 > 10 or value2 < 50)  # or- return true is atleat one statements is true 
print(not (value1 < 50 and value2 < 30))  # not- reverse the result, if result is true then it will return false 


# Identity Operators 
fruits = ['Apple',"Banana","Orange","Mango"]
bucket = ["Apple","Banana","Orange"]
cart = fruits
print(fruits is cart) # return true because cart has same object as fruits
print(fruits is bucket) # return false because both have different object 
print(fruits is not bucket) # return true because both have different object


# Membership operators 
print('Banana' in fruits) # return true because "Bannan" is in the fruits list 
print('Mango' not in bucket) # return true because "Mango" is not in the bucket list


# Bitwise Operators 
num3 = 5
num4 = 2
print( num3 & num4 )  # AND->set each bit to 1 if both bit are 1 
print( num3 | num4 )  # OR->set each bit to 1 if any of the bit is 1
print( num3 ^ num4 )  # XOR->set each bit to 1 if only one bit is 1
print( num3 << num4 )  # zero fill left shift->bitwise left shift-->Shifts the bits of the number to the left and fills 0 on voids right as a result
print( num3 >> num4 )  # signed right shift->bitwise right shift-->Shifts the bits of the number to the right and fills 0 on voids left as a result
print( ~num3)  # NOT->Inverts all the bits


# Operator precedence
"""
1. paranthesis-()
2. Exponentiation- **
3. Unary plus, unary minus, and bitwise NOT- +*,-*,~*
4. Multiplication, division, floor division, and modulus- *, /, //, %
5. addition and subtraction- +,-
6. Bitwise left and right shift- <<,>> 
7. Bitwise AND- & 
8. Bitwise XOR- ^
9. Bitwise OR- |
10. Comparisons, identity, and membership operators- ==, >, <, >=, <=, !=,is,is not,in, not in
11. Logical NOT- not
12. AND- and
13. OR- or 
"""

