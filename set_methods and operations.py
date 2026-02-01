# Corrected and commented set examples

# Create a set. Sets are unordered collections of unique items.
s = {1, 2, 3, 4, 5, 68, 42, "harry"}  # mixing ints and strings is allowed but uncommon
print("Initial set:", s, "Type:", type(s))

# Add an element to the set
s.add(566)
print("After add(566):", s)

# Remove an element safely
# .remove(x) raises KeyError if x not present. .discard(x) does not raise.
s.discard(1)
print("After discard(1):", s)

# ---------------------------------------------------------------- #
# SET OPERATIONS: UNION and INTERSECTION
s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

# union: all unique elements from both sets
print("s1 union s2:", s1.union(s2))

# intersection: elements common to both sets
print("s1 intersection s2:", s1.intersection(s2))
