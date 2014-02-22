from proc import *

__author__ = 'Nick Hirakawa'

import string
from re import *
from tokenizer import *


def main():
    textproc = TextProcessor(filename='input.txt', stop_file='stopwords.txt')
    textproc.process()
    print textproc.get_output()

if __name__ == '__main__':
    main()