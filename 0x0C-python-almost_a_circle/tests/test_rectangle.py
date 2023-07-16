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
    rect = None
    rect1 = None
    rect2 = None
    rect3 = None
    rect4 = None
    rect5 = None

    @classmethod
    def setUpClass(cls):
        cls.rect = Rectangle(1, 5)
        cls.rect1 = Rectangle(10, 15)
        cls.rect2 = Rectangle(100, 50)
        cls.rect3 = Rectangle(1, 5, 0, 5, 10)
        cls.rect4 = Rectangle(10, 15, 15, 20, 50)
        cls.rect5 = Rectangle(100, 50, 18, 16)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.rect
        del cls.rect1
        del cls.rect2
        del cls.rect3
        del cls.rect4
        del cls.rect5

    def test_init_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_init_with_args(self):
        self.assertEqual(self.rect.id, 50)
        self.assertEqual(self.rect.width, 1)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)

        self.assertEqual(self.rect1.id, 51)
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 15)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)

        self.assertEqual(self.rect2.id, 52)
        self.assertEqual(self.rect2.width, 100)
        self.assertEqual(self.rect2.height, 50)
        self.assertEqual(self.rect2.x, 0)
        self.assertEqual(self.rect2.y, 0)

    def test_init_with_full_args(self):
        self.assertEqual(self.rect3.id, 10)
        self.assertEqual(self.rect3.width, 1)
        self.assertEqual(self.rect3.height, 5)
        self.assertEqual(self.rect3.x, 0)
        self.assertEqual(self.rect3.y, 5)

        self.assertEqual(self.rect4.id, 50)
        self.assertEqual(self.rect4.width, 10)
        self.assertEqual(self.rect4.height, 15)
        self.assertEqual(self.rect4.x, 15)
        self.assertEqual(self.rect4.y, 20)

        self.assertEqual(self.rect5.id, 53)
        self.assertEqual(self.rect5.width, 100)
        self.assertEqual(self.rect5.height, 50)
        self.assertEqual(self.rect5.x, 18)
        self.assertEqual(self.rect5.y, 16)

    def test_setter(self):
        self.rect.width = 20
        self.assertEqual(self.rect.width, 20)

    def test_getter(self):
        x = self.rect.width
        self.assertEqual(x, 1)

    def test_to_json(self):
        ls = [
            self.rect3.to_dictionary(),
            self.rect4.to_dictionary(),
            self.rect5.to_dictionary()
        ]
        s = self.rect.to_json_string(ls)
        self.assertEqual(
            '[{"x": 0, "y": 5, "id": 10, "height": 5, "width": 1}, {"x": 15, "y": 20, "id": 50, "height": 15, '
            '"width": 10}, {"x": 18, "y": 16, "id": 53, "height": 50, "width": 100}]',
            s
        )

    def test_to_json1(self):
        ls = None
        s = self.rect.to_json_string(ls)
        self.assertEqual(
            '[]',
            s
        )

    def test_from_json(self):
        rectangles = Rectangle.from_json_string(
            '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        )

        expected_data = [
            {'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}
        ]
        self.assertEqual(expected_data, rectangles)

    def test_from_json1(self):
        rectangles = Rectangle.from_json_string(
            None
        )

        expected_data = [
        ]
        self.assertEqual(expected_data, rectangles)


if __name__ == "__main__":
    unittest.main()
