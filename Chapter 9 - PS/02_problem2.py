import random

def game(): 
    print("You are playing the game..")
    # .randint will create a random no. between 1 and 62
    score = random.randint(1, 100)
    
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        # If the hiscore is emplty then consider it 0 else convert it into int and make it hiscore
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    # IF high score is greater then it will write it in the txt file
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()