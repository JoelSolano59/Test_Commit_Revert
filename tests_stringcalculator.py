import unittest
from . import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(stringcalculator.Add(""), 0)


if __name__ == '__main__':
    unittest.main()