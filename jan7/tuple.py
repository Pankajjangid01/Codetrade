# Update tuple
"""
since tuples are immutable we cannot change items once we created the tuple 
So to update tuple we have to convert it into list and then update the list and then againg convert the list into tuple  
"""

# change tuple value 
tupl=('ram','shyam','verma')
list1=list(tupl)
list1[0]='Aman'
tupl=tuple(list1)
print(tupl)


# add item to tuple --> we can use append method by converting tuple into list
tupl=('ram','shyam','verma')
addlist=list(tupl)
addlist.append("sharma")
tupl=tuple(addlist)
print(tupl)

# add tuple to tuple
existingtuple=('India',"USA")
newtuple=('UK',)
existingtuple+=newtuple
print(existingtuple)

# remove item from tuple
newlist=list(tupl)
newlist.pop() #remove the last item from the list 
tupl=tuple(newlist)
print(tupl)

# deleting tuple completely using del 
del tupl
# print(tupl)

#####################################################

# unpacking tuple
"""
packing a tuple means normally assiging value to the tuple 
And unpacking means we can extract the values back to the variable 
"""
mytupl=('Orange','Mango',"Apple")
(fruit1,fruit2,fruit3)=mytupl
print(fruit1)
print(fruit2)
print(fruit3)


# use of Asterisk *
'if the no. of variable are less then the no. of values , then we can assign * to any variable and the values will be stored as the list in the variable'
newtupl=('Orange','Mango',"Apple","papaya")
(*orange,yellow,red)=newtupl
print(orange)
print(yellow)
print(red)

# count()-->count the no. of time a value occur in tuple
print(newtupl.count('Orange'))
