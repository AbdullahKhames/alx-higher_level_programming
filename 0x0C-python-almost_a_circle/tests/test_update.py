#!/usr/bin/python3
"""
test update
"""


import unittest
from models.rectangle import Rectangle


class test_update(unittest.TestCase):
    """
    test update class
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.rect = Rectangle(1, 2, 3, 4)
        cls.rect1 = Rectangle(5, 6, 7, 8, 10)

    def test_update(self):
        self.assertEqual(self.rect.id, 1)
        self.rect.update(50)
        self.assertEqual(self.rect.id, 50)

        self.assertEqual(self.rect1.id, 10)
        self.rect1.update(50)
        self.assertEqual(self.rect1.id, 50)

    def test_update1(self):
        self.assertEqual(self.rect.width, 1)
        self.rect.update(50, 10)
        self.assertEqual(self.rect.width, 10)

        self.assertEqual(self.rect1.width, 5)
        self.rect1.update(50, 10)
        self.assertEqual(self.rect1.width, 10)

    def test_update2(self):
        self.assertEqual(self.rect.height, 2)
        self.rect.update(50, 10, 10)
        self.assertEqual(self.rect.height, 10)

        self.assertEqual(self.rect1.height, 6)
        self.rect1.update(50, 10, 20)
        self.assertEqual(self.rect1.height, 20)

    def test_update3(self):
        self.assertEqual(self.rect.x, 3)
        self.rect.update(50, 10, 10, 6)
        self.assertEqual(self.rect.x, 6)

        self.assertEqual(self.rect1.x, 7)
        self.rect1.update(50, 10, 20, 14)
        self.assertEqual(self.rect1.x, 14)

    def test_update4(self):
        self.assertEqual(self.rect.y, 4)
        self.rect.update(50, 10, 10, 6, 8)
        self.assertEqual(self.rect.y, 8)

        self.assertEqual(self.rect1.y, 8)
        self.rect1.update(50, 10, 20, 14, 16)
        self.assertEqual(self.rect1.y, 16)


if __name__ == '__main__':
    unittest.main()
