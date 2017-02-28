#!/usr/bin/python

import os

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    i,j,v=line.split(' ')
    v=float(v)
    
    a = os.environ['mapreduce_map_input_file']
    #a="/Users/dario/Dropbox/TEACHING-2016/X/BigData/Data/Tables/data/Customer.txt"
    l = a.split("/")
    namefile = l[len(l)- 1]
    
    if namefile=='A.txt':
        print '%s\t%s' % (j,[i,'A',v])
    elif namefile=='B.txt':
        print '%s\t%s' % (i,[j,'A',v])







