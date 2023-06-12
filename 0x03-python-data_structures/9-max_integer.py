#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length <= 0:
        return
    max = -99999999999999999999
    for i in my_list:
        if i > max:
            max = i
    return max
