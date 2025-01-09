"""
Call by Refrence: In python when we pass the mutable variables such as list,dictionary,set to the function then there object refrence is passed
                  so any changes made to the variable inside the function will also reflect outside the function 
"""

def refrencedfunction(mylist):
    mylist.append('gurgoan')
mylist=['jaipur','delhi','noida','gujrat']
print("My list before function call",mylist)
refrencedfunction(mylist)
print("My list After function call",mylist)