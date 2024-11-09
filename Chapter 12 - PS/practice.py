try:
    with open ("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open ("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open ("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Working fine")

print("--------------------------------------------------------------------")

l = [1,2,3,4,5,6,7,8,9]

for i, item in enumerate(l):
    if i == 2 or i == 4:
        print(item)

print("--------------------------------------------------------------------")

n = int(input("please enter a number: "))

table = [n*i for i in range(1,11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")

print("--------------------------------------------------------------------")

a = int(input("please enter a number: "))
b = int(input("please enter a number: "))

try:
    x = a/b
    print(x)
except Exception as e:
    if(b == 0):
        print("Error : Don't divide by zero")

print("--------------------------------------------------------------------")

try:
    l = int(input("Enter l: "))
    k = int(input("Enter k: "))
    print(l/k)
except ZeroDivisionError as v:
    print("Infinite")
    print(v)

print("--------------------------------------------------------------------")
