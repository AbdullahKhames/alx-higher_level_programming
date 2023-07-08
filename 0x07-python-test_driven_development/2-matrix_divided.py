#!/usr/bin/python3
"""
This is the "02-matrix_div" module.
"""


def matrix_divided(matrix=None, div=None):
    """
    the function to divide a matrix
    :param matrix: a list of lists of integers or floats
    :param div:must be a number (integer or float)
    :return:a new matrix
    """
    if matrix is None:
        raise TypeError("matrix cannot be none")

    if div is None:
        raise TypeError("div cannot be none")

    check_div(div)
    check_zero(div)
    list_checker(matrix)
    size_checker(matrix)
    new_outer_matrix = []
    for outer in matrix:
        new_inner_matrix = []
        for inner in outer:
            new_inner_matrix.append(round(divide(inner, div), 2))
        new_outer_matrix.append(new_inner_matrix)
    return new_outer_matrix


def divide(x, y):
    return x / y


def list_checker(lists):
    for x in lists:
        for y in x:
            if not check_value(y):
                return False
    return True


def check_value(x):
    if isinstance(x, int) or isinstance(x, float):
        return True
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


def check_zero(x):
    if x == 0:
        raise ZeroDivisionError("division by zero")


def check_div(x):
    if type(x) not in [int, float]:
        raise TypeError("div must be a number")


def size_checker(lists):
    first_size = 0
    idx = 0
    for x in lists:
        for y in x:
            first_size += 1
        break
    for x in lists:
        for y in x:
            idx += 1
        if first_size != idx:
            raise TypeError("Each row of the matrix must have the same size")
        idx = 0
    return True
