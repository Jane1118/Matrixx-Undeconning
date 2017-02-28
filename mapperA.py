#!/usr/bin/python

import os

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    i,j,v=line.split(' ')
    v=float(v)
    print '%s\t%s' % (j,[i,'A',v])






