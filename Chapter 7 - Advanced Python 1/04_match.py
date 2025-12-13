# match statement is used as switch statement like in other languages

def greet(status):
    match status:
        case 1:
            return "Hello!"
        case 2:
            return "Bonjour!"
        case _:
            return "Namaste!"
        
print(greet(1))  # Output: Hello!
print(greet(2))  # Output: Bonjour!     
print(greet(3))  # Output: Namaste!