#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = {}
    for k, v in a_dictionary.items():
        b[k] =  v *2
    return b
b= multiply_by_2({'a': 2, 'b':3, 'c':7})

print(f"{b}")
