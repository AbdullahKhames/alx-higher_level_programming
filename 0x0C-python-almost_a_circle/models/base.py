#!/usr/bin/python3
"""
base class
"""


import json
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs=None):
        fileName = cls.__name__ + ".json"
        with open(fileName, 'w') as fp:
            dictionaries = []
            if list_objs is None:
                fp.write(Base.to_json_string(dictionaries))
            else:
                for obj in list_objs:
                    dictionaries.append(obj.to_dictionary())
                fp.write(Base.to_json_string(dictionaries))

    @staticmethod
    def to_json_string(list_dictionaries=None):
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = Rectangle(1, 2)
        elif cls.__name__ == 'Square':
            obj = Square(5)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        instances = []
        with open(cls.__name__ + ".json") as fp:
            json_string = fp.read()
            dicts = cls.from_json_string(json_string)

        for obj in dicts:
            instance = cls.create(**obj)
            instances.append(instance)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()

        t = turtle.Turtle()

        t.speed(1)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.fillcolor('blue')  # Set the fill color to blue
            t.begin_fill()  # Begin the shape filling
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.end_fill()  # End the shape filling

        # Draw squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.fillcolor('red')  # Set the fill color to red
            t.begin_fill()  # Begin the shape filling
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.end_fill()  # End the shape filling

        # Close the turtle graphics window when done
        turtle.done()
