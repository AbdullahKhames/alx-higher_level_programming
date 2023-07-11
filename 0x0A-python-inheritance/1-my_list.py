#!/usr/bin/python3
"""
module mylist
"""


class MyList(list):
    """
    class my list
    """

    @staticmethod
    def check_value(x):
        """
        value validator
        :param x: the value
        :return: no return
        """
        if not isinstance(x, int):
            raise TypeError("value must be int")
        return True

    def print_sorted(self):
        """
        function to print
        :return: no return
        """
        try:
            for i in self:
                if not MyList.check_value(i):
                    return
        except TypeError as e:
            print(f"TypeError: {e}")
            return

        sorted_list = sorted(self)
        print(sorted_list)
