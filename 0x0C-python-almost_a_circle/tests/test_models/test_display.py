#!/usr//bin/python3
"""
test display
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

from models.rectangle import Rectangle
from unittest.mock import patch


class test_display(unittest.TestCase):
    """
    class to test display
    """

    def setUp(self) -> None:
        self.rect = Rectangle(5, 5)
        self.rect1 = Rectangle(2, 2)
        self.rect2 = Rectangle(4, 10)
        self.rect3 = Rectangle(5, 3)
        self.rect4 = Rectangle(2, 6)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disp(self, mock_stdout):
        self.rect.display()  # Call function.
        self.assertEqual(mock_stdout.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

    def test_disp1(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.rect1.display()

        self.assertEqual(fake_stdout.getvalue(), '##\n##\n')

    def test_disp2(self):
        with mock.patch('sys.stdout') as fake_stdout:
            self.rect2.display()

        fake_stdout.assert_has_calls([
            mock.call.write('#'),
            mock.call.write(''),
            mock.call.write('\n')
        ])

    def test_disp3(self):
        # Capture the output of the print statements
        output = io.StringIO()
        with redirect_stdout(output):
            self.rect3.display()

        # Get the printed output as a string
        printed_output = output.getvalue()

        # Compare the printed output with the expected result
        expected_output = "#####\n#####\n#####\n"
        self.assertEqual(printed_output, expected_output)

    def test_disp4(self):
        output = io.StringIO()
        with redirect_stdout(output):
            self.rect4.display()
        printed_output = output.getvalue()
        expected_output = """##
##
##
##
##
##
"""
        self.assertEqual(printed_output, expected_output)


if __name__ == '__main__':
    unittest.main()
