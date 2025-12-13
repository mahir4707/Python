import random
n= random.randint(1,100)
a = -1 
guesses = 0

while (a!=n):
    guesses += 1
    a = int(input("Guess a number between 1 and 100: "))
    if a > n:
        print("Too high!")
    else:
        print("Too low!")

print(f"Congratulations! You guessed the number {a} in {guesses} guesses.")