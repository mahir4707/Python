''' Code to print this pattern for n=3
          *
         ***
        *****
'''

n= int(input("Enter the number"))

for i in range(0,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1), end="")
    print(" ")