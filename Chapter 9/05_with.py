# a can be used instead of f but good practice is using f
a = open("filePractice.txt")
print(a.read())
a.close()

print("-----------------------------------------------------------------------------------")

# with statement is mostly used
# The same can be written using with statement like this:

with open("filePractice.txt") as f:
    print(f.read())

# You dont have to explicitly close the file