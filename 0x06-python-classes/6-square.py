#!/usr/bin/python3
"""
this module shows getters and setters the python way
"""


class Square:
    """
    class represents square characteristics
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        init method
        """
        if validate_size(size):
            self.__size = size
        if validate_position(position[0]) and validate_position(position[1]):
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        if validate_position(value[0]) and validate_position(value[1]):
            self.__position = value

    def my_print(self):
        """
        function to print the squares with the # notation
        """
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for _ in range(self.position[1]):
                print()
            for c in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()


def validate_size(value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    return True


def validate_position(value):
    if not isinstance(value, int) or value < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
    return True
