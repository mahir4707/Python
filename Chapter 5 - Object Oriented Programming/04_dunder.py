# code to demonstate dunder methods in Python classes.

class school:
    def __init__(self, name, location, fees):
        self.name = name
        self.location = location
        self.fees = fees

mahir = school("The school of science", "Rajkot", 120000)
print(mahir.name, mahir.location, mahir.fees)
    