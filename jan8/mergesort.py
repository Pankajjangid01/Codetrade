"""
Merge sort: It works by recursively dividing the input array into smaller subarrays and
            sorting those subarrays then merging them back together to obtain the sorted array.
Time complexity:
    1.Best case: O(n)
    2.average case: O(log n)
    3.Worst case: O(log n)
"""
def merge(arr, start, end ):
    mid = ( start + end ) // 2
    leftsize = mid - start + 1  
    rightsize = end - mid    
    leftarr = [0] * leftsize  # Created a left array of leftsize
    rightarr = [0] * rightsize  # Created a right array of rightsize

    # Copy elements to left array
    copyindex = start
    for i in range(leftsize):
        leftarr[i] = arr[copyindex]
        copyindex += 1
    
    # Copy elements to right array
    copyindex=mid+1
    for i in range(rightsize):
        rightarr[i] = arr[copyindex]
        copyindex += 1
    
    # Merge left and right arrays back into original array
    leftindex = 0
    rightindex = 0
    mainarrayindex = start

    while leftindex < leftsize and rightindex < rightsize:
        if leftarr[leftindex] < rightarr[rightindex]: # checks value of left array is smaller than right array or not
            arr[mainarrayindex] = leftarr[leftindex]  # if the value of left array is smaller then copy it at the main array 
            leftindex += 1
        else:
            arr[mainarrayindex] = rightarr[rightindex]  # othewies copy right array value 
            rightindex += 1
        mainarrayindex += 1

    # Copy remaining elements of left array
    while leftindex < leftsize:
        arr[mainarrayindex] = leftarr[leftindex]
        leftindex += 1
        mainarrayindex += 1

    # Copy remaining elements of right array
    while rightindex < rightsize:
        arr[mainarrayindex] = rightarr[rightindex]
        rightindex += 1
        mainarrayindex += 1

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

def merge_sort(arr, start, end):
    if start < end:
        mid = ( start + end) // 2
        merge_sort( arr, start, mid )  # Recursive call on left array
        merge_sort( arr, mid+1, end )  # Recursive call on right array
        merge( arr, start, end )   # Merge function to merge the elements in sorted order


arr = [1,9,8,4,5,5,7,6]
print("Before merge sort:", arr)
merge_sort(arr,0,len(arr) - 1)
print("After merge sort:")
print_list(arr)