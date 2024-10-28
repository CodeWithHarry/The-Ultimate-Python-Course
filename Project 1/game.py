# Snake Water and gun game
import random

# We will assign computer a random value for the game
computer = random.choice([-1, 0, 1])

# This will let the user put the choice-
youStr = input("Enter your choice: ")

# We will create a dictionary for the choices for Snake, Water and Gun
youDict = {"s":1,"w":-1,"g":0}

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

#It will chose the no. on the basis of user choice 
you = youDict[youStr]

# This will print the choices of both the computer and user.
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# This is will print when the both chose the same option
if(computer == you):
    print("Its a draw")
else:
# This is nested loop example
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")