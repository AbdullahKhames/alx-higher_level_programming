#!/usr/bin/python3
"""
test __str__
"""
import io
import unittest
from models.rectangle import Rectangle


class test_str(unittest.TestCase):
    """
    class to test __str__
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        function to setup class
        :return: no return
        """

        cls.rect = Rectangle(1, 2)
        cls.rect1 = Rectangle(3, 4, 5)
        cls.rect2 = Rectangle(5, 6, 7, 8)
        cls.rect3 = Rectangle(1, 2, 3, 4, 10)
        cls.rect4 = Rectangle(1, 2, 5)
        cls.rect5 = Rectangle(1, 2, y=6, id=50)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (64) 0/0 - 1/2")

    def test_str1(self):
        self.assertEqual(str(self.rect1), "[Rectangle] (65) 5/0 - 3/4")

    def test_str2(self):
        self.assertEqual(str(self.rect2), "[Rectangle] (66) 7/8 - 5/6")

    def test_str3(self):
        self.assertEqual(str(self.rect3), "[Rectangle] (10) 3/4 - 1/2")

    def test_str4(self):
        self.assertEqual(str(self.rect4), "[Rectangle] (67) 5/0 - 1/2")

    def test_str5(self):
        self.assertEqual(str(self.rect5), "[Rectangle] (50) 0/6 - 1/2")


if __name__ == '__main__':
    unittest.main()
