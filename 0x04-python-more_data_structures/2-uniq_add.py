#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = my_list.copy()
    uni = set()
    for idx in range(len(my_list)):
        uni.update((my_list[idx],))
    sum = 0
    for elem in uni:
        sum += elem
    return sum
