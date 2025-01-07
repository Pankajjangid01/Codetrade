# boolean data type
print(10>2)
print(2>10)
print(2==4)

# if statement condition return true or false 
a=20
b=39
if a>b:
    print("a is greater")
print("b is greater")

"""
1. any string is true except empty string
2. any number is true except 0
3. any list,tuple,set or dictionary is true, except empty ones
"""
country=["INDIA","AUSTRALIA","USA"]
print(bool(country))
countrycode=[]
print(bool(countrycode))

