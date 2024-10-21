friends = ["Apple", "Banana", 5, 345.06, False, "Aakash", "Hitesh"]
print(friends)
print("-----------------------------------------------------------------")
# Adds in the end of the list
friends.append("Emily") 
print(friends)
print("-----------------------------------------------------------------")

# Sorts the list
l1 = [1, 34,62, 2, 6, 11]
l1.sort()
print(l1)
print("-----------------------------------------------------------------")

# Reverse the list
l1.reverse()
print(l1)
print("-----------------------------------------------------------------")

# Insert the list
l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
print(l1)
print("-----------------------------------------------------------------")

# take out the indev from the list
value = l1.pop(3)
print(value)
print("-----------------------------------------------------------------")

# Remove data from the list
l1.remove(333333)
print(l1)
print("-----------------------------------------------------------------")

# Final output
print(l1)