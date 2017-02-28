#!/usr/bin/python

import sys

for line in sys.stdin:
    pair = line.strip().split('\t')
    s = pair[0]
    l = pair[1]
    #code du reducer
    i,j=list(s)
    v=0.0
    for x in l:
        v+=x
    print '%s\t%s' % (i+' '+j+' '+str(v))

                                     


