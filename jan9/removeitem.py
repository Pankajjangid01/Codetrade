mydict={
    "id":1,
    "name":"pankaj",
    "email":"pankajjangir1034@gmail.com",
    "password":"Pankaj@123"
}

mydict.pop("password")  # remove the item with specific key value
print(mydict) 

mydict.popitem() # remove the last inserted item in the dictionary
print(mydict)

del mydict["password"]  # remove the item with specific key value or we can also completeley delete the dictionary
print(mydict)

mydict.clear() #clear the dictionary and makes it empty
print(mydict) 

