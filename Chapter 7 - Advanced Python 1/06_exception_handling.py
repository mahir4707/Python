#best practice is to handle specific exceptions rather than using a general exception handler.

#for invalid conversion
try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Invalid conversion to integer!")

# #for division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter numbers only!")
except ZeroDivisionError:
    print("Number cannot be zero!")
