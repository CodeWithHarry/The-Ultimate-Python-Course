n = int(input("Enter a number: "))

for i in range (1,11):
    print(f"{n} * {i} = ", n * i )

print("------------------------------------------------------------------")
a = ["Aakash", "Emily", "Hitesh", "Anna"]

for n in a :
    if (n.startswith("E")):
        print(f"Hello!! {n}")

print("------------------------------------------------------------------")
b = int(input("Enter a number: "))

for n in range(2  ,b) :
    if (b % n) == 0:
        print(f"This is not a prime number")
        break
else:
    print(f"This is a prime number")
        
