# find the greatest number

def greatestNum(a,b,c):
    
    if(a>b and a>c):
        print("a is the greatest")
    elif(b>a and b>c):
        print("b is the greatest")
    else:
        print("c is the greatest")

greatestNum(9,165,8)

print("------------------------------------------------------------------------------------")


def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

print("------------------------------------------------------------------------------------")

print("a")
print("b")
print("c", end="")
print("d")

print("------------------------------------------------------------------------------------")

def sum(n):
    if(n==1):
        return 1 
    return sum(n-1) + n

print(sum(6))
print(sum(4))

print("------------------------------------------------------------------------------------")

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

print(pattern(5))

print("------------------------------------------------------------------------------------")

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")

print("------------------------------------------------------------------------------------")

def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(5)

print("------------------------------------------------------------------------------------")


def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Aakash", "Rohan", "Shubham", "an"]

print(rem(l, "an"))