#!/usr/bin/python

import sys

for line in sys.stdin:
    pair = line.strip().split('\t')
    s = pair[0]
    l = pair[1]
    #code du reducer
    As,Bs=[]
    for x in l:
        if x[1]=='A':
            As.append(x)
        else:
            Bs.append(x)
    for a in A:
        v1=a[2]
        i=a[0]
        for b in B:
            v2=b[2]
            j=b[0]
            c=v1*v2
    print '%s\t%s' % (str(i)+str(j),c)
