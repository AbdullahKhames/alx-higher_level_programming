#!/usr/bin/python3

"""
this is based on last task
"""


class Square:
    """
    this is extenstion of last class
    """

    def __init__(self, size=0):
        """
        initialization method for class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size > 0:
            raise ValueError("size must be >= 0")
        self.__size = size
