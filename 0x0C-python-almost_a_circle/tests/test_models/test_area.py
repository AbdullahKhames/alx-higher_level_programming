#!/usr/bin/python3
"""
test area method
"""


import unittest
from models.rectangle import Rectangle


class test_rect(unittest.TestCase):

    def setUp(self) -> None:
        self.rect = Rectangle(2, 3)
        self.rect1 = Rectangle(10, 4)
        self.rect2 = Rectangle(10, 5)
        self.rect3 = Rectangle(10, 6)

    def test_area1(self):
        self.assertEqual(self.rect.area(), 6, "the area is wrong")

    def test_area2(self):
        self.assertEqual(self.rect1.area(), 40, "the area is wrong")

    def test_area3(self):
        self.assertEqual(self.rect2.area(), 50, "the area is wrong")

    def test_area4(self):
        self.assertEqual(self.rect3.area(), 60, "the area is wrong")


if __name__ == '__main__':
    unittest.main()
