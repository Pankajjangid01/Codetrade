"""
    Description:
    Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list.
"""

def get_common_element(list1,list2):
    """function to get the common element from 2 list by creating the new list and comparing the elements of the list, if they are equal than append them in list"""
    list3 = [item for item in list1 if item in list2]
    return list3

list1 = [1,2,3,4,5,6,7,8]
list2 = [4,5,6,7,8,9,10]
print(get_common_element(list1,list2))