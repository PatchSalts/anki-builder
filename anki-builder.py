#!/usr/bin/python

import sys
import time

import find_j
import segment_j
import lookup_j
import timeestimate

words = set()
for filename in sys.argv[1:]:
    file = open(filename)
    for line in file:
        for fragment in find_j.find_japanese(line):
            words.update(segment_j.segment_japanese(fragment))
    file.close()

worddata = list()
print("Please wait " + str(timeestimate.estimate_time(len(words))) + " seconds while we look up those words on jisho.org...")
for word in words:
    worddata.extend(lookup_j.lookup_japanese(str(word)))
    time.sleep(timeestimate.SLEEPTIME)