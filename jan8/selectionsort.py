"""
Selection sort: The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part 
                and putting it at the beginning. 
Time complexity:
    1.Best case: O(n^2)
    2.Average case: O(n^2)
    3.Worst case: O(n^2)        
"""
def selectionsort(arr):                         
    for index in range(len(arr)):    # iterate the list from 0 to the lenght of list 
        current=index                #stored the current index 
        for num in range(index+1,len(arr)):  #loop to iterate from index+1 value to lenght of the list
            if arr[current]>arr[num]:        #checking if the current vlaue of list is grater than then the next elements
                arr[current],arr[num]=arr[num],arr[index]   # Swap if the current value is larger than the next elements
            
arr=[5,2,3,7,9,4,1,0]    #created list array
selectionsort(arr)       #called the selection sort function by passing arr as argument  
print(arr)