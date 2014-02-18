__author__ = 'Nick Hirakawa'


class StopwordRemover:

    def __init__(self, stop_file):
        with open(stop_file, 'r') as f:
            self.stopwords = f.readlines()
        self.output = []


    def feed(self, input):
        buffer = [x for x in input if x in self.stopwords]
        for word in buffer:
            self.output.append(word)