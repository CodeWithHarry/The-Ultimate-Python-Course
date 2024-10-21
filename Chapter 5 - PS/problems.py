words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want meaning of: ")

print("The meaning of the word is: " ,words[word]) 
# If the word is not available in dict it will give a key error

print("-----------------------------------------------------------------------------------")

# create an empty set
s = set()

n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)
# This set will give all the unique value in the set

print("-----------------------------------------------------------------------------------")

t = set()
t.add(18)
t.add("18")
t.add(18.0)

# Yes it prints the value to different type
print(t)

print("-----------------------------------------------------------------------------------")
y = set()
y.add(20)
y.add(20.0)
y.add('20') # length of s after these operations?

# 2 cuz 20 == 20.0 comparision operator
print(len(y))

print("-----------------------------------------------------------------------------------")
u = {}
print(type(u))
# type is dict cuz its is initiated as empty

name = input("Enter your name: ")
lang = input("Enter your language: ")

print(u.update({name: lang}))
print(u)

print("-----------------------------------------------------------------------------------")

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)
# same way solved in last file

print("-----------------------------------------------------------------------------------")
# No we cannot update it-
# TypeError: unhashable type: 'list' set is not indexed

o = {8, 7, 12, "Harry", [1,2]}
o[4][0] = 9