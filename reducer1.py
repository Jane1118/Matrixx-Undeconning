#!/usr/bin/python

import sys
import ast

current_cid = None
cid = None
As,Bs=[],[]


for line in sys.stdin:
    pair = line.strip().split('\t')
    cid = pair[0]
    x=ast.literal_eval(pair[1])
    #code du reducer
    if current_cid != cid:
        As,Bs=[],[]
    current_cid = cid
    
    if x[1]=='A':
        As.append(x)
        v1=x[2]
        i=x[0]        
        for b in Bs:
            v2=b[2]
            j=b[0]
            c=v1*v2
            print '%s\t%s' % (str(i)+' '+str(j),c)
    else:
        Bs.append(x)
        v1=x[2]
        j=x[0]        
        for a in As:
            v2=a[2]
            i=a[0]
            c=v1*v2
            print '%s\t%s' % (str(i)+' '+str(j),c)
