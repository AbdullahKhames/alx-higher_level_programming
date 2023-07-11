#!/usr/bin/python3
"""
to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    to json file
    :param my_obj: obj to save
    :param filename: fle to save to
    :return: None
    """
    with open(filename, 'w', encoding="UTF-8")as fp:
        json.dump(my_obj, fp)
