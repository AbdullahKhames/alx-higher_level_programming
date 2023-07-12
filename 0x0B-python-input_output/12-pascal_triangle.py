#!/usr/bin/python3
"""
pascal triangle problem
"""


def pascal_triangle(n):
    """
    pascal triangle
    :param n: number of rows
    :return: list of lists
    """
    if not type(n) is int:
        raise TypeError("n must me an integer")
    if n <= 0:
        return []
    ls = []
    for row in range(n):
        print(row)
        inner_ls = init_new_row(row)
        if check_each_row(row, inner_ls):
            ls.append(inner_ls)
        # init_diagonal(0, ls)
    return ls


def init_new_row(row):
    ls = [0]
    for col in range(row):
        ls.append(col)
    if row == 0:
        ls[row] = 1
    else:
        ls[0] = 1
        ls[-1] = 1
    if row >= 2:
        ls[1] = row
        ls[-2] = row
    return ls


def check_each_row(row=0, ls=None):
    if ls is None:
        ls = []
    accumulator = 0
    for col in ls:
        accumulator += col
    return accumulator == get_pow(row)


def get_pow(n=0):
    return 2 ** n


def init_diagonal(row=0, ls=None):
    if ls is None:
        ls = []

    for count, new_list in enumerate(ls):
        if count == 0 or count == 1:
            continue
        new_list[1] = count
        new_list[-2] = count


print(pascal_triangle(7))
print(check_each_row(2, [1, 2, 1]))


