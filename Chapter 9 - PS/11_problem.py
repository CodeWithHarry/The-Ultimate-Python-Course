with open("old.txt") as f:
    content = f.read()

with open("renamed_by_aakash.txt", "w") as f:
    f.write(content)