#!/usr/bin/python3
"""
square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size):
        """
        init method
        :param size: size
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        function to calculate area
        :return: power 2 of size
        """
        return self.__size * self.__size
