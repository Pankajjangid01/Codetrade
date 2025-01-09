"""
1.Binary search: used to find the particular element from a collection of sorted elements
2. Time complexity:
    1.Best case: O(1)
    2.Average case: O(log n)
    3.Worst case: O(log n)
"""
def sortbubble(mylist):   #used bubble sort to sort the list 
    for item in range(len(mylist)):
        for number in range(item+1,len(mylist)):
            if mylist[item]>mylist[number]:
                mylist[item],mylist[number]=mylist[number],mylist[item]
def binary_search(mylist,brand):
    start=0
    end=len(mylist)-1
    mid=0
    while start<=end:
        mid=(start+end)//2   # We have to find the mid of the list and then compare our element to the mid element
        if mylist[mid]==brand: #if element equal to mid value then we return the mid
            return mid
        elif mylist[mid]>brand: # if element is smaller then mid element then we search in the left part
            end=mid-1
        else:
            start=mid+1  #if element is larger then mid element then we search in the right part
    return -1
mylist=[2,4,1,1,2,9,0,2,3]
mylist=list(set(mylist))  #convert the list into set to remove duplicates and then again convert it into list
print("My list after removing duplicates",mylist)
sortbubble(mylist)
key=2
index=binary_search(mylist,key)
print(f"{key} if found at:",index)