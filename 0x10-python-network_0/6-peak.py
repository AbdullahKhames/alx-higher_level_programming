#!/usr/bin/python3
""" function to find_peak in a list """


def find_peak(list_of_integers):
    """ function to find_peak in a list """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
