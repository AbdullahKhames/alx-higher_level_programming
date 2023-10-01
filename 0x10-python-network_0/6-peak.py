#!/usr/bin/python3
""" function to find_peak in a list """
def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    min_int = list_of_integers[0]
    for i in list_of_integers:
        if i > min_int:
            min_int = i
    return min_int
