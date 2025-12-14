l = [1, 2, 3, 4, 5]

#map function
square = lambda x: x ** 2
squared_list = list(map(square, l))
print("Squared List:", squared_list)

#filter function
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print("Even Numbers:", even_numbers)

#reduce function
from functools import reduce

sum_of_list = reduce(lambda x, y: x + y, l) 

print("Sum of List:", sum_of_list)
product_of_list = reduce(lambda x, y: x * y, l)

print("Product of List:", product_of_list)
