s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

# 2 cuz 20 == 20.0 comparision operator
print(len(s))