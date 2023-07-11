#!/usr/bin/python3
"""
to json
"""
import json


def to_json_string(my_obj=None):
    """
    to json
    :param my_obj: obj to convert
    :return: JSON representation of an object (string)
    """
    json_str = json.dumps(my_obj)
    return json_str
