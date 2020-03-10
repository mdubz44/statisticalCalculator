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
from StatisticalOperations.mode import Mode
from StatisticalOperations.variance import Variance
from StatisticalOperations.standardDeviation import StandardDeviation
from StatisticalOperations.quartile import Quartile
from StatisticalOperations.skewness import Skewness
from StatisticalOperations.zScore import ZScore

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

    def Mean(self, aList):
        aList = [1, 2, 3, 4]
        self.Result = Mean.Mean1(aList)
        return self.Result

    def Median(self, aList):
        aList = [1, 2, 2, 3, 4]
        self.Result = Median.Median1(aList)
        return self.Result

    def Mode(self, aList):
        aList = [1, 2, 2, 3, 4]
        self.Result = Mode.Mode1(aList)
        return self.Result

    def Variance(self, aList):
        aList = [1, 2, 3, 4, 5]
        self.Result = Variance.Variance1(aList)
        return self.Result

    def StandardDeviation(self, aList):
        aList = [1, 2, 3, 4, 5]
        self.Result = StandardDeviation.StandardDeviation1(aList)

    def Quartile(self, aList):
        aList = [1, 2, 3, 4, 5]
        self.Result = Quartile.Quartile1(aList)

    def Skewness(self, aList):
        aList = [1, 2, 3, 4, 5]
        self.Result = Skewness.Skew(aList)

    def ZScore(self, aList):
        aList = [1, 2, 3, 4, 5]
        self.Result = ZScore.ZScore1(aList)
