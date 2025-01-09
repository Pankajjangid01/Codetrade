mydict={
    "id":1,
    "name":"pankaj",
    "email":"pankajjangir1034@gmail.com",
    "password":"Pankaj@123"
}
copied=mydict.copy()
# print(copied)
copied1=dict(mydict)
# print(copied1)

# nested dictionary
maindict={
    "dict1":{
        "name":"pankaj",
        "year":2003
    },
    "dict2":{
        "name":"naman",
        "year":2010
    },
    "dict3":{
        "name":"rahul",
        "year":2002
    }
}
# print(maindict["dict2"]["name"])  #accessing nested dictionay 

# looping through a dictionary, we can use items() method
for item,initem in maindict.items():
    print(item)
    for newitem in initem:
        print(newitem+" ",initem[newitem])