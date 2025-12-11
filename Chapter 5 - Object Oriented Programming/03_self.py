# This is code to demonstrate the use of 'self' in Python classes.

# class school:
#     name = "The school of science"
#     location = "Rajkot"
#     fees = 120000

#     def getinfo():
#         print(f"I have studied in {school.name} located at {school.location} with fees {school.fees}")

# mahr = school()
# mahr.getinfo()  # This will raise a TypeError because 'self' is missing in the method definition.

# corrected way with 'self'
class school:
    name = "The school of science"
    location = "Rajkot"
    fees = 120000

    def getinfo(self):
        print(f"I have studied in {self.name} located at {self.location} with fees {self.fees}")

mahr = school()
mahr.getinfo()  # This will work correctly now.
    