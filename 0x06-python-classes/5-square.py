#!/usr/bin/python3
"""
this module shows getters and setters the pythony way
"""


class Square:
    """
    class represents square characteristics
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
        method to calculate area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        function to print the squares with the # notation
        """
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
