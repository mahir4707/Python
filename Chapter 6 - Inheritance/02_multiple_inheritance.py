# multiple inheritance is a process where a class can inherit properties and behaviors from more than one parent class.

class company:
    name = "TCS"
    total_employees = 10000

class departmentA(company):
    departmentA_name = "IT"

class departmentB(company):
    departmentB_name = "Marketing"

# o = company()
# print(o.name, o.total_employees, o.departmentA_name) #This will show error as department name is not in the class company

o = departmentA()
print(o.name, o.total_employees, o.departmentA_name) #This can access all the attributes of parent classes

o = departmentB()
print(o.name, o.total_employees, o.departmentB_name) #This can access all the attributes of parent classes