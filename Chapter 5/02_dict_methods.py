# Dictionary is mutable
marks = {
    "Aakash": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry",
    "Emily": [1,2,3]
}

# 0: "Harry" is allowed

# it will give all the details of Dictionary
print(marks.items())
print("---------------------------------------------------------------------------------")

# Give the keys of the Dictionary
print(marks.keys())
print("---------------------------------------------------------------------------------")

# Give the keys of the Dictionary
print(marks.values())
print("---------------------------------------------------------------------------------")


# Updates the Dictionary with given key:value pairs
marks.update({"Aakash": 99, "Renuka": 100})
print(marks)
print("---------------------------------------------------------------------------------")

# IF THE KEY IS NOT PRESENT IT WILL GIVE NONE
print(marks.get("Hitesh")) 
print(marks.get("Aakash")) 
# print(marks["Aakash2"]) # Returns an error if this method is 
print("---------------------------------------------------------------------------------")

print(marks.get("Emily"))
print("---------------------------------------------------------------------------------")

