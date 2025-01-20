"""
    description: Get a list of 1 to 20 then remove elements from list to get only even elements.
"""

def get_even_element(my_list):
    """function to get only the even number of the list"""
    my_even_list = [element for element in my_list if element % 2 == 0 ]
    return my_even_list

my_list = [1,4,5,6,3,2,7,9,8,10,14,15,12,17,13,18,20,19,16,11]
print(get_even_element(my_list))