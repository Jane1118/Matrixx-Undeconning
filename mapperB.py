#!/usr/bin/python

import os

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    attributes = line.split(",")
    # read name of file from os environment
    a = os.environ['mapreduce_map_input_file']
    #a="/Users/dario/Dropbox/TEACHING-2016/X/BigData/Data/Tables/data/Customer.txt"
    l = a.split("/")
    namefile = l[len(l)- 1]
   # print(namefile)
    if namefile !='Customer.txt' :
        print '%s\t%s' % ( attributes[0], namefile +","+ attributes[1])
    elif attributes[1][3:5]=="07" :
        print '%s\t%s' % (attributes[0], namefile )

