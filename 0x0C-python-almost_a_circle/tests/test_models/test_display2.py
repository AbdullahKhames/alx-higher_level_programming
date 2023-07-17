#!/usr/bin/python3
"""
test display2
"""
import io
import unittest
from models.rectangle import Rectangle
from contextlib import redirect_stdout
from unittest.mock import patch


class test_disp2(unittest.TestCase):
    """
    class test disp after mod
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.rect = Rectangle(1, 2)
        cls.rect1 = Rectangle(3, 4, 5)
        cls.rect2 = Rectangle(5, 6, 7, 8)
        cls.rect3 = Rectangle(1, 2, 3, 4, 10)
        cls.rect4 = Rectangle(2, 3, 5)
        cls.rect5 = Rectangle(1, 2, y=6, id=50)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disp(self, mocked_output):
        self.rect.display()
        self.assertEqual(mocked_output.getvalue(),
                         """#
#
""")

    def test_disp1(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.rect1.display()
        self.assertEqual(output.getvalue(),
                         """     ###
     ###
     ###
     ###
""")
        pass

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disp2(self, mocked_str):
        self.rect2.display()
        self.assertEqual(mocked_str.getvalue(), """







       #####
       #####
       #####
       #####
       #####
       #####
""")
        pass

    def test_disp3(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.rect3.display()
        self.assertEqual(output.getvalue(),
                         """



   #
   #
""")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disp4(self, mock):
        self.rect4.display()
        self.assertEqual(mock.getvalue(),
                         """     ##
     ##
     ##
""")

    def test_disp5(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.rect5.display()
        self.assertEqual(output.getvalue(),
                         """





#
#
""")

    def test_to_file(self):
        lse = [
            self.rect3,
            self.rect4,
            self.rect5
        ]
        Rectangle.save_to_file(lse)
        ch = None
        with open("../Rectangle.json") as fp:
            ch = fp.read()

        self.assertEqual(
            '[{"x": 3, "y": 4, "id": 10, "height": 2, "width": 1}, {"x": 5, "y": 0, "id": 49, "height": 3, '
            '"width": 2}, {"x": 0, "y": 6, "id": 50, "height": 2, "width": 1}]',
            ch
        )

    def test_to_file1(self):
        lse = []
        Rectangle.save_to_file(lse)
        ch = None
        with open("../Rectangle.json") as fp:
            ch = fp.read()

        self.assertEqual(
            '[]',
            ch
        )


if __name__ == '__main__':
    unittest.main()
