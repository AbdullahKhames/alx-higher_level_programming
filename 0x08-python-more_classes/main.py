#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle
r = Rectangle(3, 6)
print(r.width)
print(r.height)
print(r.__dict__)
r.width = 5
r.height = 3
print(r.width)
print(r.height)
print(r.__dict__)
print(r.area())

Rectangle1 = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle1(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--"*50)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))