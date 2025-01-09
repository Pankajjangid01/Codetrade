"""
Call by Refrence: In python when we pass the mutable variables such as list,dictionary,set to the function then there object refrence is passed
                  so any changes made to the variable inside the function will also reflect outside the function 
"""

def refrencedfunction(mylist):
    mylist.append('gurgoan')  #appending new element in the list inside the function

mylist=['jaipur','delhi','noida','gujrat','Indore']
print("My list before function call",mylist)
refrencedfunction(mylist)  #function called 
print("My list After function call",mylist)  #Changes on list inside the function also reflect outside the function


