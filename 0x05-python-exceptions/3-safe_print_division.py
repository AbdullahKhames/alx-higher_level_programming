#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = a / b
    except ZeroDivisionError as ex:
        return None
    finally:
        print("Inside result: {:d}".format(x))
        