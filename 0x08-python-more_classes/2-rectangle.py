#!/usr/bin/python3
"""
rectangle module
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        if int_validator(width, 'width') \
                and value_validator(width, 'width'):
            self.__width = width
        if int_validator(height, 'height') \
                and value_validator(height, 'height'):
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if int_validator(width, 'width') \
                and value_validator(width, 'width'):
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if int_validator(height, 'height') \
                and value_validator(height, 'height'):
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)


def int_validator(value, s):
    if not isinstance(value, int):
        raise TypeError(s + ' must be an integer')
    return True


def value_validator(value, s):
    if value < 0:
        raise ValueError(s + ' must be >= 0')
    return True
