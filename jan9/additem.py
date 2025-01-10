mydict={
    "car":"Mahindra",
    "year":2020,
    "milage":50,
    "owner":["aman",'raman']
}
mydict["condition"] = "Best"  # add new item to dictionary
print(mydict)

mydict.update({"tyre":"MRF"})  # here update() method item if it is not present in dictionary
print(mydict)

mydict["owner"].append("pankaj")
print(mydict)