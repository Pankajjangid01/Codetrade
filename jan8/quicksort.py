"""
Quick sort: Choose one element as pivot element and moves other elements along the pivot so that lower values comes to the left of the pivot and 
            higher values are on the right of it.
Time complexity: 
    1.Best case: O(n)
    2.Average case: O(n log n)
    3.Worst case:O(n^2)
"""

def partition(mylist,start,end):
    pivot=mylist[end]  #last element as pivot 
    index=start-1
    for item in range(start,end):
        if mylist[item]<pivot:  # checking each element whether it is smaller than pivot or not 
            index+=1   # increment the index -1 to 0 and so on
            mylist[index],mylist[item]=mylist[item],mylist[index]  #swapping the values of index and item 
        
    mylist[index+1],mylist[end]=mylist[end],mylist[index+1]  # when the item reach the last element swap the last element i.e pivot element to the next of index 
    return index+1

def quicksort(mylist,start,end):
    if start<end:     #check the condition start is lesser than end
        pivotindex=partition(mylist,start,end)  #finde the pivot index by calling partition function
        quicksort(mylist,start,pivotindex-1)  #recursive call before the pivot index i.e left part
        quicksort(mylist,pivotindex+1,end)   #recursive call after the pivot index i.e right part

mylist=[5,6,2,3,10,4,45,25,35]
quicksort(mylist,0,len(mylist)-1)  #called the quick sort function passing list ,start index 0 and end index value 
print(mylist)



