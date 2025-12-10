import random

'''
Rock = -1
Paper = 0
Scissor = 1

'''
options = [-1, 0, 1]
computer = random.choice(options)
youstr = input("Enter Your choice from r, s and p:")
youDict = {"r": -1, "p": 0, "s": 1}
reverseDict = {-1: "Rock", 0: "Paper", 1: "Scissor"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You lose!!")
    elif(computer == -1 and you == 0):
        print("You win!!")
    elif(computer == 1 and you == -1):
        print("You win!!")
    elif(computer == 1 and you == 0):
        print("You lose!!")
    elif(computer == 0 and you == 1):
        print("You win!!")
    elif(computer == 0 and you == -1):
        print("You lose!!")
    else:
        print("Something went Wrong")