#!/usr/bin/python3
"""
student mod
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "[Student] firstname: {}, lastname: {}, age: {}"\
            .format(self.first_name, self.last_name, self.age)

    def to_json(self, attrs=None):
        dict_obj = {}
        if attrs is None:
            return self.__dict__
        else:
            for att in attrs:
                try:
                    dict_obj = {att: getattr(self, att)}
                except Exception as e:
                    print(e)
            return dict_obj
