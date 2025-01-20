"""
    description: Get a list of 1 to 20 then remove elements from list to get only even elements.
"""

def get_even_element(my_list):
    """function to get only the even number of the list"""
    my_even_list = [element for element in my_list if element % 2 == 0 ]
    return my_even_list

print("Enter a list, separated by spaces:")
user_input = input()
my_list = list(map(int, user_input.split()))

print("Given list is:",my_list)
print("Even  numbers list:",get_even_element(my_list))