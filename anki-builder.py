#!/usr/bin/python

import sys

print(str(len(sys.argv)) + " args: " + str (sys.argv))

for filename in sys.argv[1:]:
    file = open(filename)
    for line in file:
        print(line)
    file.close()