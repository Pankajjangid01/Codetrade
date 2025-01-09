mydict={
    "car":"Mahindra",
    "year":2020,
    "milage":50,
    "owner":["aman",'raman']
}

mydict["car"]="Tata" #update the value of car in dictionary
print(mydict)

mydict.update({"year":2025,"milage":78}) # update() method to update the values in dictionary
print(mydict)

mydict["owner"][1]="Pankaj"  #update the list value in dictionary
print(mydict)