with open("log.txt") as f:
    content = f.read()

# checking f the python is present in file
if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")