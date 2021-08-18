from mrjob.job import MRJob
from mrjob.step import MRStep


class MRSimpleJob(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        yield 'line', 1
        yield 'word', len(line.split())
        yield 'char', len(line)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRSimpleJob.run()