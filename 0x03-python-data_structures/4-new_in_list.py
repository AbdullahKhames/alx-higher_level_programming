#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    a = my_list.copy()
    if idx < 0:
        return a
    elif idx >= length:
        return a
    else:
        a[idx] = element
        return a
