import unittest

from str_calc import str_calc


class StrCalcTestCase(unittest.TestCase):

    def test_empty_str(self):
        self.assertEqual(str_calc(""), 0)

    def test_single_num(self):
        self.assertEqual(str_calc("0"), 0)
        self.assertEqual(str_calc("123"), 123)
        self.assertEqual(str_calc("-123"), -123)


if __name__ == "__main__":
    unittest.main()
