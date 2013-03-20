from mrjob.job import MRJob
from math import sqrt
import json
from mrjob.protocol import JSONValueProtocol, PickleProtocol, RawValueProtocol
import sys
import random

class mrStratify(MRJob):


    def mapper_init(self):
        MRJob.set_status(self, "=============>  mapper init called")

    def __init__(self, *args, **kwargs):

        super(mrStratify, self).__init__(*args, **kwargs)

        self.output = {}
        self.strata = {}

    def configure_options(self):

        super(mrStratify, self).configure_options()

        # define the sampling rate                                                                                                                                                                        
        self.add_passthrough_option('--sampling_rate',
            dest = 'sampling_rate',
            default = 0.1,
            type = 'float',
            help = 'sampling rate')

    def mapper(self, key, line):

        # parse
        instance = json.loads(line)
        label = instance['class']

        try:
            self.strata[label].append(instance)
        except:
            self.strata[label] = []
            self.strata[label].append(instance)

    def mapper_final(self):

        MRJob.set_status(self, "=============>  mapper final called")

        for label in self.strata:
            stratum = self.strata[label]
            number_of_samples = int( len(stratum) * self.options.sampling_rate )

            if not stratum: # stratum should not be empty                                                                                                                                                 
        pass
            else:
               for random_sample in random.sample(stratum, number_of_samples):
                    yield label, random_sample


    def reducer(self, label, samples):

        try:
                self.output[label].extend(samples)
        except:
                self.output[label] = []
                self.output[label].extend(samples)

    def reducer_final(self):

        MRJob.set_status(self, "=============>  reducer final called")

        for label in self.output:
            stratum_samples = self.output[label]
            yield label, (len(stratum_samples), stratum_samples)

    def steps(self):
         return [self.mr(mapper=self.mapper,
                         mapper_final=self.mapper_final,
                         reducer=self.reducer,
                         reducer_final=self.reducer_final)]

if __name__ == '__main__':
    mrStratify.run()

