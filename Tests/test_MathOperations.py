import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication


class MyTestCase(unittest.TestCase):


    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(1, Subtraction.difference(2, 1))

    def test_MathOperations_Multiplication(self):
        self.assertEqual(4, Multiplication.multiply(2, 2))

    def test_MathOperations_sum_list(self):
        valueList = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valueList))






if __name__ == '__main__':
    unittest.main()
