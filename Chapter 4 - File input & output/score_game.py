# Code to update high score file whenever user enter score greater than previous one 
def game():
    # input from the user
    your_score  = int(input("Enter any number:"))

    #fetching data from txt file
    with open("3_High_score.txt") as f:
        high_score = f.read()
        if(high_score !=""):
            high_score = int(high_score)
        else:
            high_score == 0

    #comparing both the scores
    if (your_score > high_score):
        print("You win!!")
        print(f"HIgh score is now {your_score}")
        
    #writing into file new high score
        with open("3_High_score.txt", "w") as f:
            f.write(str(your_score))

    else:
        print("Better luck next Time!!")
        
    return your_score

game()