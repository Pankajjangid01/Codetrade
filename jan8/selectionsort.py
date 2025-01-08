"""
Selection sort: The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part 
                and putting it at the beginning. 
Time complexity:
    1.Best case: O(n^2)
    2.Average case: O(n^2)
    3.Worst case: O(n^2)        
"""
def selectionsort(arr):
    for index in range(len(arr)):
        current=index  
        for num in range(index+1,len(arr)):
            if arr[current]>arr[num]:
                arr[current],arr[num]=arr[num],arr[index]   #Swap the smaller value with larger value
            
arr=[5,2,3,7,9,4,1,0]
selectionsort(arr)
print(arr)