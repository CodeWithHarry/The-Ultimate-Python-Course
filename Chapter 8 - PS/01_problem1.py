def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        print("The greatest number is: b")
        return b
    elif(c>b and c>a):
        print("The greatest number is: c")
        return c

a = 1
b = 23
c = 3

print(greatest(a, b, c))
