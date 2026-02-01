import os

#select the directory whose content you wnat to list
directory_path = '/'

#use the os module to list the directory content 
contents = os.listdir(directory_path)
#print the contents of the directory 
print(contents)
