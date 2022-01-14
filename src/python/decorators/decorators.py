import numpy as np
import functools


# This is a template for decorators
# Rename wrapper function, outer "wrapper"
# Underscore inner function
def wrapper(func):
    # Decorator factory
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # Some calculation before
        print(f'Before {func.__name__}')

        # Call the function
        value = func(*args, **kwargs)

        # Some calculation after
        print(f'After {func.__name__}')
        print("Altered value from wrapper: ", value + 1)

        # Usually return the value
        return value

    return _wrapper


@wrapper
def dice_roll():
    """Custom docstring"""
    random_value = np.random.randint(1, 10)
    value_ = "True value from func: " + str(random_value)
    print(value_)
    return random_value


print(dice_roll())
print(dice_roll.__name__, dice_roll.__doc__)

# TEMPLATE
#
# import functools
#
#
# def wrapper(func):
#     """Template for decorators"""
#
#     @functools.wraps(func)
#     def _wrapper(*args, **kwargs):
#         """The wrapper function replacing the original"""
#         # Do something before calling the function
#         value = func(*args, **kwargs)
#         # Do something after calling the function
#         return value
#
#     return _wrapper

print("#" * 80)


# Basic logic of decorators
# Inner and outer functions
def outer():
    print('Outer function')

    def inner():
        print('Inner function')

    # Call inner function from local scope
    inner()
outer()


# Manipulate functions
def hello(func):
    print(f'Hello {func.__name__}')
    return func
hello(outer)  # With call of outer function


print("#" * 80)


# Decorate
def wrapper(func):
    print(f'Before {func.__name__}')
    func()
    print(f'After {func.__name__}')
wrapper(outer)


print("#" * 80)


@wrapper
def outer():
    print('Outer function')

    def inner():
        print('Inner function')
    # Call inner function from local scope
    inner()
