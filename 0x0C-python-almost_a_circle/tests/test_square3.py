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
        cls.square3 = Square(6, 5, 10)
        cls.square4 = Square(2, 3, 2)

    def test_square1(self):
        self.assertEqual(self.square.id, 70)
        self.square.update(80)
        self.assertEqual(self.square.id, 80)
        self.square.update(id=88)
        self.assertEqual(self.square.id, 88)

    def test_square5(self):
        self.assertEqual(self.square1.width, 5)
        self.square1.update(80, 80)
        self.assertEqual(self.square1.width, 80)
        self.square1.update(size=88)
        self.assertEqual(self.square1.width, 88)

    def test_square2(self):
        self.assertEqual(self.square2.height, 3)
        self.square2.update(80, 80)
        self.assertEqual(self.square2.height, 80)
        self.square2.update(width=88)
        self.assertEqual(self.square2.height, 88)

    def test_square3(self):
        self.assertEqual(self.square3.x, 5)
        self.square3.update(80, 80, 10)
        self.assertEqual(self.square3.x, 10)
        self.square3.update(x=88)
        self.assertEqual(self.square3.x, 88)

    def test_square4(self):
        self.assertEqual(self.square4.y, 2)
        self.square4.update(80, 80, 10, 4, y=80)
        self.assertEqual(self.square4.y, 4)
        self.square4.update(y=88)
        self.assertEqual(self.square4.y, 88)

    def test_square6(self):
        self.assertEqual({'size': 5, 'id': 88, 'x': 0, 'y': 0},
                         self.square.to_dictionary())


if __name__ == '__main__':
    unittest.main()
