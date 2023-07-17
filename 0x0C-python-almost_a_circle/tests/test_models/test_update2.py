#!/usr/bin/python3
"""
test update
"""


import unittest
from models.rectangle import Rectangle


class test_update2(unittest.TestCase):
    """
    test update class
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.rect = Rectangle(1, 2, 3, 4)
        cls.rect1 = Rectangle(5, 6, 7, 8, 10)

    def test_update(self):
        self.assertEqual(self.rect.id, 69)
        with self.assertRaises(TypeError):
            self.rect.update(id="50")
        self.assertEqual(self.rect.id, 69)

        self.assertEqual(self.rect1.id, 10)
        with self.assertRaises(TypeError):
            self.rect1.update(id=(2, ))
        self.assertEqual(self.rect1.id, 10)

        self.assertEqual(self.rect1.id, 10)
        with self.assertRaises(ValueError):
            self.rect1.update(id=-1)
        self.assertEqual(self.rect1.id, 10)

        self.assertEqual(self.rect.id, 69)
        self.rect.update(id=50)
        self.assertEqual(self.rect.id, 50)

        self.assertEqual(self.rect1.id, 10)
        self.rect1.update(id=50)
        self.assertEqual(self.rect1.id, 50)

    def test_update1(self):
        self.assertEqual(self.rect.width, 1)
        with self.assertRaises(TypeError):
            self.rect.update(width='10')
        self.assertEqual(self.rect.width, 1)

        self.assertEqual(self.rect1.width, 5)
        with self.assertRaises(TypeError):
            self.rect.update(width=(10, ))
        self.assertEqual(self.rect1.width, 5)

        self.assertEqual(self.rect1.width, 5)
        with self.assertRaises(ValueError):
            self.rect.update(width=-5)
        self.assertEqual(self.rect1.width, 5)

        self.assertEqual(self.rect.width, 1)
        self.rect.update(50, width=10)
        self.assertEqual(self.rect.width, 1)

        self.assertEqual(self.rect.width, 1)
        self.rect.update(id=50, width=10)
        self.assertEqual(self.rect.width, 10)

        self.assertEqual(self.rect1.width, 5)
        self.rect1.update(id=50, width=10)
        self.assertEqual(self.rect1.width, 10)

    def test_update2(self):
        self.assertEqual(self.rect.height, 2)
        with self.assertRaises(TypeError):
            self.rect.update(height="10")
        self.assertEqual(self.rect.height, 2)

        self.assertEqual(self.rect1.height, 6)
        with self.assertRaises(ValueError):
            self.rect.update(height=-9)
        self.assertEqual(self.rect1.height, 6)

        self.assertEqual(self.rect.height, 2)
        self.rect.update(10, height=10)
        self.assertEqual(self.rect.height, 2)

        self.assertEqual(self.rect.height, 2)
        self.rect.update(height=10)
        self.assertEqual(self.rect.height, 10)

        self.assertEqual(self.rect1.height, 6)
        self.rect1.update(height=20)
        self.assertEqual(self.rect1.height, 20)

    def test_update3(self):
        self.assertEqual(self.rect.x, 3)
        with self.assertRaises(TypeError):
            self.rect.update(x="6")
        self.assertEqual(self.rect.x, 3)

        self.assertEqual(self.rect1.x, 7)
        with self.assertRaises(ValueError):
            self.rect1.update(x=-8)
        self.assertEqual(self.rect1.x, 7)

        self.assertEqual(self.rect.x, 3)
        self.rect.update(10, x=6)
        self.assertEqual(self.rect.x, 3)

        self.assertEqual(self.rect.x, 3)
        self.rect.update(x=6)
        self.assertEqual(self.rect.x, 6)

        self.assertEqual(self.rect1.x, 7)
        self.rect1.update(x=14)
        self.assertEqual(self.rect1.x, 14)

    def test_update4(self):
        self.assertEqual(self.rect.y, 4)
        with self.assertRaises(TypeError):
            self.rect.update(y="8")
        self.assertEqual(self.rect.y, 4)

        self.assertEqual(self.rect1.y, 8)
        with self.assertRaises(ValueError):
            self.rect1.update(y=-16)
        self.assertEqual(self.rect1.y, 8)

        self.assertEqual(self.rect.y, 4)
        self.rect.update(10, y=8)
        self.assertEqual(self.rect.y, 4)

        self.assertEqual(self.rect.y, 4)
        self.rect.update(y=8)
        self.assertEqual(self.rect.y, 8)

        self.assertEqual(self.rect1.y, 8)
        self.rect1.update(y=16)
        self.assertEqual(self.rect1.y, 16)


if __name__ == '__main__':
    unittest.main()
