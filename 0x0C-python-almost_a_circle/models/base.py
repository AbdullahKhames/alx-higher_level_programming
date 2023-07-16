#!/usr/bin/python3
"""
base class
"""


class Base:
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        :param id: id for project's objects
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            if not type(id) is int:
                raise TypeError("id must be an integer")
            if id <= 0:
                raise ValueError("id cannot be <= 0")
            self.id = id
