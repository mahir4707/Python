# Code for function to print multiplication table for the given number 

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter any number:"))
table(n)
