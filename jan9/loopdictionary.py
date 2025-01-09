mydict={
    "car":"Mahindra",
    "year":2020,
    "milage":50,
    "owner":["aman",'raman']
}



for key in mydict: 
    print(key,end=" ")   #print all key name one by one

for key in mydict: 
    print(mydict[key])   #print all value one by one


for key in mydict.values():  #can use values() method to print values of the dictionary
    print(key)   #print all value one by one


for key in mydict.keys():  #can use keys() method to print all keys of the dictionary
    print(key)   #print all key one by one



for key in mydict.items():  # items() method to print both values and keys of the dictionary as a tuple 
    print(key) 
