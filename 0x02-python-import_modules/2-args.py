#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(length):
            print("{}: {}".format(i + 1, argv[i + 1]))
