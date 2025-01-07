# int(): convert values to integer
"""
s="10"
integerValue=int(s)
print(integerValue)
"""

#float(): convert values into floating point numbers
"""
num=10
f=float(num)
print(f)
"""

#str():convert any data type to string
"""
dec=10.02
st=str(dec)
print(st)
"""


#to check type of vriable use type()
"""
print(type(integerValue))
print(type(f))
print(type(st))
"""


'Local vairable --> scope of variable is only within the function'

"""
def f():
    name="pankaj"
    print(name)
f()
"""


'Global variable -->scope of variable is global and can be accessed anywhere using global keyword'

"""
a=10
def add():
    global a
    b=20
    a=a+b
    print("Value of B is:",b)
    print("Value of A is:",a)
add()
print(a)
"""

'object refernce'
x=5
y=x
x="Hello"  #creates a new object for the value "Hello" and makes x reference this new object. Y remain unchanged
y="world"  #create a new object for the value "world" and updtes y to reference it 
print(x,y)


'deleting a variable using del keyword'

name="pankaj"
print(name)
del name
print(name)