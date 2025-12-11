# This code is for static method

# static method is used when we don't want to use self word in our method.

class school:
    name = "The school of science"
    location = "Rajkot"
    fees = 120000

    @staticmethod
    def getinfo():
        print(f"I have studied in {school.name} located at {school.location} with fees {school.fees}")

mahr = school()
mahr.getinfo() #withput self we can call static method directly