import statistics

class ZScore:

    @staticmethod
    def zS(alist):
        alist = []
        mean = statistics.mean(alist)
        stD = statistics.stdev(alist)
        for i in alist:
            zscore = (i - mean)/stD
            return zscore