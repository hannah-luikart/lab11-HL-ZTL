import unittest
from calculator import (add, subtract, mul, div, logarithm, exp, hypotenuse, square_root)
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_divide(self):
        self.assertEqual(div(2, 10), 5.0)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -8)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3.0)
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
    def test_sqrt(self):
        self.assertEqual(square_root(9), 3.0)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
if __name__ == "__main__":
    unittest.main()