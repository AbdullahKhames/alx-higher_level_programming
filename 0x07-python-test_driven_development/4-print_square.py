#!/usr/bin/python3
def print_square(size):
    check_type(size)
    check_value(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


def check_value(x):
    if isinstance(x, float) and x < 0:
        raise TypeError("size must be an integer")
    elif isinstance(x, int) and x < 0:
        raise ValueError("size must be >= 0")


def check_type(x):
    if isinstance(x, float) or isinstance(x, int):
        return True
    else:
        raise TypeError("size must be an integer")

try:
    print(print_square(-.8))
except TypeError as ex:
    print(ex)
