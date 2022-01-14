""" Prime Numbers
Example: 2, 3, 5, 7, 11, 13, 17
"""


def prime_numbers(_interval: list):
    assert len(_interval) == 2
    for num in range(_interval[0], _interval[1] + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num


if __name__ == '__main__':
    interval = [0, 100]
    print(len(interval))
    generator = prime_numbers([0, 100])
    print(*generator)
