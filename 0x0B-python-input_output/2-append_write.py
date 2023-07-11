#!/usr/bin/python3
"""
append file module
"""


def append_write(filename="", text=""):
    """
    append file function
    :param text: text to append
    :param filename: file to open
    :return:no return
    """
    with open(filename, 'a', encoding="UTF-8") as fp:
        red = fp.write(text)
        return red
