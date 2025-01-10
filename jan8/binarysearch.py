"""
1.Binary search: used to find the particular element from a collection of sorted elements
2. Time complexity:
    1.Best case: O(1)
    2.Average case: O(log n)
    3.Worst case: O(log n)
"""
def sortbubble(mylist, size):
    # Bubble Sort used to sort the unsorted list 
    for item in range(size):

        for number in range(size - item - 1):
            if mylist[number] > mylist[number + 1]:
                mylist[number], mylist[number + 1] = mylist[number + 1], mylist[number]
            
            if item > 0 and mylist[item] == mylist[item-1]:  #check 1st iteration value should >0 and value of item and item-1 value is equal or not 
                del mylist[item]  
                size -= 1  # every time decrease lenght of list when element is removed

def binary_search(mylist,brand):   
    start = 0                       
    end = len(mylist) - 1               
    mid = 0                         
    while start <= end:  # loop runs while start and end cross each other 
        mid=( start + end ) // 2        
        if mylist[mid] == brand:  # checking the mid value to the search value
            return mid            
        elif mylist[mid] > brand:  # checking element is smaller then mid element or not and search in the left part
            end = mid - 1             
        else:
            start = mid + 1  # if element is larger then mid element then we search in the right part
    return -1

mylist=[2,4,1,1,2,9,0,2,3]    
size=len(mylist)

sortbubble(mylist,size)
key = 2  # search key                           

index = binary_search(mylist, key)
print(f"{key} if found at:", index)
