# multiline strings 
string="""hello world!
welcome to python learning"""
print(string)

# accessing the character from string 
name="pankaj"
print(name[0])

# looping through string 
for char in name:
    print(char)

# printing length of string 
print("Lenght of string is:",len(name))


# checking if any character present in string using "in" keyword
print("pan" in name )
print("kan" in name )


# using "in" keyword in "if" condition
if "kaj" in name:
    print("yes! it is present")
else:
    print("not present")

# not in
if "naj" not in name:
    print("No, it is not present in",name)

##############################################################################

# slicing string 
sentence="hello, today is my first day"
print(sentence[2:13])  #start index is inclusive and end index is exclusive 

# slice from start 
print(sentence[:13])

#slice to the end
print(sentence[2:]) 

# negative indexing to start slicing from end 
greet = "hello, world!"
print(greet[-12:-5])

###############################################################################

# MODIFY string
sentence2="Coding Duniya"
print(sentence2.upper())  #convert whole string to upper case
print(sentence2.lower())  #convert whole string to lower case 
print(sentence2.strip())  #remove whitespaces before and after the actual text from string 
print(sentence2.replace("Coding Duniya","code world"))  #replace string/character with another string/character
print(sentence2.split(" ")) #return a list of seperated words based on any seperator 

###############################################################################

# String Concatenation
word1="hello"
word2="sir,"
word3="welcome"
print(word1+" "+word2+" "+word3)

##############################################################################

# fromat string i.e adding string and number using f-string
age=22
print(f"My age is {age}")

price=20000
print(f"the price is {price} dollars")

##############################################################################

# escape character
print("hello from \"Pankaj\"kumar") 