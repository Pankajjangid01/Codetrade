mylist=['rhaul','rohit','virat','hardik']
print(mylist[-1]) #negative index means start from last i.e -1 means last element in the list
print(mylist[0:3]) #return a  list of specified items
print(mylist[:2]) #return a list from start to specified index where last index is exclusive
print(mylist[1:]) #return a list from specific index to last 
print(mylist[-4:-1]) # to access the items from the end 
if 'rohit' in mylist:
    print("rohit is present in mylist:",mylist)


# how to change value in list
newname='Rahul'
mylist[0]=newname #change a single item value
print(mylist)

mylist[1:3]=['Pankaj','Rishi'] #change a range of item values 
print(mylist)


# insert() method--> insert a new item in the list without replacing any existing item at a specific index
mylist.insert(2,"Rohit")
print(mylist)

# append()-->add item in the list at last 
mylist.append("Virat")
print(mylist)

# extend()-->to add elements of another list to the current list
newlist=['orange','apple','banana','kiwi']
mylist.extend(newlist)
print(mylist) 

colortuple=('red','green','blue')
mylist.extend(colortuple) # we can also add any iterable object such as set,tuple,dictionary,etc. 
import pdb
pdb.set_trace()
print(mylist)


# remove() method--> to remove the item from list
mylist.remove('blue')
print(mylist)

#pop(index)--> remove the element of particular index
mylist.pop(5)
print(mylist)

# pop()--> remove the last element of the list 
mylist.pop()
print(mylist)

# del()--> this also remove the specified index
del mylist[5]
print(mylist)

del mylist #delete the complete list 
# print(mylist)

mynewlist=['set','tuple','dictionary']
mynewlist.clear() #epmty the list
print(mynewlist)
mynewlist=['set','tuple','dictionary']

# Looping a list using for loop
for item in mynewlist:     
    print(item)


print("\nPrinting item through index number")
for item in range(len(mynewlist)):
    #loop through the index number 
    print(mynewlist[item])

# Looping a list using while loop
index=0
print("\nPrinting item though while loop")
while index<len(mynewlist):
    print(mynewlist[index])
    index+=1

# looping a list using list comprehension
print("\nPrinting item though list comprehension")
[print(item) for item in mynewlist]

# List comprehension --> provide shortest syntex when we want to create a new list using the value of existing vlaues 
fruits=[item for item in mynewlist if 'e' in item] 
print("\nnew list from list comprehension",fruits)