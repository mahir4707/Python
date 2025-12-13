# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter numerator (a): "))
    b = int(input("Enter denominator (b): "))
    result = a / b
    print("Result of a/b is:", result)
except ZeroDivisionError:
    print("infinite")