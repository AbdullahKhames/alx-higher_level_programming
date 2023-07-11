#!/usr/bin/python3
"""
module to check is instance
"""


def is_same_class(obj, a_class):
    """
    funcition to check if same class
    :param obj: the object
    :param a_class: the class
    :return: True if same false otherwise
    """
    return type(obj) is a_class
