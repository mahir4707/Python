# class method is used when we have to show the class attribute instead of instance attribute.

class company:
    a = 10
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

o = company()
o.a = 45 #instance attiribute if we not use class methos then it will show instance attribute
o.show()