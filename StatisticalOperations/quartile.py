import statistics

class Quartile:

    @staticmethod
    def Quart(alist):
        alist = []
        med = statistics.median(alist)
        q1 = statistics.median(alist[0:med])
        q3 = statistics.median(alist[med:-1])
        return q1, q3