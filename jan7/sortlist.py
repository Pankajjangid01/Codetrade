# sorting the list alphabetically
thislist = ["red", "green", "blue", "black", "brown"]
thislist.sort()
print(thislist)

# sorting the list numerically
numericlist=[100,200,12,155,656,60]
numericlist.sort()
print(numericlist)

# sorting the list in descending order by doing "reverse=true"
numericlist.sort(reverse=True)
print(numericlist)

caselist=["Red", "green", "blue", "Black", "brown"]
caselist.sort() #["Black","Red", "blue","brown","green" ]  because sort() is case sensitive so it put the capital letters first 
print(caselist)  
caselist.sort(key=str.lower)
print(caselist)

caselist.reverse()  #reverse the current list 
print(caselist) 

############################################

"""
we cannot copy list by typing list2=list1 , because list2 refrence the list1 and any change made in list1 will automatically reflected in list2
so we use copy() method , list() method which is an in built method and using slice operator(:) 
"""
# copy()
list1=["apple", "banana", "cherry"]
list2=list1.copy()
print("Printing the copied list 2:",list2)

# list()
list1=["apple", "banana", "cherry","Mango"]
list2=list(list1)
print("\nPrinting the copied list 2 using list:",list2)

# using slice operator
list1=["apple", "banana", "cherry","Mango","kiwi"]
list2=list1[:]
print("\nPrinting the copied list 2 using slice operator:",list2)


##################################################

# Join list using +
number=[1,2,3,4]
alphabets=['A','B','C']
joinlist=number+alphabets
print("\nJoined the list using +:",joinlist)

# Join list using extend
number=[1,2,3,4]
alphabets=['A','B','C']
alphabets.extend(number)
print("\nJoined the alphabets list using extend method:",alphabets)

# Join list using append
for item in alphabets:
    number.append(item)
print("\nJoined the alphabets list using append method:",number)

