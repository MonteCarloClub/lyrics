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

    # because Hadoop sorts map output by composite_word
    print '%s\t%s' % (composite_word, num)

    try:
        # add num to count
        count += int(num)
    except ValueError:
        pass

# write total num of words to output file
print 'num of words is %s' % (count)