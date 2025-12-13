# type definitions to return the type of an object.

# for variable (:) is used and for function -> is used.

a: int = 5

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(a)          
print(greet("mahir"))
