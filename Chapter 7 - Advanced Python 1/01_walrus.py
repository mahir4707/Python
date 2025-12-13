# walrus operator is used as "assignment expression" in Python. It allows you to assign a value to a variable as part of an expression. The operator is represented by `:=`.

if (n := len("Hello, World!")) > 10:
    print(f"The length of the string is {n}, which is greater than 10.")

    #here n is assigned with value of len and then compared with 10
    #2 in one work assignment + comparison