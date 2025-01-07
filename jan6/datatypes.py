# str,int,float,complex,list,tuple,range,set,frozenset,dict,bytes,NoneType
name="pankaj"  # str
number=11 # int
decimal=11.2 # float
comp=1j # complex
fruits=['orange','banana','apple'] # list(mutable,insertion and deletion easy,Indexeing and slicing allowed)
print(fruits)
tupl=('pen','books','paper') # tuple (immutable,appropriate for accessing elements,Indexeing and slicing allowed)
rangee=range(6) # range
dictionary={"name":"Pankaj","age":22,"gender":"male"}  # dict- key value pair 
isTrue=True # bool
byts=b"hello"  # bytes
color=None  # NoneType

#set
"""
1. set do not allow duplicates
2. contains hetrogenous elements
3. usefull for mathmetical operations such as union, intersaction and difference
4. mutable and cannot be accessed using index value 
5. Indexeing and slicing not allowed
"""
setExample={'red','green','blue','red'}
# print(setExample)o

#frozenset
"""
1. Immutable and it is hashable using index value
2. unordered and unindexed collection of unique elements
3. Do not allow duplicates
"""
frozenSet=frozenset({"rahul","sumit","hardik","rahul"})
# print(frozenSet)


#dictionary with frozenset
numberDictionay={"occupation":"student","mobilenumber":63759484445,"gender":"Male","age":22}
print(frozenset(numberDictionay))