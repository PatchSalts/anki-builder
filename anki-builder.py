#!/usr/bin/python

import sys
import find_j

print(str(len(sys.argv)) + " args: " + str (sys.argv))

for filename in sys.argv[1:]:
    file = open(filename)
    for line in file:
        for j in find_j.find_japanese(line):
            print(j)
    file.close()