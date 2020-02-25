import statistics

class Variance:

    @staticmethod
    def Var():
        aList = []
        me = statistics.mean(aList)
        return statistics.variance(aList, me)