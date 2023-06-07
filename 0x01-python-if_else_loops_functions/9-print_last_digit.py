#!/usr/bin/env python3
def print_last_digit(number):
    assert isinstance(number, (int, float)), "Value is not a number."
    x = abs(number) % 10
    print("{}".format(x), end = '')
    return x
