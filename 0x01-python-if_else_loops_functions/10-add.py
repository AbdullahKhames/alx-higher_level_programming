#!/usr/bin/python3
def add(a, b):
    assert isinstance(a, (int, float)), "a is not a number."
    assert isinstance(b, (int, float)), "b is not a number."
    return a + b
