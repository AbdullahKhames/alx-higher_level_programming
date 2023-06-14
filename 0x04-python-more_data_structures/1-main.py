#!/usr/bin/python3

search_replace = __import__('1-search_replace').search_replace
lis = [1,2,3,4,5,6,7,8,9,2,2,2,10]
print(f"{lis}")
new_lis = search_replace(lis, 2 , 89)
print(f"{lis}")
print(f"{new_lis}")
