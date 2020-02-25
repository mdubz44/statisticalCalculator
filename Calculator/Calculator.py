import math
import statistics
from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.squareRoot import SquareRoot
from MathOperations.logarithm import Logarithm
from StatisticalOperations.mean import Mean
from StatisticalOperations.median import Median

class Calculator:

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiply(self, a, b):
        self.Result = Multiplication.multiply(a, b)
        return a * b

    def Divide(self, a, b):
        self.Result = Division.divide(a, b)
        return a / b

    def SqRt(self, a):
        self.Result = SquareRoot.sqRt(a)
        return math.sqrt(a)

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)
        return math.pow(a, b)

    def Log(self, a, b):
        self.Result = Logarithm.log(a, b)
        return math.log(a, b)

    def Mean1(self):
        aList = [4, 5, 6, 7]
        self.Result = Mean.Mea(aList)
        return statistics.mean(aList)

    def Median1(self):
        list1 = [4,5,6,7]
        self.Result = Median.Med(list1)
        return statistics.median(list1)



