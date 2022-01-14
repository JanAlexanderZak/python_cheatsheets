""" Fibonacci Numbers
Example: 1, 1, 2, 3, 5, 8, ...
Formula: Xn = Xn-1 + Xn-2 ; must start with Xn-1 = 0 and Xn-2 = 1
"""


def fibonacci_numbers(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            yield b


if __name__ == '__main__':
    generator = fibonacci_numbers(20)
    [print(number) for number in generator]
    print(*generator)  # empty
