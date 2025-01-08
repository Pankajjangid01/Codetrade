"""
Quick sort: It is one of the fastest sorting algorithm
            The Quicksort algorithm takes an array of values
            Choose one element as pivot element and moves other elements so that lower values comes to the left of the pivot and 
            higher values are on the right of it.
Time complexity: 
    1.Best case: O(n)
    2.Average case: O(n log n)
    3.Worst case: O(n^2)
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
    if start<end:
        pivotindex=partition(mylist,start,end)
        quicksort(mylist,start,pivotindex-1)
        quicksort(mylist,pivotindex+1,end)
mylist=[5,6,2,3,10,4,45,25,35]
quicksort(mylist,0,len(mylist)-1)
print(mylist)



# Taking first element as pivot 
def partition2(mylist,start,end):
    pivot=mylist[start]
    low=start+1
    high=end
    while True:
        while low<=high and mylist[high]>=pivot:
            high=high-1
        while low<=high and mylist[low]<=pivot:
            low+=1
        if low<=high:
            mylist[low],mylist[high]=mylist[high],mylist[low]
        else:
            break
    mylist[start],mylist[high]=mylist[high],mylist[start]
    return high
def quicksort2(mylist,start,end):
    if start<end:
        pivotindex=partition2(mylist,start,end)
        quicksort2(mylist,start,pivotindex-1)
        quicksort2(mylist,pivotindex+1,end)
mylist=[5,6,2,3,10,4,45,25,35]
quicksort2(mylist,0,len(mylist)-1)
print(mylist)
