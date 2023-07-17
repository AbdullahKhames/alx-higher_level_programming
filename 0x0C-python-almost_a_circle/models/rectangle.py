#!/usr/bin/python3
"""
rect module
"""

Base = __import__('base').Base


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
        self.__class__.int_validator(width, 'width')
        self.__class__.int_validator(height, 'height')
        self.__class__.int_validator(x, 'x')
        self.__class__.int_validator(y, 'y')
        self.__class__.value_validator(width, 'width')
        self.__class__.value_validator(height, 'height')
        self.__class__.dimensions_validator(x, 'x')
        self.__class__.dimensions_validator(y, 'y')

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
        self.__class__.int_validator(width, 'width')
        self.__class__.value_validator(width, 'width')
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
        self.__class__.int_validator(height, 'width')
        self.__class__.value_validator(height, 'width')
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
        self.__class__.int_validator(x, 'x')
        self.__class__.dimensions_validator(x, 'x')
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
        self.__class__.int_validator(y, 'y')
        self.__class__.dimensions_validator(y, 'y')
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

    def update(self, *args, **kwargs):
        """
        update instance
        :param args: args to be updated
        :param kwargs: kwargs to be updated if ars in none
        :return: none
        """
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        for k, v in enumerate(args):
            attribute = attribute_names[k]
            self.__class__.none_checker(v)
            self.__class__.int_validator(v, attribute)
            if attribute in ('x', 'y'):
                self.__class__.dimensions_validator(v, attribute)
            else:
                self.__class__.value_validator(v, attribute)
            setattr(self, attribute, v)

            # if k == 0:
            #     self.__class__.none_checker(v)
            #     self.__class__.int_validator(v, "id")
            #     self.__class__.value_validator(v, "id")
            #     self.id = v
            # elif k == 1:
            #     self.__class__.none_checker(v)
            #     self.__class__.int_validator(v, 'width')
            #     self.__class__.value_validator(v, 'width')
            #     self.__width = v
            # elif k == 2:
            #     self.__class__.none_checker(v)
            #     self.__class__.int_validator(v, 'height')
            #     self.__class__.value_validator(v, 'height')
            #     self.__height = v
            # elif k == 3:
            #     self.__class__.none_checker(v)
            #     self.__class__.int_validator(v, 'x')
            #     self.__class__.dimensions_validator(v, 'x')
            #     self.__x = v
            # elif k == 4:
            #     self.__class__.none_checker(v)
            #     self.__class__.int_validator(v, 'y')
            #     self.__class__.dimensions_validator(v, 'y')
            #     self.__y = v

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__class__.int_validator(val, key)
                if key in ('x', 'y'):
                    self.__class__.dimensions_validator(val, key)
                else:
                    self.__class__.value_validator(val, key)
                if hasattr(self, key):
                    setattr(self, key, val)

    def __str__(self):
        """
        :return: a string representation of class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    @staticmethod
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

    @staticmethod
    def value_validator(value, s):
        """
        validates the value sent to it
        :param value:value t o be checked
        :param s: param name
        :return: none
        """
        if value <= 0:
            raise ValueError(s + ' must be > 0')

    @staticmethod
    def dimensions_validator(value, s):
        """
        dimensions validator
        :param value: value to be checked
        :param s: param name
        :return: none
        """
        if value < 0:
            raise ValueError(s + ' must be >= 0')

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
