#!/usr/bin/python3
import json
"""
to json
"""


def to_json_string(my_obj=None):
    """
    to json
    :param my_obj: obj to convert
    :return: JSON representation of an object (string)
    """
    if my_obj is None:
        return None
    elif type(my_obj) is not dict and  hasattr(my_obj, '__dict'):
        my_obj = my_obj.__dict__
    json_str = json.dumps(my_obj)
    return json_str
