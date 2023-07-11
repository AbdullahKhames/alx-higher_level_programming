#!/usr/bin/python3
"""
from json file
"""
import json


def load_from_json_file(filename):
    """
    from json file
    :param filename: fle from save from
    :return: None
    """
    with open(filename, 'r', encoding="UTF-8")as fp:
        return json.load(fp)
