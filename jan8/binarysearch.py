"""
1.Binary search: used to find the particular element from a collection of sorted elements
2. Time complexity:
    1.Best case: O(1)
    2.Average case: O(log n)
    3.Worst case: O(log n)
"""
def sortbubble(mylist):                                                   #used bubble sort to sort the list 
    for item in range(len(mylist)):                                       #iterate over the list from 0 to the lenght of list 
        for number in range(item+1,len(mylist)):                          #iterate over the list from item+1 i.e 1 to lenght of the list 
            if mylist[item]>mylist[number]:                               #check if the value of item is greater than number or not 
                mylist[item],mylist[number]=mylist[number],mylist[item]   #if it is grater than swap them 


"""Binary search to search the element """
def binary_search(mylist,brand):  # mylist,brand are the parameters 
    start=0                       #taken a pointer start at 0 index
    end=len(mylist)-1             #taken a pointer end at last  
    mid=0                         # initialized a varible mid with 0
    while start<=end:             #loop runs while start and end cross each other 
        mid=(start+end)//2        # We have to find the mid of the list and then compare our element to the mid element
        if mylist[mid]==brand:    #checking the mid value to the search value
            return mid            # if search value and mid value are equal than return mid 
        elif mylist[mid]>brand:   # checking element is smaller then mid element or not 
            end=mid-1             # searching in the left part
        else:
            start=mid+1           #if element is larger then mid element then we search in the right part
    return -1
mylist=[2,4,1,1,2,9,0,2,3]        #created a list of name mylist
mylist=list(set(mylist))          #convert the list into set to remove duplicates and then again convert it into list
# print("My list after removing duplicates",mylist)
sortbubble(mylist)                #calling bubble sort function
key=2                            
index=binary_search(mylist,key)
print(f"{key} if found at:",index)
