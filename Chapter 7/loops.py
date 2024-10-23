# In python below is he syntax for run till n-1
# For i in range(0,100,4) 4 here is jump number
for i in range(0,100,4):
    print(i)

print("-----------------------------------------------------------")
# While loop
j = 1
while(j<5):
    print(j)
    j+=1

print("-----------------------------------------------------------")
#print content of the list
a = [1,2,3,4,5,"Aakash"] 
k=0
while(k < len(a)):
    print(a[k])
    k+=1

print("-----------------------------------------------------------")
# for loop in list with else
for l in a:
    print(l)
else:
    print("Loop completed") # This prints when the loop is completed

print("-----------------------------------------------------------")
t = (6,23,42,98)
for m in t:
    print(m)

print("-----------------------------------------------------------")
# Break - exit the loop at the break statement
for n in range(100):
    if(n == 35):
        break
    print(n)

print("-----------------------------------------------------------")
# continue skips the given condition
for n in range(50):
    if(n == 35):
        continue
    print(n)

print("-----------------------------------------------------------")
# Pass
for n in range(50):
    pass

#  Pass allow Python to run the code with out throwing an error
j = 1
while(j<5):
    print(j)
    j+=1

