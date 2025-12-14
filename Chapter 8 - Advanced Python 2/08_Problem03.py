# Write a program to filter a list of numbers which are divisible by 5

numbers = [10, 23, 45, 67, 80, 91, 100, 123, 150]

divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(divisible_by_5)