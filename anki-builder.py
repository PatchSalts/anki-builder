#!/usr/bin/python

import sys
import find_j
import segment_j

words = list()
for filename in sys.argv[1:]:
    file = open(filename)
    for line in file:
        for fragment in find_j.find_japanese(line):
            words.extend(segment_j.segment_japanese(fragment))
    file.close()