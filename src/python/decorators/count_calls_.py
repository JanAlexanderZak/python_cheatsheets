import functools

# https://www.youtube.com/watch?v=T8CQwGIsrx4&t=11289s&ab_channel=PyCon2020


# Implementation as function
def count_calls(func):

    @functools.wraps(func)
    def _count_calls(*args, **kwargs):

        # Before functon
        _count_calls.num_calls += 1

        value = func(*args, **kwargs)
        return value

    # Assign attribute to func, gets executed first"
    _count_calls.num_calls = 0
    return _count_calls


@count_calls
def fibonacci(number):
    # Stop condition, since func is recursive
    if number < 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


fibonacci(7)
print(fibonacci.num_calls)


# Implementation as class
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def fibonacci(number):
    # Stop condition, since func is recursive
    if number < 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


fibonacci(7)
print(fibonacci.num_calls)
