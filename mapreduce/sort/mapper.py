#!/usr/bin/env python

import sys

# input from STDIN
for line in sys.stdin:
    # split space
    line = line.strip()
    # line is not null
    if line:
        # separate string by whitespace into [word, num]
        word, num = line.split()
        # construct composite key like num|word, 
        # mapreduce framework will sort by this composited key
        composite_word = ('000000' + num)[-6:] +'|'+ word
        # write (key, value) to STDOUT, as the input for reducers
        print '%s\t%s' % (composite_word, num)