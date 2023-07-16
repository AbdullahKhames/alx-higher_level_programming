#!/usr/bin/python3
"""
test square
"""


import unittest
from models.square import Square


class TestSquare2(unittest.TestCase):
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

    def test_square3(self):
        self.assertEqual(self.square.width, 5)
        with self.assertRaises(TypeError):
            self.square.size = "4"
        self.assertEqual(self.square.width, 5)

    def test_square5(self):
        self.assertEqual(self.square.width, 5)
        with self.assertRaises(TypeError):
            self.square.size = [4, 8]
        self.assertEqual(self.square.width, 5)

    def test_square6(self):
        self.assertEqual(self.square.width, 5)
        with self.assertRaises(TypeError):
            self.square.size = {"width": 5}
        self.assertEqual(self.square.width, 5)

    def test_square7(self):
        self.assertEqual(self.square.width, 5)
        with self.assertRaises(TypeError):
            self.square.size = 'r'
        self.assertEqual(self.square.width, 5)

    def test_square8(self):
        self.assertEqual(self.square.width, 5)
        with self.assertRaises(TypeError):
            self.square.size = (5, 8, 9)
        self.assertEqual(self.square.width, 5)

    def test_square4(self):
        self.assertEqual(self.square.height, 5)
        with self.assertRaises(TypeError):
            self.square.size = "4"
        self.assertEqual(self.square.height, 5)

    def test_square9(self):
        self.assertEqual(self.square.height, 5)
        with self.assertRaises(TypeError):
            self.square.size = (1, 2, 3)
        self.assertEqual(self.square.height, 5)

    def test_square10(self):
        self.assertEqual(self.square.height, 5)
        with self.assertRaises(ValueError):
            self.square.size = -5
        self.assertEqual(self.square.height, 5)

    def test_square11(self):
        Square.save_to_file([self.square3, self.square4])
        with open("Square.json") as fp:
            self.assertEqual('[{"x": 5, "y": 10, "id": 10, "size": 6}, {"x": 3, "y": 2, "id": 71, "size": 2}]',
                             fp.read())

    def test_square12(self):
        Square.save_to_file(None)
        with open("Square.json") as fp:
            self.assertEqual('[]',
                             fp.read())


if __name__ == '__main__':
    unittest.main()
