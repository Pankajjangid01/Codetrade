"""
Bubble sort: repeatedly swap the adjacent elements if they are in wrong order 
Time complexity: 
    1.Best case- O(n) "if the list is already sorted"
    2.Average case- O(n^2)
    3.Worst case- O(n^2)
"""

# Bubble sort using function
def sortbubble(fruits):
    for item in range(len(fruits)):
        for number in range(item+1,len(fruits)):
            if fruits[item]>fruits[number]:
                fruits[item],fruits[number]=fruits[number],fruits[item]
fruits=[1,6,2,1,9,3,7]
fruits=list(set(fruits))
sortbubble(fruits)
print(fruits)


# sorting the list after duplicate removal 
mylist1=[5,2,8,6,1,2,4,3]
mylist1=list(set(mylist1))
for number in range(len(mylist1)):
    for index in range(number+1,len(mylist1)):
        if mylist1[number]>mylist1[index]:
            mylist1[number],mylist1[index]=mylist1[index],mylist1[number]
print("My list after removing duplicates",mylist1)


########################################################################################################

# sorting string after duplicate removals
# Sorting strings 
def compare(char1,char2):
    """
    if first character of char1 is greater than first character of char2 then it will return 1
    if first character of char2 is greater than first character of char1 then it will return -1
    """
    return ((char1<char2)-(char1>char2))   

def sortlist(mylist,size):
    #using bubble sort 
    temp=""
    for index in range(size-1):
        for character in range (index+1,size):
            if compare(mylist[index],mylist[character])<0:
                """
                1.compairing each string in the compare function, it will return value 1,-1 or 0
                2.if the value is less then zero then swapping will be done 
                3.The sorted list will be in ascending order  
                4.If we want to get the list in descending order then we have to change the condition greater than 0 i.e compare()>0
                """
                temp=mylist[character]
                mylist[character]=mylist[index]
                mylist[index]=temp
    for number in range(0,size-2):   
        if mylist[number]==mylist[number+1]:
            del mylist[number]
mylist=["Pankaj","Pawan","Ajay","Shashank","Ajay","Chinu"]
mylist=list(set(mylist))
n=len(mylist)
sortlist(mylist,n)
print("sorting strings after duplicate removal",mylist)


# examples of call by refrence and varibles with example
# for loop inside the for loop to remove duplicates 
# doctype comments
# binary search and linear search using function

