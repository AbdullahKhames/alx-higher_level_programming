#!/usr/bin/python3
"""
rect 2 module test
"""

from models.rectangle import Rectangle
import unittest


class test_rect(unittest.TestCase):

    def setUp(self) -> None:
        self.rect = Rectangle(1, 2)

    def tearDown(self) -> None:
        del self.rect

    def test_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 15)

        with self.assertRaises(ValueError):
            self.rect.width = -1

        self.assertEqual(self.rect.width, 1)
        self.rect.width = 50
        self.assertEqual(self.rect.width, 50)

    def test_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 15)

        with self.assertRaises(TypeError):
            Rectangle((1,), 15)

        with self.assertRaises(TypeError):
            Rectangle([1], 15)

        with self.assertRaises(TypeError):
            Rectangle({"x": "15"}, 15)

        self.assertEqual(self.rect.width, 1)
        self.rect.width = 50
        self.assertEqual(self.rect.width, 50)

    def test_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(15, 0)

        with self.assertRaises(ValueError):
            self.rect.height = -1

        self.assertEqual(self.rect.height, 2)
        self.rect.height = 50
        self.assertEqual(self.rect.height, 50)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "15")

        with self.assertRaises(TypeError):
            Rectangle(15, (1, ))

        with self.assertRaises(TypeError):
            Rectangle(1, [15])

        with self.assertRaises(TypeError):
            Rectangle(15, {"x": "15"})

        self.assertEqual(self.rect.height, 2)
        self.rect.height = 50
        self.assertEqual(self.rect.height, 50)

    def test_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(15, 20, -1)

        with self.assertRaises(ValueError):
            self.rect.x = -1

        self.assertEqual(self.rect.x, 0)
        self.rect.x = 50
        self.assertEqual(self.rect.x, 50)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 15, "0")

        with self.assertRaises(TypeError):
            Rectangle(15, 10, (1, ))

        with self.assertRaises(TypeError):
            Rectangle(1, 2, [15])

        with self.assertRaises(TypeError):
            Rectangle(15, 10, {"x": "15"})

        self.assertEqual(self.rect.x, 0)
        self.rect.x = 50
        self.assertEqual(self.rect.x, 50)

    def test_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(15, 20, 1, -1)

        with self.assertRaises(ValueError):
            self.rect.y = -1

        self.assertEqual(self.rect.y, 0)
        self.rect.y = 50
        self.assertEqual(self.rect.y, 50)

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 15, 1, "0")

        with self.assertRaises(TypeError):
            Rectangle(15, 10, 1, (1,))

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, [15])

        with self.assertRaises(TypeError):
            Rectangle(15, 10, 1, {"x": "15"})

        self.assertEqual(self.rect.y, 0)
        self.rect.y = 50
        self.assertEqual(self.rect.y, 50)

    def test_dic_to_ins(self):
        dic = {'height': 2, 'width': 1, 'id': 1, 'x': 5, 'y': 5}
        self.assertEqual("[Rectangle] (1) 5/5 - 1/2",
                         str(Rectangle.create(**dic)))


if __name__ == '__main__':
    unittest.main()