"""
    Description: Get the first 5 elements of list, string and tuple
"""

def get_list_element(my_list):
    """splice the list upto 5 to get the first 5 elements"""
    for item in range(len(my_list)):
        if item <5:
            print(my_list[item], end = ' ')

    # return my_list[:5]

def get_tuple_element(my_tuple):
    """return the first five element of tuple"""
    for item in range(len(my_tuple)):
        if item <5:
            print(my_tuple[item], end = ' ')
    # return my_tuple[:5]

def get_set_elements(my_set):
    """return the first five element of set"""
    for element in my_set:
        if element < 6:
            print(element, end=" ")  

def get_last_character(string):
    return string[:5]
my_list = [1,2,3,4,8,5,6,2,7]
print("First five element of the list:")
get_list_element(my_list)

my_tuple = (8,2,5,3,4,6)
print("\nFirst five element of the Tuple:")
get_tuple_element(my_tuple)

my_set = {9,4,5,6,2,0,4,3}
print("\nFirst five element of the Set:")
get_set_elements(my_set)

print("\nFirst five element of the String:")
string = "Coding"
print(get_last_character(string))