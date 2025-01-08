"""
1.Binary search: used to find the particular element from a collection of elements
2.Applied only on sorted data
3.We have to find the mid of the list and then compare our element to the mid element, if it equal to mid then we return the mid
  if mid element is not equal to our element then we compare whether it is smaller then mid element or larger
  if it is smaller then mid element then we search in the left part otherwise we search in right part
4. Time complexity:
    1.Best case: O(1)
    2.Average case: O(log n)
    3.Worst case: O(log n)
"""

def binary_search(mylist,brand):
    start=0
    end=len(mylist)-1
    mid=0
    while start<=end:
        mid=(start+end)//2
        if mylist[mid]==brand:
            return mid
        elif mylist[mid]>brand:
            end=mid-1
        else:
            start=mid+1
    return -1
mylist=[2,4,1,9,0,3]
key=0
index=binary_search(mylist,key)
print(f"{key} if found at:",index)


#binary search on strings 
# def binary_search(mylist,brand):
#     start=0
#     end=len(mylist)-1
#     mid=0
#     while start<=end:
#         mid=(start+end)//2
#         item=mylist[mid]
#         if item==brand:
#             return mid
#         elif item>brand:
#             end=mid-1
#         else:
#             start=mid+1
#     return -1
mylist=['banana','papaya','mango']
fruit='papaya'
index=binary_search(mylist,fruit)
print(f"{fruit} if found at:",index)