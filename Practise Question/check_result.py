# code to check the result if student is pass or fail

print("Please Enter marks out of 100")
maths = int(input("Marks Obtained in Maths:"))
science = int(input("Marks Obtained in Science:"))
english = int(input("Marks Obtained in English:"))
total = maths+science+english

print("Marks for Maths, Science and English are ",maths, science, english)
print("Total marks obtained:",total)

if(maths>33 and science>33 and english>33 and total>120):
    print("You have cleared all subjects and You have Passed!!")
else:
    print("Better Luck Next time")


