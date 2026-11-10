import unittest
from calculator import add, subtract, multiply, divide, logarithm, exponent
class TestCalculator(unittest.TestCase):
def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
def test_subtract(self):
    self.assertEqual(sub(5, 3), 2)
def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        div(0, 5)
    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3.0)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-2, 8)
    def test_exponent(self):
        self.assertEqual(exp(2, 3), 8)
if __name__ == "__main__":
    unittest.main()