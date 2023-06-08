#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0")
    else:
        sum = 0
        for i in range(length):
            sum += int(argv[i + 1])
        print("{}".format(sum))
