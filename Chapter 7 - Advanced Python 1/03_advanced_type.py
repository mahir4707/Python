from typing import List, Tuple, Dict, Union, Optional

#list
numbers: List[int] = [1, 2, 3, 4, 5]

#tuple
person: Tuple[str, int] = ("Alice", 30)

#dictionary
employee: Dict[str, int] = {"Mahir": 101, "John": 102}

#union
identifier: Union[int, str] = "ABC123"
identifier = 456

print(numbers)
print(person)
print(employee)
print(identifier)
