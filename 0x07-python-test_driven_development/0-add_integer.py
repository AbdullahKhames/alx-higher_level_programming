#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Return the addition of two numbers."""
    a = check_value(a, "a")
    b = check_value(b, "b")
    return a + b


def check_value(x, s):
    if isinstance(x, int) or isinstance(x, float):
        return int(x)
    else:
        raise TypeError(s + " must be an integer")
