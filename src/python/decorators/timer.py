import functools
import time

# https://www.youtube.com/watch?v=T8CQwGIsrx4&t=11289s&ab_channel=PyCon2020


def timer(func):

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Elapsed time: {toc - tic:.2f} seconds")
        return value

    return _timer


@timer
def waste_time(number):
    total = 0
    for num in range(number):
        total += sum(n for n in range(num))
    return total


print(waste_time(1000))
