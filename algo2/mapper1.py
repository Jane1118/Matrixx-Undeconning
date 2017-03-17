#!/usr/bin/python

import os

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    i,j,v=line.split(' ')
    v=float(v)
    i,j=map(int,[i,j])

    try:
        a = os.environ['mapreduce_map_input_file']
    except KeyError:
        a = os.environ['map_input_file']

    #a="/Users/dario/Dropbox/TEACHING-2016/X/BigData/Data/Tables/data/Customer.txt"
    l = a.split("/")
    namefile = l[len(l)- 1]
    if namefile=='A.txt':
        print '%s\t%s' % (['A',i],[j,v])
    elif namefile=='B.txt':
        print '%s\t%s' % (['B',j],[i,v])
