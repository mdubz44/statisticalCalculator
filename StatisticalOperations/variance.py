from StatisticalOperations.mean import Mean


class Variance:

    @staticmethod
    def Variance1(aList):
        var = []
        mean = Mean.Mean1(aList)
        for i in aList:
            var.append((i - mean) ** 2)
        return sum(var)/(len(aList) - 1)