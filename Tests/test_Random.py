import random

from RandomGenerator.randNumWoSeed import RandNumWoSeed
from RandomGenerator.randNumWSeed import RandNumWSeed
from RandomGenerator.randomListGen import RandomListGen

class randomTest:

    def test_RandomGenerator_RandNumWoSeed(self):
        return random.randrange(10, 20)

    def test_RandomGenerator_RandomNumWSeed(self):
        random.seed(15)
        return random.randint(10, 20)

    def test_RandomGenerator_RandomListGen(self):
        aList = []
        random.seed(15)
        for i in range(4):
            aList.append(random.randint(10, 20))
