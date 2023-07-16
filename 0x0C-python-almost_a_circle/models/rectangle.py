#!/usr/bin/python3
"""
rect module
"""

from models.base import Base


class Rectangle(Base):
    """
    class rectangle
    """

    def __init__(self, width=None, height=None, x=0, y=0, id=None):
        """
        init method to initialize the class
        """
        if width is None or height is None \
                or x is None or y is None:
            raise TypeError("cannot be None")
        int_validator(width, 'width')
        int_validator(height, 'height')
        int_validator(x, 'x')
        int_validator(y, 'y')
        value_validator(width, 'width')
        value_validator(height, 'height')
        dimensions_validator(x, 'x')
        dimensions_validator(y, 'y')

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter for property
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter for property
        """
        Rectangle.none_checker(width)
        int_validator(width, 'width')
        value_validator(width, 'width')
        self.__width = width

    @property
    def height(self):
        """
        getter for property
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter for property
        """
        int_validator(height, 'width')
        value_validator(height, 'width')
        Rectangle.none_checker(height)
        self.__height = height

    @property
    def x(self):
        """
        getter for property
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter for property
        """
        Rectangle.none_checker(x)
        int_validator(x, 'x')
        dimensions_validator(x, 'x')
        self.__x = x

    @property
    def y(self):
        """
        getter for property
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for property
        """
        Rectangle.none_checker(y)
        int_validator(y, 'y')
        dimensions_validator(y, 'y')
        self.__y = y

    @staticmethod
    def none_checker(value):
        """
        staticmethod to check if a value is none or not
        """
        if value is None:
            raise TypeError("cannot be None")

    def area(self):
        """
        function to calculate rectangle area
        :return: area of rect
        """
        return self.__height * self.__width

    def display(self):
        """
        function to display rectangle with #
        :return: no return
        """
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def update(self, *args):
        """
        update instance
        :param args: args to be updated
        :return: none
        """
        for k, v in enumerate(args):
            if k == 0:
                self.id = v
            elif k == 1:
                self.__class__.none_checker(v)
                int_validator(v, 'width')
                value_validator(v, 'width')
                self.__width = v
            elif k == 2:
                self.__class__.none_checker(v)
                int_validator(v, 'height')
                value_validator(v, 'height')
                self.__height = v
            elif k == 3:
                self.__class__.none_checker(v)
                int_validator(v, 'x')
                dimensions_validator(v, 'x')
                self.__x = v
            elif k == 4:
                self.__class__.none_checker(v)
                int_validator(v, 'y')
                dimensions_validator(v, 'y')
                self.__y = v
        pass

    def __str__(self):
        """
        :return: a string representation of class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


def int_validator(value, s):
    """
    int calidator
    :param value: value to validate
    :param s: the name of parameter
    :return: True in case all good
    """
    if not isinstance(value, int):
        raise TypeError(s + ' must be an integer')
    return True


def value_validator(value, s):
    """
    validates the value sent to it
    :param value:value t o be checked
    :param s: param name
    :return: none
    """
    if value <= 0:
        raise ValueError(s + ' must be > 0')


def dimensions_validator(value, s):
    """
    dimensions validator
    :param value: value to be checked
    :param s: param name
    :return: none
    """
    if value < 0:
        raise ValueError(s + ' must be >= 0')
