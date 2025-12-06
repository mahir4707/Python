# code to show if elif else ladder 

num = int(input("Enter any number:"))

if(num%2 == 0):
    print("num is even")

if(num>0):
    print("Number is POSITIVE")

elif(num<0):
    print("Number is Negative")

else:
    print("Invalid number")

print("End of Program")