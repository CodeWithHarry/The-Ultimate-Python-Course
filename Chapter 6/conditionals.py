age = int(input("Please enter your age: "))

# in Python we use : instd of {} IF ELIF LADDER -- Multiple if statements
# All the IF statements works independently - else and elif cannot be alone
# IF STATEMENT 1

if (age >18) :
    print( "You are allowed to vote!")

elif(age<0):
    print("Please enter a valid age")

elif(age==0):
    print("You are entering 0")

else:
    print("You are not allowed to vote!!")

#END OF IF STATEMENT 1


print("---------------------------------------------------------------------")


# IF STATEMENT 2
if (age%2 == 0) :
    print( "Age is even")

#END OF IF STATEMENT 2

print("---------------------------------------------------------------------")

