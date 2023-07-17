#!/usr/bin/python3
"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.square = Square(5)
        cls.square1 = Square(5, 3)
        cls.square2 = Square(3, 2, 2)
        cls.square3 = Square(6, 5, 10, 10)
        cls.square4 = Square(2, 3, 2)

    def test_square(self):
        self.assertEqual(self.square.id, 64)
        self.assertEqual(self.square2.id, 66)
        self.assertEqual(self.square3.id, 10)
        self.assertEqual(self.square4.id, 67)

    def test_square1(self):
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square2.width, 3)
        self.assertEqual(self.square3.width, 6)
        self.assertEqual(self.square4.width, 2)

    def test_square2(self):
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square2.height, 3)
        self.assertEqual(self.square3.height, 6)
        self.assertEqual(self.square4.height, 2)

    def test_square3(self):
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square2.x, 2)
        self.assertEqual(self.square3.x, 5)
        self.assertEqual(self.square4.x, 3)

    def test_square4(self):
        self.assertEqual(self.square.y, 0)
        self.assertEqual(self.square2.y, 2)
        self.assertEqual(self.square3.y, 10)
        self.assertEqual(self.square4.y, 2)


if __name__ == '__main__':
    unittest.main()
