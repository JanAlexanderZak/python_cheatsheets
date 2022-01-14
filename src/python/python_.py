# Notations
x1 = 0x12
x2 = hex(18)
x3 = bin(18)

print("Binary: \t\t", x1,
      "\nHexadecimal: \t", x2,
      "\nOctal: \t\t\t", x3,
      "\nScientific: \t", 2e2)

bytes = (1024).to_bytes(2, byteorder='little')
print(bytes)

s = b'string'
s_encode = str(s, encoding='utf-8')
s_decode = s.decode()

# Strings
points = 50
phrase = "points to Gryffindor"

print("{} {}".format(points, phrase))
print("{points} {phrase}".format(points=points, phrase=phrase))
print(points, phrase)
print("%d %s" % (points, phrase))
print("%(points)d %(phrase)s" % {"points": points, "phrase": phrase})
print(f"{points} {phrase}")

s = "string"
print(s.center(10, "*"))
print(s.ljust(10, "*"))
print(s.rjust(10, "*"))
print(s.zfill(10))

# value, start, end
s = "string_substring_name"
print(s.startswith("name", 2))

# value, start, end
s = "string_substring_name"
print(s.endswith("name"))

s = "abcdefghijklmnopqrstuvwxyz"
print(s.find("i"))
print(s.index("i"))

s = "abcdefghijklmnopqrstuvwxyz"
print(s.find("de"))
print(s.find("de", 5))
print(s.find("de", 5, 10))

print(s.count("de"))
print(s.count("d"))

# repr()
my_sting = '\nHello, world!'
print(my_sting)
print(repr(my_sting))

# Dictionaries
en_de = {
    "red": "rot",
    21: "twenty_one",
    (1, 2): "coordinate",
}
print("red" in en_de)
print(dict.fromkeys(en_de, "red").items())


for key in en_de:
    print("{}: {}".format(key, en_de[key]))


# Enumerate
dict_ = dict({'1': '1', '2': 'b'})
for key, value in dict_.items():
    print(key, value)


# Zip
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']
z = zip(numbers, letters)
l = list(z)
print(l)


# List comprehension
num_list = [num for num in range(10) if num % 2 == 0]
print(num_list)

# Dict comprehension
num_dict = {str(num): num for num in range(9) if num % 2 == 0}
print(num_dict)

# Generator comprehension
num_generator = (num for num in range(10) if num % 2 == 0)
print(num_generator)


# Functions
def g():
    print("G")


def f1(func):
    print("F")
    func()


def f2(x):
    def g_(y):
        return(x + y + 3)
    return g_


print(f1(g))
x = f2(1)
print(x(1))


# Function as first class object
def say_hello(name, logger):
    logger(f'Hello {name}')


say_hello('world', logger=print)


# Classes
class Robot1:
    pass


x = Robot1()
x.name = "Alex"
Robot1.name = "name"
print(Robot1.__dict__)


class Robot2:
    def __init__(self):
        pass

    def __del__(self):
        print("Roboter 2 was destroyed")


x = Robot2()
del x


class Fraction:
    def __init__(self, z, n):
        self.__z = z
        self.__n = n

    def __str__(self):
        return str(self.__z) + "/" + str(self.__n)

    # greatest common divisor
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def reduce(self):
        g = Fraction.gcd(self.__z, self.__n)
        self.__z = self.__z // g
        self.__n = self.__n // g
        return str(self.__z) + "/" + str(self.__n)


fraction = Fraction(2, 6)
print(fraction.reduce())


# Generators
cities = ["Berlin", "Munich"]
for city in cities:
    print(city)


def city_generator(array):
    for entry in array:
        yield(entry)


for value in city_generator(cities):
    print(value)


generator = city_generator(cities)
next(generator)


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n-1)


factorial(10)
