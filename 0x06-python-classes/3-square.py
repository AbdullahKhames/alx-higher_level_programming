#!/usr/bin/python3

"""
this is new module
"""


class Square:
    """
    new class
    """

    def __init__(self, size=0):
        """
        init method
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        mthod to calculate area of square
        """
        return self.__size * self.__size
