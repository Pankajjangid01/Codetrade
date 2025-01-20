"""
    Description:Print all the keys and values of a dictionary.
"""

def get_dictionary(mydict):
    """ function to get all the keys and values together and seperatly """

    print("Printing all the keys:")
    for key in mydict.keys():  # can use keys() method to print all keys of the dictionary
        print(key)   

    print("Printing all the values:")
    for value in mydict.values():  # can use values() method to print values of the dictionary
        print(value)

    print("printing all the keys and values:") 
    for key in mydict.items():  # items() method to print both values and keys of the dictionary as a tuple 
        print(key) 

my_dict = {'name':'pankaj','id':4,'Domain':"Odoo"}
get_dictionary(my_dict)