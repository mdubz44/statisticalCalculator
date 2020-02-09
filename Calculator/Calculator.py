import math
from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication

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

    def division(self, a, b):
        return a / b

    def squareRoot(self, a):
        return math.sqrt(a)

    def squared(self, a):
        return math.pow(a, 2)

