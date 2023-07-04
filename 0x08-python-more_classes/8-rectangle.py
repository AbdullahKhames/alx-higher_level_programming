#!/usr/bin/python3
"""
rectangle module
"""


class Rectangle:
    """
    rectangle class
    with 2 public static attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        init method to define instance public
        and protected and private fields for class
        """
        if int_validator(width, 'width') \
                and value_validator(width, 'width'):
            self.__width = width
        if int_validator(height, 'height') \
                and value_validator(height, 'height'):
            self.__height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for the private instance attribute width"""
        if int_validator(width, 'width') \
                and value_validator(width, 'width'):
            self.__width = width

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for the private instance attribute height"""
        if int_validator(height, 'height') \
                and value_validator(height, 'height'):
            self.__height = height

    def area(self):
        """function to calculate rect area"""
        return self.__width * self.__height

    def perimeter(self):
        """function to calculate rect perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        rect = ""
        if self.__width != 0 and self.__height != 0:
            rect += "\n".join("{}".format(self.print_symbol) * self.__width
                              for j in range(self.__height))
        return rect

    def __repr__(self):
        """returns string representation of class"""
        return "{}({}, {})" \
            .format(self.__class__.__name__, self.width, self.height)

    def __del__(self):
        """prints rught befort obj destruction"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_validator(rect_1, 'rect_1') \
                and rect_validator(rect_2, 'rect_2'):
            return rect_1.area() \
                if rect_1.area() > rect_2.area() else rect_2.area()


def int_validator(value, s):
    if not isinstance(value, int):
        raise TypeError(s + ' must be an integer')
    return True


def value_validator(value, s):
    if value < 0:
        raise ValueError(s + ' must be >= 0')
    return True


def rect_validator(rectangle, s):
    if not isinstance(rectangle, Rectangle):
        raise TypeError(s + ' must be an instance of Rectangle')
    return True
