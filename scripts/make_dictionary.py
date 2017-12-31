#!/usr/bin/env python3

# .SHELLDOC
#
# This script consumes a tab-delmited list of words on standard input, and
# emits a Python file on standard output containing a Lexitar dictionary,
# which is a hashtable which associates a byte sequence with a coding. Two
# copies of the dictionary are generated, one indexed by byte sequence, and
# one by coding.
#
# The dictionary generated always uses a byte sequence length of 16 bits, and
# contains 2^16 entries.
#
# The input data should be of the format word\tfrequency
#
# The frequency must be specified as a positive integer.
#
# Blank lines are ignored
#
#
# .ENDOC

chunksize = 16

import sys
import os
import operator
import pprint

words = [] # list of tuples of word, frequency
for line in sys.stdin:
    line = line.strip()
    word = line.split('\t')[0]
    freq = int(line.split('\t')[1])
    words.append((word, freq))

words.sort(key=operator.itemgetter(1), reverse=True)
words = words[0:pow(2, chunksize)]

by_coding = {}
by_chunk  = {}

for idx in range(0, pow(2, chunksize)):
    chunk = (int(idx)).to_bytes(2, byteorder="big")
    coding = words[idx][0]
    by_coding[coding] = chunk
    by_chunk[chunk] = coding

pp = pprint.PrettyPrinter(indent=4)
print("by_coding = \\")
pp.pprint(by_coding)

print("by_chunk = \\")
pp.pprint(by_chunk)
