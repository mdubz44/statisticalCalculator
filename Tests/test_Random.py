import random

from RandomGenerator.randNumWoSeed import RandNumWoSeed
from RandomGenerator.randNumWSeed import RandNumWSeed
from RandomGenerator.randomListGen import RandomListGen
from RandomGenerator.randomPick import RandomPick
from RandomGenerator.randomNumsFromList import RandomNumsFromList

class randomTest:

    def test_RandomGenerator_RandNumWoSeed(self):
        return random.randrange(10, 20)

    def test_RandomGenerator_RandomNumWSeed(self):
        random.seed(15)
        return random.randint(10, 20)

    def test_RandomGenerator_RandomListGen(self):
        alist = []
        return listGen(alist)

    def test_RandomGenerator_RandomPick(self):
        alist= [1, 2, 3, 4, 5]
        return Pick(alist)

    def test_RandomGenerator_RandomFromListNoSeed(self):
        alist = [1,2,3,4,5,6]
        return NumsFromListNoSeed(alist)
