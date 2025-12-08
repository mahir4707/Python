# Code to convert celsius into fahrenheit
# formula F = ( C x 9/5 ) + 32

def find_fahrenheit(c):
    f = (c * 9/5) +32
    print(f"The {c} degree is {f}")

c = int(input("Enter the celsius Temperature:"))
find_fahrenheit(c)
print("Thank You!!")
