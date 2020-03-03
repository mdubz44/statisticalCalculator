import statistics
from StatisticalOperations import mean

class Variance:

    @staticmethod
    def Var(aList):
        aList = []
        mean = Mea(aList)
        return (float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, aList)))/ len(aList)-1)