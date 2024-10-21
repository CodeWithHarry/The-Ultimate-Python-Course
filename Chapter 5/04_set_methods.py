# Different type of data is allowed in a set
s = {1, 5, 32, 54,5, 5, 5, "Aakash"}

print(s, type(s))
print("---------------------------------------------------------------------------")

# It add the element to the set
s.add(566)
print(s, type(s))
print("---------------------------------------------------------------------------")

# It removes the element to the set
s.remove(1)
print(s, type(s))

print("---------------------------------------------------------------------------")
# It removes random value
s.pop()
print(s, type(s))
