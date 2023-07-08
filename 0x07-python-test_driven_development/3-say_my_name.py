#!/usr/bin/python3
"""
module to say my name
"""


def say_my_name(first_name=None, last_name=""):
    """
    function to say my name
    :param first_name: firstname
    :param last_name: lastname
    :return: no return
    """
    check_value(first_name, "first_name")
    check_value(last_name, "last_name")
    print(f"My name is {first_name} {last_name}")


def check_value(val, s):
    if not isinstance(val, str):
        raise TypeError(s + " must be a string")
