"""
Linear search: linear search is used to find the element from the collection of elements 
It is only applied on the sorted elements 
If the elemnts are not sorted, first we have to sort them and then we can apply linear search on them 
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
searchlist=[1,2,3,4,5] 
key=3
print("Key is found at:",linear_search(searchlist,key))

#Linear search on Strings

def linear_search(searchlist,fruit):
    for number in range(len(searchlist)):
        if(searchlist[number]==fruit):
            return number
    return -1
searchlist=["orange","mango","banana","kiwi","papaya","graphs"] 
fruit="papaya"
print(f"{fruit} is found at:",linear_search(searchlist,fruit))