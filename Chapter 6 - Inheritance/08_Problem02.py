# write code to create class animal and make another class pet inherited from animal then further inherite class dog from pet , add methos bark to dog class

class animal:
    pass

class pet(animal):
    pass 

class dog(pet):
    pass 

    def bark(self):
        print("Bhoww! Bhoww!")

d = dog()
d.bark()