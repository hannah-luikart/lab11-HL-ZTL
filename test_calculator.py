
import unittest
from calculator import (add, subtract, mul, div, logarithm, exp, hypotenuse, square_root)
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_divide(self):
        self.assertEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(2, 4), 2)
        self.assertAlmostEqual(div(1, 4), 4)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 4)
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -8)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-4, 6)
    def test_logarithm(self):
        self.assertEqual(logarithm(8, 2), 3.0)
        self.assertEqual(logarithm(4, 2), 2.0)
        self.assertEqual(logarithm(25, 5), 2.0)
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(3, 0), 0)
        self.assertEqual(mul(4, 5), 20)
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-2)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(25), 5.0)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
if __name__ == "__main__":
    unittest.main()