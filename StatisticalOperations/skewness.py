import statistics

class Skewness:

    @staticmethod
    def Skew(alist):
        alist = []
        mean = statistics.mean(alist)
        median = statistics.median(alist)
        stD = statistics.stdev(alist)
        skew = 3 * (mean - median)/stD
        return skew
