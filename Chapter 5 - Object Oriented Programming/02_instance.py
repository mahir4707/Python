class school:
    name = "ABC High School"
    location = "New York" # this is a class attribute

student1 = school() #create object of class school
print(student1.name, student1.location)

# if we change location for student1
student1.location = "Los Angeles" # this creates an instance attribute
print(student1.name, student1.location) #gives instance attribute

# it always looks for instance attribute first, then class attribute