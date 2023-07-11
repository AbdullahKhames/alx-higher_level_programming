#!/usr/bin/python3
"""
rebel int module
"""


class MyInt(int):
    """
    rebel int class
    """
    def __new__(cls, value):
        """
        calling super __new__
        """
        return super().__new__(cls, value)

    def __ne__(self, other):
        """
        rebelling against int
        :param other: other value to compare to
        :return: True if equals false if not
        """
        return super().__eq__(other)

    def __eq__(self, other):
        """
        rebelling against int
        :param other: other value to compare to
        :return: false if equals true if not
        """
        return super().__ne__(other)
