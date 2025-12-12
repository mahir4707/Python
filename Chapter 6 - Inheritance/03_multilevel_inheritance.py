# multilevel inheritance is a process where a class can inherit properties and behaviors from a parent class,
# and then another class can inherit from that child class, forming a chain of inheritance.

class school:
    name = "The school of science"
    total_students = 500
    
    def display_school_info(self):
        print(f"There are {self.total_students} students in {self.name}.")

class A(school):
    medium = "English"
    
    def display_medium(self):
        print(f"The medium of instruction is {self.medium}.")

class B(A):
    section1 = "Maths A Group"
    section2 = "Biology B Group"

    def getinfo(self):
        self.display_school_info()
        self.display_medium()
        print(f"Sections available: {self.section1} and {self.section2}.")


o = B()
o.getinfo()