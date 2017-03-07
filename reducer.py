#!/usr/bin/python

import sys

current_cid = None
cid = None
c=0

for line in sys.stdin:
    cid,x = line.strip().split('\t')
    x=float(x)
    if current_cid == cid:
        c+=x
    else:
        if current_cid:
            print '%s\t%s' % (current_cid,str(c))
            c=0
            current_cid = cid
    
if current_cid == cid:
    if current_cid:
        print '%s\t%s' % (current_cid,str(c))

