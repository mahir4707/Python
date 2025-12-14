# Write a program to find the maximum of the numbers in a list using the reduce
# function

from functools import reduce
numbers = [12, 45, 2, 67, 34, 89, 23]

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum number in the list is:", max_number)