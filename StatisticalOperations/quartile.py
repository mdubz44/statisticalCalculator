from StatisticalOperations.median import Median

class Quartile:

    @staticmethod
    def Quartile1(alist):
        med = Median.Median1(alist)
        q1 = Median.Median1(alist[0:med])
        q3 = Median.Median1(alist[med:-1])
        return q1, med, q3