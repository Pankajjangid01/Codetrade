"""
Dictionary: A dictionary is collection of ordered and unique key value elements and they are changeable 
"""

dict1 = {
    "id":1,
    "name":"pankaj",
    "number":123,
    "number":1234 # key should be different name, same name key overwrite the previous key value
}
print(dict1)
print(len(dict1)) # lenght of dictionary


# dict() constructor to create dictionary
thisdict = dict( name="pankaj", id=1, number=456 )
print("Constructed dictionary",thisdict)


# Accesing items from dictionary
item = thisdict["name"]  # accessing item using its key name 
print(item)

getitem = thisdict.get("number")
print(getitem)


keylist = thisdict.keys()  # return a list of all the keys in dictionary
print(keylist)


valuelist = thisdict.values()  # return a list of all the values in the dictionary
print(valuelist)

allitems = thisdict.items()  # return each item in a dicitonary as a tuple
print(allitems)


# determine if the key is present in dictionary or not 
if "name" in thisdict:
    print(thisdict.get("name"))