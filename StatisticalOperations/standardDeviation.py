import statistics

class StandardDeviation:

    @staticmethod
    def SD():
        aList = []
        mean = statistics.mean(aList)
        return statistics.stdev(aList, mean)