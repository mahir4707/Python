# Store the multiplication tables generated in problem 3 in a file named Tables.txt

n = int(input("Enter a number: "))

list = [n * i for i in range(1, 11)]

with open("Tables.txt", "a") as file:
   
    file.write(f"{str(list)} \n")
    # for item in list:
    #     file.write(f"{item}")
print("Multiplication table stored in Tables.txt")