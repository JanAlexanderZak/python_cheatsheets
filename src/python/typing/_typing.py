import types
from typing import List, Union
from decimal import Decimal


Number = Union[                 # Define a type
    int,
    float,
    complex,
    Decimal,
]

print(list(str(float(34))))     # type gets converted to string

print(isinstance(42, int))      # list, int, str is a class

print(dir(types))

users: List[int] = []
users.append(32)
users.append('S')               # This throws an mypy error
print(users)


def func(a: int, b: str):       # Problem is, that you dont know what type is required as input. Mby type error
    assert type(a) is int       # Force an error


print(func('2', '2'))
print(func.__annotations__)     # Print all type hints
