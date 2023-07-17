#!/usr/bin/python3
"""
square module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        method to initialize square
        :param size: instead of width and height
        :param x: x
        :param y: y
        :param id: id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overrides the str function
        :return: return string rep of class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter
        :return: return size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        setter for size
        :param size: size
        :return: none
        """
        Rectangle.int_validator(size, 'width')
        Rectangle.value_validator(size, 'width')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        update the arguments
        :param args: args
        :param kwargs: kwargs
        :return: none
        """
        attrs = ['id', 'width', 'x', 'y']
        if args:
            for k, v in enumerate(args):
                att = attrs[k]
                Rectangle.none_checker(v)
                Rectangle.int_validator(v, att)
                if att in ['x', 'y']:
                    Rectangle.dimensions_validator(v, att)
                else:
                    Rectangle.value_validator(v, att)
                setattr(self, att, v)
                if att == 'width':
                    self.height = v
        elif kwargs:
            for key, value in kwargs.items():
                Rectangle.none_checker(value)
                Rectangle.int_validator(value, key)
                if key in ['x', 'y']:
                    Rectangle.dimensions_validator(value, key)
                else:
                    Rectangle.value_validator(value, key)
                if hasattr(self, key):
                    setattr(self, key, value)
                    if key == 'width':
                        self.height = value

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
