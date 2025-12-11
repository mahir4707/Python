# code to write class for train booking 
from random import randint

class train:
    def __init__(self, train_number):  
        self.train_number = train_number

    def getstatus(self):
        print(f"Train number {self.train_number} is on time.")

    def book(self, fro, to):
        print(f"Your ticket from {fro} to {to} has been booked on train number {self.train_number}.")

    def getfare(self, fro, to):
        print(f"The fare from {fro} to {to} is Rs.{randint(150, 5555)}.")

t = train(12345)
t.getstatus()
t.book("Rajkot", "Ahmedabad")
t.getfare("Rajkot", "Ahmedabad")