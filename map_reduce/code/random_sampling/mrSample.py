'''
Created on Feb 1, 2012

@author:
'''
import os
import random
from mrjob.job import MRJob
from math import sqrt
import json
from mrjob.protocol import JSONValueProtocol, PickleProtocol, RawValueProtocol, JSONProtocol


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


class mrSample(MRJob):
    INPUT_PROTOCOL = RawValueProtocol
    INTERNAL_PROTOCOL = JSONProtocol
    OUTPUT_PROTOCOL = RawValueProtocol


    def __init__(self, *args, **kwargs):

        super(mrSample, self).__init__(*args, **kwargs)
        self.samples = []
        self.count = 0

    def configure_options(self):

        super(mrSample, self).configure_options()

        # define the sample size parameter
        self.add_passthrough_option('**sample_size',
            dest='sample_size',
            default=10,
            type='int',
            help='number of samples in the output file')

    def mapper(self, key, line):
        MRJob.set_status(self, "=============>  mapper called")

        sample_line = line

        self.count += 1
        if len(self.samples) <= self.options.sample_size:
            self.samples.append(sample_line)
        else:
            expected_prob = (self.options.sample_size * 1.0) / self.count
            actual_prob = random.random()
            if actual_prob <= expected_prob:
                index = random.randint(0, self.options.sample_size)
                self.samples[index] = sample_line

    def mapper_final(self):
        MRJob.set_status(self, "=============>  mapper final called")

        out = [self.count, self.samples]
        jOut = json.dumps(out)

        yield 1, jOut


    def reducer(self, n, vars):
        MRJob.set_status(self, "=============>  reducer called")

        samples_from_mappers = []
        counts_from_mappers = []

        # First read all the counts from different mappers fo we know the total number of items and we can give
        # each of the sets coming from different mappers their appropriate weight
        total_counts_from_mappers = 0

        for x in vars:
            input = json.loads(x)
            total_counts_from_mappers += input[0]

            counts_from_mappers.append(input[0])
            samples_from_mappers.append(input[1])

        # Now based on the number of samples in each mapper we need to select appropriate number of samples form
        # samples_from_mappers
        i = 0
        for sample_set in samples_from_mappers:
            weight = counts_from_mappers[i] * 1.0 / total_counts_from_mappers
            number_of_needed_samples = int(round(weight * self.options.sample_size))

            for j in range(number_of_needed_samples):
                yield 1, sample_set.pop()

            i += 1


if __name__ == '__main__':
    mrSample.run()
