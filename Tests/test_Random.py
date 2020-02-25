import random

from RandomGenerator.randNumWoSeed import RandNumWoSeed
from RandomGenerator.randNumWSeed import RandNumWSeed

class randomTest:

    def test_RandomGenerator_RandNumWoSeed(self):
        return random.randrange(10, 20)

    def test_RandomGenerator_RandomNumWSeed(self):
        random.seed(15)
        return random.randint(10, 20)
