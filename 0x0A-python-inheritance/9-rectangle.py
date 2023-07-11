#!/usr/bin/python3
"""
mod
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rect
    """
    def __init__(self, width, height):
        """
        init method
        :param width: width
        :param height: height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        function to calculate rect area
        :return: area = width * height
        """
        return self.__width * self.__height

    def __str__(self):
        """
        function to represent the rect in string format
        :return:
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
