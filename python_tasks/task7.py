"""
    Description:Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's
    method.
"""

print("Enter a list, separated by spaces:")
user_input = input()
list = list(map(int, user_input.split()))
new={i+1:x for i,x in enumerate(list)}
print(new)