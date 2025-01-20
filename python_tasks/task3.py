"""
    Description:
    Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list.
"""

def get_common_element(list1,list2):
    """function to get the common element from 2 list by creating the new list and comparing the elements of the list, if they are equal than append them in list"""
    list3 = [item for item in list1 if item in list2]
    return list3

print("Enter a list 1, separated by spaces:")
user_input_list1 = input()
list1 = list(map(int, user_input_list1.split()))
print("List 1 is:",list1)  # printing list 1

print("Enter a list 2, separated by spaces:")
user_input_list2 = input()
list2 = list(map(int, user_input_list2.split()))
print("List 2 is:",list2)  # printing list 2

print(get_common_element(list1,list2))  #calling the function to find the common elements in both list