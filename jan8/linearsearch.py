"""
Linear search: linear search is used to find the element from the collection of sorted elements 
Time complexity:
    1. Best case: O(1)
    2. Average case: O(n)
    3. Worst case: O(n)
"""

def linear_search(searchlist,key):   
    for number in range(len(searchlist)):  #iterate over the list from 0 to the lenght of list 
        if(searchlist[number]==key):   #checking the key is equal to current value or not
            return number    # if equal then return the index 
    return -1   #if not finde the key then return -1

# Linear search using functions
def sortbubble(name):
    for item in range(len(name)):  #iterate over the list from 0 to the lenght of list 
        for number in range(item+1,len(name)):  #iterate over the list from item+1 to the lenght of list 
            if name[item]<name[number]:  #checking the outer loop value to the inner loop value greater or not
                name[item],name[number]=name[number],name[item]   #if grater than swap them 

name=["Pankaj","Rahul","Ajay","Ajay","Mohit"]
key="Ajay"
fruits=list(set(name))  #removed the duplicates using set 
sortbubble(name)  #called the sort function passing name list as argument
print("Key is found at:",linear_search(name,key))  #called the linear search function passing name list and key as arguments  
print(name)