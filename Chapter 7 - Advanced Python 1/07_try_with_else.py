#else block runs only if no exception occurs in try block
try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid number!")
else:
    print("Square:", n*n)
