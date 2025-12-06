# Code to print multiplication table of given number

n = int(input("Enter any number:"))


for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    

# Using while loop
n = int(input("Enter any number:"))

i=1
while(i<=10):
    print(n*i)
    i +=1