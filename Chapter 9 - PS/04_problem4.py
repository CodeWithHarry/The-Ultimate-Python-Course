word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(contentNew)