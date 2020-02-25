import random

class RandomListGen:

    @staticmethod
    def listGen(a,b,c,d):
        alist= []
        random.seed(a)
        for i in range(b):
           alist.append(random.randint(c, d))
