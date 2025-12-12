# super() function is used to call a method from a parent class in a child class.

class employee:
    a = 10

    def __init__(self):
        print("Constructor of employee class")

class manager(employee):
    b = 20

    def __init__(self):
        print("Constructor of manager class")

class director(manager):
    c = 30

    def __init__(self):
        super().__init__()
        print("Constructor of director class")

o = director()
print(o.a, o.b, o.c)