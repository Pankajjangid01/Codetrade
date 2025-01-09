"""
Linear search: linear search is used to find the element from the collection of sorted elements 
Time complexity:
    1. Best case: O(1)
    2. Average case: O(n)
    3. Worst case: O(n)
"""

def linear_search(searchlist,key):
    for number in range(len(searchlist)):
        if(searchlist[number]==key):
            return number
    return -1
# searchlist=[1,2,3,4,5] 
# key=3
# print("Key is found at:",linear_search(searchlist,key))


# Linear search using functions

def sortbubble(name):
    for item in range(len(name)):
        for number in range(item+1,len(name)):
            if name[item]>name[number]:
                name[item],name[number]=name[number],name[item]
name=["Pankaj","Rahul","Ajay","Ajay","Mohit"]
key="Ajay"
fruits=list(set(name))
sortbubble(name)
print("Key is found at:",linear_search(name,key))
print(name)