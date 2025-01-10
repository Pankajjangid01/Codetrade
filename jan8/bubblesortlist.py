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
def compare(char1,char2):
    """
    if first character of char1 is greater than first character of char2 then it will return 1
    if first character of char2 is greater than first character of char1 then it will return -1
    """
    return ( (char1<char2) - (char1>char2) )   

def sortlist(mylist,size):
    """
    1.compairing each string in the compare function, it will return value 1,-1 or 0
    2.if the value is less then zero then swapping will be done and The sorted list will be in ascending order  
    3.If we want to get the list in descending order then we have to change the condition greater than 0 i.e compare()>0
    """
    #using bubble sort 
    temp = " "


    for index in range(size-1):  
        for character in range (index+1,size):  
            if compare( mylist[index],  mylist[character] ) < 0:  # Called the compare function passing inner loop and outer loop index value from list 
                temp = mylist[character]         
                mylist[character] = mylist[index]   
                mylist[index] = temp 
            
            if index > 0 and fruits[index] == fruits[size-index-1]:
                import pdb
                pdb.set_trace()
                del fruits[index]  
                size -= 1  # every time decrease lenght of list when element is removed

    return print("sorting strings after duplicate removal", mylist)

mylist = ["Pankaj", "Pawan", "Ajay", "Shashank", "Ajay", "Chinu"]
n = len(mylist)   
sortlist(mylist,n)  
print(mylist)

