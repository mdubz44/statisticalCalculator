import statistics
from StatisticalOperations.mean import Mean
from StatisticalOperations.median import Median
from StatisticalOperations.standardDeviation import StandardDeviation

class Skewness:
    @staticmethod
    def Skew(alist):
        mean = Mean.Mean1(alist)
        median = Median.Median1(alist)
        stD = StandardDeviation.StandardDeviation1(alist)
        skew = 3 * (mean - median)/stD
        return skew
