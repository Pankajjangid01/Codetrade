"""
Call by Refrence: In python when we pass the mutable variables such as list,dictionary,set to the function then there object refrence is passed
                  so any changes made to the variable inside the function will also reflect outside the function 
"""

def refrencedfunction(mylist):
    mylist.append('gurgoan')  # appending new element in the list inside the function


#1. adding element to list
mylist = ['jaipur', 'delhi', 'noida', 'gujrat', 'Indore']
refrencedfunction(mylist)  
print("My list After function call",mylist)  # Changes on list inside the function also reflect outside the function


#2. updating list element
def update_list(list1):
    list1[0] = 'JJN'

list1 = ['kota', 'jaipur', 'sikar']
update_list(list1)
print(list1)


#3. Extend list
def extend_list(list2):
    list2.extend(['Gurgaon', 'Kolkata', 'Mumbai'])

list2 = ['Jaipur', 'Delhi']
extend_list(list2)
print(list2)

#4. Removing element from list 
def remove_list(list3):
    list3.remove(5)

list3 = [1,5,3,4,8,6]
remove_list(list3)
print(list3)


#5. updating element in dictionary
def dictfunction(mydict) :
    mydict["Brand"]="Iphone"

mydict = {"Key":1,"item":"Phone","Brand":"Samsung"}
dictfunction(mydict)
print(mydict)


#6. adding element in dictionary
def additem(newdict):
    newdict["grade"]="A"

newdict = {"id":1,"name":"Pankaj","marks":354}
additem(newdict)
print(newdict)

#7.remove element from dictionary
def remove_item_dictionary(dict2):
    dict2.pop("password")

dict2 = {"fname":"Pankaj","lname":"Kumar","password":"pankaj@123"}
remove_item_dictionary(dict2)
print(dict2)

#8. Clear List
def clear_list(list4):
    list4.clear()

list4 = [8,2,6,"aman",5]
clear_list(list4)
print(list4)

#9. Clear dictionary
def clear_dictionary(dict3):
    dict3.clear()

dict3={"email":"pankajjangir1034@gmail.com","phone no.":64513397}
clear_dictionary(dict3)
print(dict3)

# 10 Slice the list inside function
def get_item(list5):
    print(list5[1:3])

list5 = [1,2,3,4,5]
get_item(list5)
