# code to write class programmer and store the info of some of microsofts programmer.

class programmer:
    name = "Microsoft"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

p = programmer("Mahir", "Developer", 1000000)
print(p.name, p.role, p.salary)

q = programmer("Amit", "Manager", 2000000)
print(q.name, q.role, q.salary)        