#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lis = my_list.copy()
    for i in range(len(lis)):
        if lis[i] == search:
            lis[i] = replace
    return lis
