# adding item to set 
'once a set is created, we cannot change its item, but we can add new items to it using add()'

myset={'laptop','pc','mobile'}
myset.add('tablet')
print(myset)
# import pdb
# pdb.set_trace()

# to add another set to the current set we use update() method
newset={'HP',"Lenevo","Dell"}
myset.update(newset)
print(myset)

# we can any iterable object to set such ad list, tuple, dictionar,etc
mylist=['Nokia','Samsung','Iphone']
newset.update(mylist)
print("After adding list to the set ",newset)


#####################################################

# Remove an item from set using remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove an item from set using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


"""
In the remove(), if it does not find the item then it will raise the error.
But in the discard(), it will not raise the error.
We can also use pop() method to remove item but we know sets are unordered so we will not know which item was deleted
"""

# looping th set using for loop
thenewset = {"apple", "banana", "cherry"}
for item in thenewset:
    print(item)
# import pdb
# pdb.set_trace()

#############################################

# Joining multiple sets
# set1={1,3,5,8,6,"pani puri","gulaab jamun"}
# set2={"pani puri","gulaab jamun","daal bati",1}

# set1.update(set2) #changes the original set and do not return a new set 
# print(set1)
# set3=set1.union(set2) #return a new set with all the item of both set 
# set3=set1 | set2 # return the same result as union
# print(set3)
# 'both update and union will exclude the duplicate items'


# # intersection() --> return a new set of only the duplicate , present in both the sets 

# set3=set1.intersection(set2)
# print("After intersection",set3)
# print("after intersection of set",set3)

# # intersection_update() --> gives only the duplicates , only changes the existing set does not give new set
# set1={'apple','banana','kiwi'}
# set2={'apple','orange','mango'}
# set1.intersection_update(set2)
# print("after intersection_update of sets ",set1)


# # difference()-->return a new set of item from first set that are not present in other set
# set1={'apple','banana','kiwi'}
# set2={'apple','orange','mango'}
# set3=set1.difference(set2)
# print("difference of set ",set3)

# #difference_update()-->  set of item from first set that are not present in other se , only changes the existing set does not give new set
# set1={'apple','banana','kiwi'}
# set2={'apple','orange','mango'}
# set1.difference_update(set2)
# print("difference_update of set ",set1)

# # symmetric_differnece()--> return a new set of items that are not present in both sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print("symmetric_differnece of set ",set3)

# # symmetric_difference_update()--> method to keep the items that are not present in both sets, only changes the existing set does not give new setset1 = {"apple", "banana", "cherry"}
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print("symmetric_differnece_update of set ",set1)


# # Methods
# firstset={1,2,3,4}
# sencondset={2,3,4}
# print(firstset.issuperset(sencondset)) #return if a set contain another set or not
# print(sencondset.issubset(firstset)) #return if a set contain another set or not
