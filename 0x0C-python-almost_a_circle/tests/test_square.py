#!/usr/bin/python3
"""
test square
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test square
    """

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
