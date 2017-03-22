#!/usr/bin/python

import sys

current_cid = None
cid = None
c=0

nA, mA = 2, 2
nB, mB = 2, 2

for line in sys.stdin:
    mid = line[0]
    newline = line.split('\t')

    if mid == 'A':
        for j in range(mB):
            print '%s\t%s' (''.join(newline[0][1:])+' '+str(j), newline[1:])
    else:
        for i in range(nA):
            print '%s\t%s' (str(i)+' '+''.join(newline[0][1:]), newline[1:])
