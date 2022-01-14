import functools
from cheatsheets.python.decorators.timer import timer

# https://www.youtube.com/watch?v=T8CQwGIsrx4&t=11289s&ab_channel=PyCon2020


def trace(func):
    name = func.__name__

    @functools.wraps(func)
    def _trace(*args, **kwargs):

        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {name} ({signature})")

        value = func(*args, **kwargs)

        print(f"{name.capitalize()} returned {value!r}")  # equiv. to repr(value)
        return value

    return _trace


@timer
@trace
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


greet("Alex")
