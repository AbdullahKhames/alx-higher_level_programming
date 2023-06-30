#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    try:
        for i in range(x):
            if not isinstance(my_list[i], int):
                continue
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        print()
        return counter
    except IndexError as ex:
        return ex
        # print()
        # return counter
