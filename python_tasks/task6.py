set1 = {1,2,4,5,3,7,8,9}
set2 = {10,12,4,5,6,11,14}

# adding item to the set
set1.add(0)
print("Added element to set 1",set1)

set2.add(0)
print("Added element to set 2",set2)

set1.remove(0)  #remove an item 
print("set 1 after removing element",set1)

set1.pop()  # pop the last element present at the top of stack
print("Popping element from set1:",set1 )

print("printing the element of set 1")
for item in set1:  # iterating over the set 1
    print(item, end= ' ')

set1.update(set2)  # changes the original set and do not return a new set 
print("Union of set using update:",set1)

set3 = set1.union(set2)  # return a new set with all the item of both set 
print("uninon of sets using Union",set3)

set4 = set1.intersection(set2)  # return a new set of only common elements
print("Intersaction of sets:",set4) 

set1.intersection_update(set2)  # update in the original set and keeps only common elements
print("Intersaction of set using Intersaction Update:",set1)

dif_set1 = {'apple','banana','kiwi'}
dif_set2 = {'apple','orange','mango'}
dif_set3 = dif_set1.difference(dif_set2)  # return a new set of item from first set that are not present in other set
print("difference of set ",dif_set3)


dif_set4 = {'apple','banana','kiwi'}
dif_set5 = {'apple','orange','mango'}
dif_set4.difference_update(dif_set5)  # set of item from first set that are not present in other se , only changes the existing set does not give new set
print("difference_update of set ",dif_set4)

firstset = {1,2,3,4}
sencondset = {2,3,4}
print(firstset.issuperset(sencondset))  #return if a set contain another set or not
print(sencondset.issubset(firstset))  #return if a set contain another set or not

new_set = {1,2,4,5,3,0}
new_set.clear()  # empty the set 
del new_set  # delete the set 

copy_set1 = {1,2,4,5,8}
copy_set2 = copy_set1.copy()  # make a copy of copy_set1
print("Copy set 2:",copy_set2)

symmetric_set1 = {"google", "microsoft", "apple"}
symmetric_set2 = {"apple", "banana", "cherry"}
symmetric_set3 = symmetric_set1.symmetric_difference(symmetric_set2)  # return a new set that is not present in both set
print("Symmetric difference of sets:",symmetric_set3)

