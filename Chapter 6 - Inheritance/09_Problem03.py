class Employee:
    salary = 50000
    increment = 10

    @property
    def salaryAfterincreament(self):
        return (self.salary + (self.salary * self.increment / 100))
    
    @salaryAfterincreament.setter
    def salaryAfterincreament(self, salary):
        self.increment = ((salary/self.salary - 1) * 100)
        

e = Employee()
# q = e.salaryAfterincreament
e.salaryAfterincreament = 55000
# print(q)
print(e.increment)