#inheritance is a process of acquiring properties and behaviors from a parent class to a child class.

class school:
    name = "The school of science"
    total_students = 500

class A(school):
    medium = "English"

o = A()
print(o.name, o.total_students, o.medium)