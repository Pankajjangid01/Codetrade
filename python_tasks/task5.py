"""
    Description:x=(1,2,3,4,5), y=(4,5,6,7). Combine these two tuples in a single tuple ignoring the
                common elements.
"""

def combine_tuple(tuple1,tuple2):
    """function to merge tuples ignoring duplicates """
    for number in tuple2:
        if number not in tuple1:  #check is tuple 2 element is present in tuple 1 or not 
            tuple1.append(number)  # append the element of tuple 2 to tuple1 if not present 
    return tuple(tuple1)

tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7)
print(combine_tuple(list(tuple1),list(tuple2)))