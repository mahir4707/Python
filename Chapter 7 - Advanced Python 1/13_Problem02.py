# program to print third, fifth and seventh element of a list using enumerate function

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index, value in enumerate(my_list):
    if index in (2, 4, 6):  
        print(value) 