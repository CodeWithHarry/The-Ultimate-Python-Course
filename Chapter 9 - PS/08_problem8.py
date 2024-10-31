with open("this.txt") as f:
    content = f.read()

# This will copy the content in other file
with open("this_copy.txt", "w") as f:
    f.write(content)