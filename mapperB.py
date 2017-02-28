#!/usr/bin/python

import os

import sys

for line in sys.stdin:
    i,j,v=line.split(' ')
    v=float(v)
    print '%s\t%s' % (i,[j,'B',v])

