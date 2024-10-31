f = open("filePractice.txt")

# readlines returns the list of lines
# lines = f.readlines()
# print(lines, type(lines))

print("----------------------------------------------------------------------------------------------------------")
# This readline will give the line only
# line1 = f.readline()
# print(line1, type(line1))

print("----------------------------------------------------------------------------------------------------------")

# line2 = f.readline()
# print(line2, type(line2))

print("----------------------------------------------------------------------------------------------------------")

# line3 = f.readline()
# print(line3, type(line3))

print("----------------------------------------------------------------------------------------------------------")

# line4 = f.readline()
# print(line4, type(line4))

print("----------------------------------------------------------------------------------------------------------")

# If there is no line then it will print empty string
# line5 = f.readline()
# print(line5 =="")

print("----------------------------------------------------------------------------------------------------------")

# Doing the same thing is loop so the it is easier to do-
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

print("----------------------------------------------------------------------------------------------------------")
