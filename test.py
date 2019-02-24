import unittest

from str_calc import str_calc


class StrCalcTestCase(unittest.TestCase):

    def test_empty_str(self):
        self.assertEqual(str_calc(""), 0)

    def test_single_num(self):
        self.assertEqual(str_calc("0"), 0)
        self.assertEqual(str_calc("123"), 123)

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

    def test_three_nums_comma(self):
        self.assertEqual(str_calc("1,3,8"), 12)
        self.assertEqual(str_calc("12,5,20"), 37)

    def test_three_nums_newline(self):
        self.assertEqual(str_calc("1\n3\n8"), 12)
        self.assertEqual(str_calc("12\n5\n20"), 37)

    def test_negative_nums(self):
        with self.assertRaises(ValueError):
            str_calc("-123")
        with self.assertRaises(ValueError):
            str_calc("1,-5")
        with self.assertRaises(ValueError):
            str_calc("1\n-5")
        with self.assertRaises(ValueError):
            str_calc("1,5,-2")
        with self.assertRaises(ValueError):
            str_calc("-1,5")
        with self.assertRaises(ValueError):
            str_calc("1\n5\n-2")
        with self.assertRaises(ValueError):
            str_calc("-1\n5")

    def test_over_1000(self):
        self.assertEqual(str_calc("1000"), 1000)
        self.assertEqual(str_calc("1001"), 0)
        self.assertEqual(str_calc("981273"), 0)
        self.assertEqual(str_calc("203,123871123"), 203)
        self.assertEqual(str_calc("43\n9812739\n8"), 51)


if __name__ == "__main__":
    unittest.main()
