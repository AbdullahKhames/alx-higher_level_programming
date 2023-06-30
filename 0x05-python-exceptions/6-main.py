#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg
try:
    raise_exception_msg("hello")
except NameError as ne:
    print("{}".format(ne))
    