from mrjob.job import MRJob
from math import sqrt
import json

size = 40

class mrStratifiedSampler(MRJob):

    self.samples = {} 
    self.count = {} 

    def mapper_init(self):
        MRJob.set_status(self, "=============>  mapper init called")




    def classify_mapper(self, key, line):
        
        # parse
        j = json.loads(line)
        k = j['kind']
        i = j

        # count

        # subsample to N

        # store locally

    def classify_mapper_final(self):
        MRJob.set_status(self, "=============>  mapper final called")

        # transmit
        yield k, i


    # def combiner(self, key, values):
    #     l = 12
    #     yield 1, (key, l, values)

    def classify_reducer(self, n, vars):
        MRJob.set_status(self, "=============>  reducer called")
        global count
        global partialcount
        
        p = sum([1 for i in vars])
        yield n, (vars, count)

    # def reducer_final(self):
    #     pass

    def steps(self):
         return [self.mr(mapper=self.classify_mapper, 
                         mapper_final=self.classify_mapper_final
                        reducer=self.classify_clareducer),
                 self.mr(mapper=self.double_counts)]


    # def steps(self):
    #      return [self.mr(mapper=self.mapper,
    #                  combiner=self.sum_words,
    #                  reducer=self.sum_words),
    #              self.mr(mapper=self.double_counts)]

if __name__ == '__main__':
    mrStratifiedSampler.run()
