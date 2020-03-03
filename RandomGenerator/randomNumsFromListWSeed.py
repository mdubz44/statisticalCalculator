import random
from RandomGenerator import randomPick
class RandomNumsFromListWSeed:

    @staticmethod
    def NumsFromListWSeed(alist, a):
        random.seed(a)
        alist = []
        newList = []
        for i in range(random.random):
            newList += Pick(alist)
        return  newList


