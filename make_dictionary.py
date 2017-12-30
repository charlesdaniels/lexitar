#!/usr/bin/env python3

# .SHELLDOC
#
# This script consumes a tab-delmited list of words on standard input, and
# emits a sorted list of n many words, ordered from most common to least
# common on standard out.
#
# The input data should be of the format word\tfrequency
#
# The frequency must be specified as a positive integer.
#
# Blank lines are ignored
#
# .SYNTAX
#
# $1 . . . n
#
# .ENDOC

import sys
import os
import operator

n = int(sys.argv[1])

words = [] # list of tuples of word, frequency
for line in sys.stdin:
    line = line.strip()
    word = line.split('\t')[0]
    freq = int(line.split('\t')[1])
    words.append((word, freq))

words.sort(key=operator.itemgetter(1), reverse=True)
words = words[0:n]

for word in words:
    print(word[0])

