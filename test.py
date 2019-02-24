import unittest

from str_calc import str_calc


class StrCalcTestCase(unittest.TestCase):

    def test_empty_str(self):
        self.assertEqual(str_calc(""), 0)

    def test_single_num(self):
        self.assertEqual(str_calc("0"), 0)
        self.assertEqual(str_calc("123"), 123)
        self.assertEqual(str_calc("-123"), -123)

    def test_two_nums_comma(self):
        self.assertEqual(str_calc("1,3"), 4)
        self.assertEqual(str_calc("3,1"), 4)
        self.assertEqual(str_calc("14,21"), 35)
        self.assertEqual(str_calc("21,14"), 35)

    def test_two_nums_newline(self):
        self.assertEqual(str_calc("1\n3"), 4)
        self.assertEqual(str_calc("3\n1"), 4)
        self.assertEqual(str_calc("14\n21"), 35)
        self.assertEqual(str_calc("21\n14"), 35)


if __name__ == "__main__":
    unittest.main()
