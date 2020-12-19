#!/usr/bin/env python

import sys

# count total num of words
count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    composite_word, num = line.split('\t')

    # because Hadoop sorts map output by key (here: num|word)
    # before it is passed to the reducer
    print '%s\t%s' % (composite_word, num)

    try:
        # add num to count
        count += int(num)
    except ValueError:
        pass

print 'num of words is %s' % (count)