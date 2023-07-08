#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
module = __import__("2-matrix_divided")
print(module.size_checker([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3]]))
print(module.list_checker([[1, 2, 3], [1, 2, 3, "4"], [1, 2, 3]]))
