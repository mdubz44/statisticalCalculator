import statistics
from StatisticalOperations import mean
from math import sqrt

class StandardDeviation:

    @staticmethod
    def SD(aList):
        mean = Mea(aList)
        return sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, aList)))/ len(aList))






