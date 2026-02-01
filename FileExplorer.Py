import os  # 📦 Import the built-in 'os' module to interact with the operating system

# 📂 Select the directory whose contents you want to list
directory_path = '/'  
# '/' means the root directory (top-most folder of the file system)
# On Windows, this may raise an error. Example alternative: 'C:\\' or '.' (current folder)

# 🧠 Use the os module to list the directory contents
contents = os.listdir(directory_path)
# os.listdir():
# - Reads all files and folders inside the given directory
# - Returns the result as a Python list of strings
# - Each string is a file or folder name
# - It does NOT give file sizes or details, only names

# 🖨️ Print the contents of the directory
print(contents)
# print():
# - Displays the list of files and folders on the screen
