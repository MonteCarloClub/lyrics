#!/usr/bin/env python

import sys
from string import punctuation

# input from STDIN
for line in sys.stdin:
    # convert to lower case
    line = line.strip()
    # separate string by whitespace into words
    word, num = line.split()
    
    for word in words:
        # remove punctuations at word boundaries
        word = word.strip(punctuation)
        # if word is not empty
        if word:
            # write (key, value) to STDOUT, as the input for reducers
            print '%s\t%s' % (word.strip(punctuation), 1)