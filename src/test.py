from mrjob.job import MRJob
from math import sqrt
import json
class mrMeanVar(MRJob):
    DEFAULT_PROTOCOL = 'json'

    def mapper(self, key, line):
        num = json.loads(line)
        var = [num,num*num]
        yield 1,var

    def reducer(self, n, vars):
        N = 0.0
        sum = 0.0
        sumsq = 0.0
        for x in vars:
            N += 1
            sum += x[0]
            sumsq += x[1]
        mean = sum/N
        sd = sqrt(sumsq/N - mean*mean)
        results = [mean,sd]
        yield 1,results

if __name__ == '__main__':
    mrMeanVar.run()
