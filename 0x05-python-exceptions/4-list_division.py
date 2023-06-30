#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(div(my_list_1, my_list_2, i))
            except TypeError:
                print("wrong type")
                new_list.append(0)

            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)

            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list


def check_instance(element):
    if isinstance(element, float) or isinstance(element, int):
        return True
    else:
        raise TypeError


def check_idx(l1, l2, idx):
    if len(l1) <= idx or len(l2) <= idx:
        raise IndexError
    elif check_instance(l1[idx] and check_instance(l2[idx])):
        return True


def div(l1, l2, idx):
    if check_idx(l1, l2, idx):
        if l2[idx] == 0:
            raise ZeroDivisionError
        return l1[idx] / l2[idx]
    else:
        return 0
