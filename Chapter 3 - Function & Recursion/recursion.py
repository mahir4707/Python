# Code to show recursion function 
# Code to find the factorial of given number from the user 

# Recursion 
'''
factorial(5)
5 x factrial(4)
5 x 4 x factorial(3)
5 x 4 x 3 x factorial(2)
5 x 4 x 3 x 2 x factorial(1)
5 x 4 x 3 x 2 x 1

'''

def factorial(n):
    if n==1 or n==0: # factorial of 1 and 0 are 1
        return 1
    return n* factorial(n-1)

n=int(input("Enter the number:"))
factorial(n)
print(f"Factorial of given number is {factorial(n)}")