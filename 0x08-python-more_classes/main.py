# #!/usr/bin/python3
# Rectangle = __import__('2-rectangle').Rectangle
# r = Rectangle(3, 6)
# print(r.width)
# print(r.height)
# print(r.__dict__)
# r.width = 5
# r.height = 3
# print(r.width)
# print(r.height)
# print(r.__dict__)
# print(r.area())
#
# Rectangle1 = __import__('3-rectangle').Rectangle
#
# my_rectangle = Rectangle1(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
#
# print(str(my_rectangle))
# print(repr(my_rectangle))
#
# print("--"*50)
#
# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle)
# print(repr(my_rectangle))
#
# Rectangle = __import__('4-rectangle').Rectangle
#
# my_rectangle = Rectangle(2, 4)
# print(str(my_rectangle))
# print("--")
# print(my_rectangle)
# print("--")
# print(repr(my_rectangle))
# print("--")
# print(hex(id(my_rectangle)))
# print("--")
#
# # create new instance based on representation
# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# print(new_rectangle)
# print("--")
# print(repr(new_rectangle))
# print("--")
# print(hex(id(new_rectangle)))
# print("--")
#
# print(new_rectangle is my_rectangle)
# print(type(new_rectangle) is type(my_rectangle))
#
# Rectangle = __import__('5-rectangle').Rectangle
#
# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
#
# del my_rectangle
#
# try:
#     print(my_rectangle)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
#
# Rectangle = __import__('7-rectangle').Rectangle
#
# my_rectangle_1 = Rectangle(8, 4)
# print(my_rectangle_1)
# print("--")
# my_rectangle_1.print_symbol = "&"
# print(my_rectangle_1)
# print(my_rectangle_1.print_symbol)
#
# print("--")
#
# my_rectangle_2 = Rectangle(2, 1)
# print(my_rectangle_2)
# print("--")
# print("before c")
#
# Rectangle.print_symbol = "C"
# print(my_rectangle_2)
# print(my_rectangle_2.print_symbol)
#
# print("--")
#
# my_rectangle_3 = Rectangle(7, 3)
# print(my_rectangle_3)
# print(my_rectangle_3.print_symbol)
#
#
# print("--")
#
# my_rectangle_3.print_symbol = ["C", "is", "fun!"]
# print(my_rectangle_3)
#
# print("--")
#
#

Rectangle = __import__('9-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

sq = Rectangle.square(5)
print(sq.area())
