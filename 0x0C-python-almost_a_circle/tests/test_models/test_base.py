import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
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
