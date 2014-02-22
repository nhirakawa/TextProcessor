TextProcessor
=============

Implemented a basic text processor for a search engine. The text processor takes an input file to read and a file containing
stopwords to remove from the resulting text. After reading in the text, the text processor passes the text through 
a tokenizer. The tokenizer removes periods and splits on all whitespace and all punctuation except periods. The resulting
list is then passed to the stopword remover. The stopword remover reads in the stopwords and removes these words from the
text. Finall, the text is passed to a stemmer, which truncates the words according to the Porter Stemmer rules. The words
are then printed.

To Run:
=======
Running main.py runs the text processor on the default input.txt and stopwords.txt files.
