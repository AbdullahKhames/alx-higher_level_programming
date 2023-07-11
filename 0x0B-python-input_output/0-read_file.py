#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    """
    read file function
    :param filename: file to open
    :return:no return
    """
    try:
        with open(filename, encoding="UTF-8") as fp:
            red = fp.read()
            print(red)
            return red
    except Exception as e:
        print(e)
