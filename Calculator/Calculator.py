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
        return Mean.Mea(aList)

    def Median1(self):
        list1 = [4,5,6,7]
        self.Result = Median.Med(list1)
        return Median.Med(list1)

    def Mode1(self):
        list2 = [4,5,6,7]
        self.Result = Mode.Mod(list2)
        return Mode.Mod(list2)

    def Variance1(self):
        list3 = [4,5,6,7]
        me = statistics.mean(list3)
        self.Result = Variance.Var(list3)
        return Variance.Var(list3)

    def StandardDeviation1(self):
        list4 = [4,5,6,7]
        me = statistics.mean(list4)
        self.Result = StandardDeviation.SD(list4)
        return StandardDeviation.SD(list4)

    def Quartile1(self):
        list5 = [4,5,6,7]
        self.Result = Quartile.Quart(list5)
        return Quartile.Quart(list5)

    def Skewness1(self):
        list6 = [4,5,6,7]
        self.Result = Skewness.Skew(list6)
        return Skewness.Skew(list6)


