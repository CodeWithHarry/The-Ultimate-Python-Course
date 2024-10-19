nameInput = input("Please enter your name:")

print("Good afternoon",nameInput,"!!")
print(f"Good afternoon, {nameInput}!!")  # Add f is mandatory

print("------------------------------------------------------------------------------------------------------------------")

name = input("Please enter your name: ")
date = input("Please enter date: ")

letter = (f'''Dear {name},
You are selected!
{date}''')

print(letter)

print("------------------------------------------------------------------------------------------------------------------")

text = "I am a great  programer"

print(text.find("  "))

print("------------------------------------------------------------------------------------------------------------------")

para = "I am a great  programer"

print(para.find("  "))


len = para.replace("  ", " ")
print(len)
print(len.find("  "))

print("------------------------------------------------------------------------------------------------------------------")

change = "Dear Aakash,\nThis python course is nice.\n\t\tThanks!"
print(change)

