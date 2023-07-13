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
        return "[Student] firstname: {}, lastname: {}, age: {}" \
            .format(self.first_name, self.last_name, self.age)

    def to_json(self, attrs=None):
        dict_obj = {}
        if attrs is None:
            return self.__dict__
        else:
            dict_obj = {}
            for att in attrs:
                if hasattr(self, att):
                    dict_obj[att] = getattr(self, att)
            return dict_obj

    def reload_from_json(self, json):
        if not type(json) is dict:
            return
        if self is None:
            Student(json["first_name"], json["last_name"], json["age"])
        else:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
