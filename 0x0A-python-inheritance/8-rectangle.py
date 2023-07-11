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
