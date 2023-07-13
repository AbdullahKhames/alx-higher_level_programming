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
    opt = [0]
    for row in range(n):
        inner_ls = [1]
        opt = init_new_row(row, inner_ls, opt)
        ls.append(inner_ls)
    return ls


def init_new_row(row, ls=None, opt=[]):
    ret = [1]
    accum_ls = []
    if ls is None:
        ls = [1]

    for col in range(row):
        ls.append(1)

    for col in ls:
        if row > 3:
            ls[1] = row
            ls[-2] = row
    if row <= 5:
        if opt[0] > 0:
            x = int(row / 2)
            if (row + 1) % 2 == 0:
                ls[x] = opt[0]
                ls[x + 1] = opt[0]
            else:
                ls[int(x)] = opt[0]
            if row == 5:
                temp = ls[1]
                for i in ls[2:-1]:
                    accum_ls.append((temp + i))
                    temp = i
                return accum_ls
            ret = [ls[x] + ls[x + 1]]
        return ret
    else:
        for k, j in enumerate(ls[2:-2]):
            ls[k + 2] = opt[k]
        temp = ls[1]
        for i in ls[2:-1]:
            accum_ls.append((temp + i))
            temp = i
        return accum_ls
