import unittest
import math

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

    def test_calculator_return_power(self):
        result = self.calculator.Power(2, 2)
        self.assertEqual(4, result)

    def test_calculator_access_power_result(self):
        self.calculator.Power(2, 2)
        self.assertEqual(4, self.calculator.Result)

    def test_calculator_return_sqRt(self):
        result = self.calculator.SqRt(4)
        self.assertEqual(2, result)

    def test_calculator_access_sqRt(self):
        self.calculator.SqRt(4)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_return_log(self):
        result = self.calculator.Log(2, 10)
        self.assertEqual(0.30102999566398114, result)

    def test_calculator_access_log(self):
        self.calculator.Log(2, 10)
        self.assertEqual(0.30102999566398114, self.calculator.Result)
    def test_calculator_access_mean_result(self):
        aList = [1,2,3,4]
        self.calculator.Mean(aList)
        self.assertEqual(2.5, self.calculator.Result)

    def test_calculator_access_median_result(self):
        aList = [1,2,2,3,4]
        self.calculator.Median(aList)
        self.assertEqual(2,self.calculator.Result)

    def test_calculator_access_mode_result(self):
        aList = [1,2,2,3,4]
        self.calculator.Mode(aList)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_access_variance_result(self):
        aList = [1,2,3,4,5]
        self.calculator.Variance(aList)
        self.assertEqual(2.5, self.calculator.Result)

    def test_calculator_access_standardDeviation_result(self):
        aList = [1,2,3,4,5]
        self.calculator.StandardDeviation(aList)
        self.assertEqual(1, self.calculator.Result)

    def test_calculator_access_quartile_result(self):
        aList = [1,2,3,4,5]
        self.calculator.Quartile(aList)
        self.assertEqual((2,3,4), self.calculator.Result)

    def test_calculator_access_skewness_result(self):
        aList = [1,2,3,4,5]
        self.calculator.Skewness(aList)
        self.assertEqual(0, self.calculator.Result)

    def test_calculator_access_ZScore_result(self):
        aList = [1,2,3,4,5]
        self.calculator.ZScore(aList)
        self.assertEqual([-2.0, -1.0, 0.0, 1.0, 2.0], self.calculator.Result)


    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(2, 1))
        self.assertEqual(4, self.calculator.Result)





if __name__ == '__main__':
    unittest.main()
