#!/usr/bin/python3
"""
unit testing module for rect
"""
import unittest

from models.rectangle import Rectangle


class test_rect(unittest.TestCase):
    """
    class to test rectangle
    """

    @classmethod
    def setUpClass(cls):
        cls.rect = Rectangle(1, 5)
        cls.rect1 = Rectangle(10, 15)
        cls.rect2 = Rectangle(100, 50)
        cls.rect3 = Rectangle(1, 5, 0, 5, 10)
        cls.rect4 = Rectangle(10, 15, 15, 20, 50)
        cls.rect5 = Rectangle(100, 50, 18, 16)

    def test_dict(self):
        self.assertEqual({'height': 5, 'id': 17, 'width': 1, 'x': 0, 'y': 0},
                         self.rect.to_dictionary())

    def test_dict4(self):
        self.assertEqual({'height': 15, 'id': 50, 'width': 10, 'x': 15, 'y': 20},
                         self.rect4.to_dictionary())


if __name__ == '__main__':
    unittest.main()
