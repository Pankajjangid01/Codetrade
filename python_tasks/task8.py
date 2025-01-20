"""
    Description:Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's
                method.
"""
def get_dictionary(mydict):
    """ Function to get all the keys and values together and separately """
    print("Printing all the keys:")

    for key in mydict.keys():  # Use keys() method to print all keys of the dictionary
        print(key)

    print("Printing all the values:")
    for value in mydict.values():  # Use values() method to print values of the dictionary
        print(value)

    print("Printing all the keys and values:")
    for key, value in mydict.items():  # Use items() method to print both keys and values of the dictionary
        print(f"{key}: {value}")

# Take input dictionary from the user
user_input = input("Enter a dictionary (e.g., {'key1': 'value1', 'key2': 'value2'}): ")
try:
    my_dict = eval(user_input)  # Evaluate the user input to convert it into a dictionary
    if isinstance(my_dict, dict):  # Check if the input is a dictionary using isinstance method
        get_dictionary(my_dict)
    else:
        print("Input is not a valid dictionary.")

except (SyntaxError):
    print("Invalid dictionary format. Please use proper syntax.")