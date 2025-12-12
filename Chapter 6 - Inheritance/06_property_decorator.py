#property decorator is used to define a method as a property, allowing you to access it like an attribute.

class company:
    a = 10
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]


o = company()
o.a = 45 
o.name = "Mahir Sama"
print(o.fname, o.lname)
o.show()