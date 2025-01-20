def get_even_element(my_list):
    """Function to get only the even numbers of the list"""
    my_even_list = [element for element in my_list if element % 2 == 0]
    return my_even_list

# Ask the user for input
print("Enter a list of numbers from 1 to 20, separated by spaces:")
user_input = input()
my_list = list(map(int, user_input.split()))

# Validate the input
if all(1 <= num <= 20 for num in my_list):
    print("Even elements from the list:", get_even_element(my_list))
else:
    print("Please enter numbers only between 1 and 20.")