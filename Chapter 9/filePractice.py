# How to read a file (Syntex)-

# r – open for reading 
# w - open for writing  
# a - open for appending 
# +  - open for updating. 
# ‘rb’ will open for read in binary mode. 
# ‘rt’ will open for read in text mode. 

# Open is built-in function which helps to open the files in python. "r" read mode is by default.
f = open("filePractice.txt")
# f.read is used to read the file content
data = f.read()
print(data)
# It is a good practice to close.
f.close()


