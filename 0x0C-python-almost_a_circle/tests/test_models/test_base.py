#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_id_generator(self):
        base1 = Base()
        base2 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        base = Base(id=5)
        base1 = Base(id=15)

        self.assertEqual(base.id, 5)
        self.assertEqual(base1.id, 15)


if __name__ == '__main__':
    unittest.main()
