import random 

"""WE ARE GOING TO PLAY
ROCK, PAPER AND SCISSORS"""

computer = random.choice(["r","p","s"])
youstr = input("Enter your choice: ")

reverseDict = {"r": "Rock", "p": "Paper", "s": "Scissors"}

you = youstr

print(f"You choose:- {reverseDict[you]}\ncomputer choose:- {reverseDict[computer]}")

if (computer == you):
    print("Tie!!")

else:
    if (computer == "r" and you == "p" ):
        print("U win!!")
    elif(computer == "p" and you == "r"):
        print("computer win!!")
    elif(computer == "s" and you == "p"):
        print("computer win!!")
    elif(computer == "p" and you == "s"):
        print("U win!!")
    elif(computer == "s" and you == "r"):
        print("U win!!")
    elif(computer == "r" and you == "s"):
        print("computer win!!")
    else:
        print("Something went wrong!!")


