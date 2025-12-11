# code to write slf and mahir instead of self, does anything change? Answer: NO
from random import randint

class train:
    def __init__(slf, train_number):  
        slf.train_number = train_number

    def getstatus(slf):
        print(f"Train number {slf.train_number} is on time.")

    def book(mahir, fro, to):
        print(f"Your ticket from {fro} to {to} has been booked on train number {mahir.train_number}.")

    def getfare(self, fro, to):
        print(f"The fare from {fro} to {to} is Rs.{randint(150, 5555)}.")

t = train(12345)
t.getstatus()
t.book("Rajkot", "Ahmedabad")
t.getfare("Rajkot", "Ahmedabad")