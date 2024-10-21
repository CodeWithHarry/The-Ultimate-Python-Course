s = {}
print(type(s))
# type is dict cuz its is initiated as empty

name = input("Enter your name: ")
lang = input("Enter your language: ")

print(s.update({name: lang}))
print(s)