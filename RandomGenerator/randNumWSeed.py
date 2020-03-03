import random

class RandNumWSeed:

    @staticmethod
    def seed(a,b, c):
        random.seed(a)
        return random.randint(b, c)

