#!/usr/bin/python

import sys
import find_j

for filename in sys.argv[1:]:
    file = open(filename)
    for line in file:
        for fragment in find_j.find_japanese(line):
            print(fragment)
    file.close()