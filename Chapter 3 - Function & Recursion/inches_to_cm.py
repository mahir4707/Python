# Code to convert inches into cm 

def convert(i):
    cm = i * 2.54
    return cm

i = int(input("Enter inches:"))
convert(i)
print(f"{i} inches is {convert(i)} cm")
print("Thank You!!")