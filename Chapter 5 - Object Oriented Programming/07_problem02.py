# code to write class for calculator and perform operation like square, cube and square root of number.

class calculator:
    
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5
    
m = calculator(2)
print("Square:", m.square())
print("Cube:", m.cube())