"""
    Description: Sort a shuffled list of 10 random number in descending order
    Time comoplexity- O(n^2)
"""

def sortlist(shuffled_list, size):
    # Check if the list is already sorted
    if shuffled_list != sorted(shuffled_list):
        print("The list is unsorted. Sorting the list now...")
    else:
        print("The list is already sorted.")

    # Bubble Sort Logic
    for item in range(size):
        for number in range(size - item - 1):
            if shuffled_list[number] < shuffled_list[number + 1]:  # checks if the number is lesser then its next number
                shuffled_list[number], shuffled_list[number + 1] = shuffled_list[number + 1], shuffled_list[number]  # swap the numbers 
            if item > 0 and shuffled_list[size-item] == shuffled_list[size-item-1]:
                del shuffled_list[size-item]  # delete the duplicate item from the list 
                size -= 1 # every time decrease lenght of list when element is removed
    print("Sorted list After Duplicate removals:", shuffled_list)


print("Enter a list, separated by spaces:")
user_input = input()
shuffled_list = list(map(int, user_input.split()))
# Validate the input
if all(1 <= num <= 10 for num in shuffled_list):
    size=len(shuffled_list)
    print("Even elements from the list:", sortlist(shuffled_list))
else:
    print("Please enter numbers only between 1 and 10.")
