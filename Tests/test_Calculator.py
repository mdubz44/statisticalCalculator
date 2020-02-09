import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_calculator_return_difference(self):

        result = self.calculator.Difference(2, 1)
        self.assertEqual(1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(2, 1)
        self.assertEqual(1, self.calculator.Result)

    def test_calculator_return_multiply(self):
        result = self.calculator.Multiply(2, 2)
        self.assertEqual(4, result)

    def test_calculator_access_multiply_result(self):
        self.calculator.Multiply(2, 2)
        self.assertEqual(4, self.calculator.Result)

    def test_calculator_return_divide(self):
        result = self.calculator.Divide(2, 2)
        self.assertEqual(1, result)

    def test_calculator_access_divide_result(self):
        self.calculator.Divide(2, 2)
        self.assertEqual(1, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(2, 1))
        self.assertEqual(4, self.calculator.Result)





if __name__ == '__main__':
    unittest.main()
