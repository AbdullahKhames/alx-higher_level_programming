#!/usr/bin/python3
"""
convert obj to json
"""


def class_to_json(obj):
    """
    converts obj to json
    :param obj: obj to be converted
    :return: object in dictionary form
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
