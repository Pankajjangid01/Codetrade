"""
    Description:Get the last element of the list, tuple and string.
"""

def get_last(list):
    """Function to get the last element from the list"""
    return list[-1]

def get_last_tuple(tuple):
    """ function to get the last element from tuple """
    return tuple[-1]

def get_last_character(string):
    return string[-1]

list = [1,5,2,3,4,6]
print("Last element of list:",get_last(list))

tuple = (5,4,8,3,1,0,2)
print("Last element of tuple:",get_last_tuple(tuple))

string = 'Hello'
print("last character of string:",get_last_character(string))