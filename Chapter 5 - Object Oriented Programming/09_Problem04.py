# code to add static function to greet all the users of calculator class

class calculator:
    
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5
    
    @staticmethod
    def greet():
        print("Hello! Welcome to the calculator class.")
    
m = calculator(9)
calculator.greet()  # Calling static method without creating an instance
print("Square:", m.square())
print("Cube:", m.cube())
print("Square Root:", m.square_root())