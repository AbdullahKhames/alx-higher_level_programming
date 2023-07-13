#!/usr/bin/python3
"""
from json file
"""
import json
import os


def load_from_json_file(filename):
    """
    from json file
    :param filename: fle from save from
    :return: None
    """
    if not os.path.exists(filename):
        open(filename, 'w').close()
    with open(filename, 'r', encoding="UTF-8") as fp:
        return json.load(fp)
