""" Fizz Buzz
Multiple of 3: fizz
Multiple of 5: buzz
Multiple of 3 and 5: fizzbuzz
"""


def fizz_buzz(n: int):
    [print("fizzbuzz") if i % 3 == 0 and i % 5 == 0
     else print("fizz") if i % 3 == 0
     else print("buzz") if i % 5 == 0
     else print(i)
     for i in range(1, n)]


def fizz_buzz_(n: int):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("buzz")
            continue
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz(50)
