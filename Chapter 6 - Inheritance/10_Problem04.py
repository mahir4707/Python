# code to add two complex number using class

class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = complex(2, 3)
c2 = complex(4, 5)
c3 = c1 + c2
print(c3)