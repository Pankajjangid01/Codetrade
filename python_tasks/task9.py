"""
    Description:Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries.
"""

def merge_dictionary(dict1,dict2):
    """Function to merge the two dictionaries"""
    # dict1.update(dict2)  # merge using update method 
    dict3 = dict1 | dict2  # merge dictionaries using | operator
    return dict3

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':4,'d':5,'e':6}
print(merge_dictionary(dict1,dict2))