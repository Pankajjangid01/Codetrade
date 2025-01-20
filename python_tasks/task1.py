"""
    Description: Get the first 5 elements of list, string and tuple
"""

def get_list_element(my_list):
    """splice the list upto 5 to get the first 5 elements"""
    for item in range(len(my_list)):
        if item <5:
            print(my_list[item], end = ' ')

def get_tuple_element(my_tuple):
    """return the first five element of tuple"""
    for item in range(len(my_tuple)):
        if item <5:
            print(my_tuple[item], end = ' ')

def get_last_character(string):
    return string[:5]

print("Enter a list, separated by spaces:")
user_input = input()
my_list = list(user_input.split())

print("First five element of the list:")
get_list_element(my_list)

print("\nEnter a tuple, separated by spaces:")
user_input = input()
my_tuple = list(user_input.split())
print("\nFirst five element of the Tuple:")
get_tuple_element(my_tuple)

print("\nFirst five element of the String:")
string = input("Enter the string:")
print(get_last_character(string))