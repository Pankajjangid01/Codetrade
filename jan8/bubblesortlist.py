"""
Bubble sort: repeatedly swap the adjacent elements if they are in wrong order 
Time complexity: 
    1.Best case- O(n) "if the list is already sorted"
    2.Average case- O(n^2)
    3.Worst case- O(n^2)
"""

# Bubble sort using function
def sortbubble(fruits):
    for item in range(len(fruits)):                                     #iterate over the list from 0 to the lenght of list 
        for number in range(item+1,len(fruits)):                        #iterate over the list from item+1 i.e 1 to lenght of the list 
            if fruits[item]>fruits[number]:                             #check if the value of item is greater than fruit or not 
                fruits[item],fruits[number]=fruits[number],fruits[item] #if it is grater than swap them 
        if item>2 and fruits[item]==fruits[item-1]:                     #check if item value>0 and value of fruit is equal to previous fruit
            del fruits[item]                                           #Mark it None if equal
fruits=[1,6,2,1,9,3,7,5]
sortbubble(fruits)                                           #calling the bubble sort function
print("sorting in the function",fruits)
import pdb
pdb.set_trace()


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
    for index in range(size-1):  #outer loop which start from 0 to size-1 of the list 
        for character in range (index+1,size):  #inner loop which start from index+1 i.e 1 to size of the list 
            if compare(mylist[index],mylist[character])<0:   #called the compare function passing inner loop and outer loop index value from list 
                """
                1.compairing each string in the compare function, it will return value 1,-1 or 0
                2.if the value is less then zero then swapping will be done 
                3.The sorted list will be in ascending order  
                4.If we want to get the list in descending order then we have to change the condition greater than 0 i.e compare()>0
                """
                temp=mylist[character]          #copy the inner loop list value to temporary vairable 
                mylist[character]=mylist[index]   #copy the outer loop list index value to inner loop value 
                mylist[index]=temp               #again the temporary variable value to the outer loop index 
    for number in range(0,size-2):      #loop to iterate from 0 to seize-2 beacuse list should not go out of the index
        if mylist[number]==mylist[number+1]:  #checking the number is equal to the next number or not
            del mylist[number]    #if the number are equal delete the the one number

mylist=["Pankaj","Pawan","Ajay","Shashank","Ajay","Chinu"]
mylist=list(set(mylist))
n=len(mylist)   #lenght of the list 
sortlist(mylist,n)  #called sortlist function by passing mylist and n  as the parametes
print("sorting strings after duplicate removal",mylist)


