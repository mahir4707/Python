# Code to find the sum of first n natural number using recursion 

'''
sum(5)
5 + sum(4)
5 + 4 + sum(3)
5 + 4 + 3 + sum(2)
5 + 4 + 3 + 2 + sum(1)
5 + 4 + 3 + 2 + 1

'''

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    
n= int(input("Enter any number:"))
sum(n)
print(f"Sum of first {n} natural numbers is {sum(n)}")
print("Thank You!!")