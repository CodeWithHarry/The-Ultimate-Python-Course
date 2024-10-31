# This is string we want to write
st = "Hey Aakash you are amazing!!"

# give the name of the file in which you want to write, w means write mode-
f = open("file_practice_write.txt", "w")

# used write msg
f.write(st)

f.close()