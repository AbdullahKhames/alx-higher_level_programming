#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if (x >= 97) and (x <= 122):
            c = chr(x - 32)
        print("{:s}".format(c), end = "")
    print()
