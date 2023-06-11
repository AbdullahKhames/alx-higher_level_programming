#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for element in my_string:
        if element == 'c' or element == 'C':
            continue
        s += element
    return s
