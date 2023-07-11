#!/usr/bin/python3
"""
base geo
"""


class BaseGeometry:
    """
    class base geo
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        value validator
        :param name: name
        :param value: value
        :return: value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
