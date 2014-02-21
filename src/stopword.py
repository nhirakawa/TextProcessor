__author__ = 'Nick Hirakawa'


class StopwordRemover:

    def __init__(self, stop_file):
        with open(stop_file, 'r') as f:
            self.stopwords = [x.rstrip() for x in f.readlines()]
        self.output = []

    def feed(self, input):
        self.output = [x for x in input if x not in self.stopwords]

    def get_output(self):
        result = self.output
        self.output = []
        return result