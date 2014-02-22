__author__ = 'Nick Hirakawa'

from tokenizer import *
from stemmer import *
from stopword import *


class TextProcessor:

    def __init__(self, filename, stop_file):
        self.file = filename
        self.lines = self.readlines()
        self.buffer = ''
        self.tokenizer = Tokenizer()
        self.stemmer = PorterStemmer()
        self.stopword = StopwordRemover(stop_file)

    def tokenize(self):
        print 'tokenizing'
        self.tokenizer.feed(self.lines)
        self.tokenizer.tokenize()
        self.buffer = self.tokenizer.get_tokens()

    def remove_stopwords(self):
        print 'removing stopwords'
        self.stopword.feed(self.buffer)
        self.buffer = self.stopword.get_output()
        print self.buffer

    def stem(self):
        print 'stemming'
        result = []
        for word in self.buffer:
            stemmed = self.stemmer.stem(word, 0, len(word)-1)
            print "%s => %s" % (word, stemmed)
            result.append(stemmed)
        self.buffer = result

    def process(self):
        self.tokenize()
        self.remove_stopwords()
        self.stem()

    def get_output(self):
        result = self.buffer
        self.buffer = []
        return result

    def readlines(self):
        print 'reading file'
        with open(self.file, 'r') as f:
            text = ''.join(f.readlines())
            print 'read lines:\n%s' % text
            return text