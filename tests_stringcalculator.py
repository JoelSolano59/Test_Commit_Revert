import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):
    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 1)


if __name__ == "__main__":
    unittest.main()
