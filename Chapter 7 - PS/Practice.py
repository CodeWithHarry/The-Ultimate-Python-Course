# n = int(input("Enter a number: "))

# for i in range (1,11):
#     print(f"{n} * {i} = ", n * i )

print("------------------------------------------------------------------")
a = ["Aakash", "Emily", "Hitesh", "Anna"]

for n in a :
    if (n.startswith("E")):
        print(f"Hello!! {n}")

print("------------------------------------------------------------------")
# b = int(input("Enter a number: "))

# for n in range(2  ,b) :
#     if (b % n) == 0:
#         print(f"This is not a prime number")
#         break
# else:
#     print(f"This is a prime number")
        
print("------------------------------------------------------------------")

n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)

print("------------------------------------------------------------------")
# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")