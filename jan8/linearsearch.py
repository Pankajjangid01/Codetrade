"""
Linear search: linear search is used to find the element from the collection of sorted elements 
Time complexity:
    1. Best case: O(1)
    2. Average case: O(n)
    3. Worst case: O(n)
"""

# Linear search using functions
def linear_search(searchlist, key):   
    for number in range(len(searchlist)):  
        if( searchlist[number] == key ):  # checking the key is equal to current value or not, if equal then return the index
            print(f"key is found at {number}")     
    return -1  # if can not find the key then return -1

def sortbubble(name,size):
    """used bubble sort function to sort the list if it is not in the sorted order"""
    for item in range(size):
        for number in range(size - item - 1):
            if name[number] > name[number + 1]:
                name[number], name[number + 1] = name[number + 1], name[number]
            
            if item > 0 and name[size-item] == name[size-item-1]:
                del name[size-item]  
                size -= 1  # every time decrease lenght of list when element is removed
name=[1,5,2,3,8,4,6,2,7]
size=len(name)
sortbubble(name,size) 
key=2 
linear_search(name,key)    
