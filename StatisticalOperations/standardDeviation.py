from StatisticalOperations.mean import Mean
from MathOperations.squareRoot import SquareRoot
import math

class StandardDeviation:

    @staticmethod
    def StandardDeviation1(aList):
        sum = 0
        mean = Mean.Mean1(aList)
        for i in range(len(aList)):
            sum += pow((aList[i]-mean),2)
        return SquareRoot.sqRt(sum/len(aList)-1)