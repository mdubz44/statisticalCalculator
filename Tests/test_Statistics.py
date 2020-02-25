import statistics

from StatisticalOperations.mean import Mean
from StatisticalOperations.median import Median
from StatisticalOperations.mode import Mode
from StatisticalOperations.variance import Variance
from StatisticalOperations.standardDeviation import StandardDeviation
from StatisticalOperations.quartile import Quartile

class StatsTest:

    def test_Statistics_Mean(self):
        aList = [4, 5, 6, 7]
        return statistics.mean(aList)

    def test_Statistics_Median(self):
        aList = [4,5,6,7]
        return statistics.median(aList)

    def test_Statistics_Mode(self):
        aList = [4,5,6,7]
        return statistics.mode(aList)

    def test_Statistics_Variance(self):
        aList = [4,5,6,7]
        me = statistics.mean(aList)
        return statistics.variance(aList, me)

    def test_Statistics_StandardDeviation(self):
        aList = [4,5,6,7]
        me = statistics.mean(aList)
        return statistics.stdev(aList, me)

    def test_Statistics_Quartile(self):
        aList = [4,5,6,7]
        med = statistics.median(aList)
        q1 = statistics.median(aList[0:med])
        q3 = statistics.median(aList[med:-1])
        return q1, q3