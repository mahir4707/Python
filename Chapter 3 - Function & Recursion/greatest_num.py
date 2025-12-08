# Code to find the greatest number from three number input from the user using function 

def find_greatest(num1, num2, num3):
    if(num1 > num2 and num1>num3):
        print(f"{num1} is greatest")

    elif(num2>num1 and num2>num3):
        print(f"{num2} is Greatest")

    else:
        print(f"{num3} is Greatest")


num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
find_greatest(num1, num2, num3)
print("Thank You!!")