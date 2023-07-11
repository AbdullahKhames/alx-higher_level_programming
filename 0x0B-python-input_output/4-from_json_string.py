#!/usr/bin/python3
"""
from json
"""
import json


def from_json_string(my_str):
    """
    from json
    :param my_str: str to convert
    :return: JSON representation of an object (string)
    """
    json_dict = json.loads(my_str)
    return json_dict
