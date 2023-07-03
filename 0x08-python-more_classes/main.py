#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle
r = Rectangle(3, 6)
print(r.width)
print(r.height)
print(r.__dict__)
r.width = 5
r.height = 20
print(r.width)
print(r.height)
print(r.__dict__)