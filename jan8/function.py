# function creation
#def keyword is used to create function
def myfunction():
    print("Function creation")

#only craeating function will not give any output we have to call it 
myfunction()  #function called 

# Passing arguments in the function
def printname(name):
    print(f"my name is {name}")

printname("Pankaj")

def multiple(name,email,age):   #passing multiple arguments 
    print(f"my name is {name} and i am {age} old.\nMy email id is {email}")
multiple("pankaj","pankajjangir1034@gmail.com",22)

# we can also pass arguments with key=value syntax
def keyvalue(child2,child3,child1):
    print(f"child1 is {child1}\nchild2 is {child2}\nchild3 is {child3}")
keyvalue(child3="raman",child1="aman",child2="baman")


# default parameter 
def countryname(country="India"):
    print(f"country name={country}")

countryname("USA")
countryname("UK")
countryname()
countryname("Australia")
countryname("Sweden")


# passing a list as an argument
def listfunction(food):
    for item in food:
        print(item)

foodlist=["Daal","Panner","Chapati","Naan"]
listfunction(foodlist)


# function with return value
def returnfunction():
    return "hello"
print(returnfunction())


"""
pass statement--> function definition cannot be empty
if it is empty it will give error so to ignore the error and we dont have content for the funtion we have to write pass in its body 
"""
def passfuntion():
    pass   