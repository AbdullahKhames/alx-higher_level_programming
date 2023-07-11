#!/usr/bin/python3
"""
add_attribute
"""


def add_attribute(obj, key, value):
    """
    add_attribute
    :param obj: object to add to
    :param key: the key of attribute
    :param value: value of atr
    :return: no return
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")

