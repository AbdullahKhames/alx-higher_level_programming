#!/usr/bin/python3
"""
write file module
"""


def write_file(filename="", text=""):
    """
    write file function
    :param text: text to be written
    :param filename: file to open
    :return:no return
    """
    with open(filename, "w", encoding="UTF-8") as fp:
        return fp.write(text)
