"""
Bubble sort: repeatedly swap the adjacent elements if they are in wrong order 
Time complexity: 
    1.Best case- O(n) "if the list is already sorted"
    2.Average case- O(n^2)
    3.Worst case- O(n^2)
"""

# Bubble sort using function
def sortbubble(fruits, size):
    # Check if the list is already sorted
    if fruits != sorted(fruits):
        print("The list is unsorted. Sorting the list now...")
    else:
        print("The list is already sorted.")

    # Bubble Sort Logic
    for item in range(size):
        for number in range(size - item - 1):
            if fruits[number] > fruits[number + 1]:
                fruits[number], fruits[number + 1] = fruits[number + 1], fruits[number]
            if item > 0 and fruits[size-item] == fruits[size-item-1]:
                del fruits[size-item]  
                size -= 1 # every time decrease lenght of list when element is removed

    # Inform the user about the sorted list
    print("Sorted list After Duplicate removals:", fruits)


fruits = [1,5,2,3,8,4,6,2,7]
size=len(fruits)
sortbubble(fruits, size)  # Calling the bubble sort function

# Debugging with pdb
import pdb
pdb.set_trace()


# Sorting strings
def compare(char1, char2):
    """
    If the first character of char1 is greater than the first character of char2, it will return 1.
    If the first character of char2 is greater than the first character of char1, it will return -1.
    """
    return ( (char1 < char2) - (char1 > char2) )

def compare(char1, char2):
    """
    If the first character of char1 is greater than the first character of char2, it will return 1.
    If the first character of char2 is greater than the first character of char1, it will return -1.
    """
    return (char1 > char2) - (char1 < char2)

def sortlist(mylist, size):
    """
    Sorting using bubble sort and removing duplicates during the sorting process.
    """
    temp = " "
    index = 0

    while index < size - 1:
        character = index + 1
        while character < size:
            # Compare the elements
            if compare(mylist[index], mylist[character]) < 0:
                temp = mylist[character]
                mylist[character] = mylist[index]
                mylist[index] = temp
            # Remove duplicates
            elif mylist[index] == mylist[character]:
                del mylist[character]
                size -= 1  # Decrease the size of the list
                continue  # Recheck the current position
            character += 1
        index += 1

    return mylist

# Test the function
mylist = ["Pankaj", "Pawan", "Ajay", "Shashank", "Ajay", "Chinu", "Chinu", "Rohit", "Ajay", "Vikas"]
n = len(mylist)
sorted_unique_list = sortlist(mylist, n)
print("Sorting strings after duplicate removal:", sorted_unique_list)