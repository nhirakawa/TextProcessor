__author__ = 'Nick Hirakawa'

import string
import re

# r"(\s([a-zA-z0-9]*))+"
# punctuation => !"#$%&'()*+,-/:;<=>?@[\]^_`{|}~

class Tokenizer:

    def __init__(self):
        self.text = ''
        self.regex = re.compile(r'\W+')
        self.tokens = []

    def feed(self, text):
        self.text = text

    def tokenize(self):
        self.text = self.text.replace('.', '') #removes periods
        self.tokens = [x.lower() for x in re.split('[^a-zA-Z0-9]+', self.text) if x] #split text on whitespace and punctuation, also remove empty string
        print 'tokens:'
        print self.tokens

    def get_tokens(self):
        result = self.tokens
        self.tokens = []
        return result
