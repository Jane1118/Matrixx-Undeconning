#!/usr/bin/python

import sys
import ast

current_cid = None
cid = None
curent_mid = None
mid = None

for line in sys.stdin:
    pair = line.strip().split('\t')
    ids = list(pair[0])
    mid = ids[0]
    cid = ''.join(ids[1:])
    x=ast.literal_eval(pair[1])
    #code du reducer
    if current_cid == None:
        line = pair[0]
        current_cid = cid

    if current_cid == cid:
        line += ' % '+str(x[0])+' '+str(x[1]) #on separe les differentes colonnes par des tabs

    if current_cid != cid:
        if current_cid:
            print line
        line = pair[0]
        line += ' % '+str(x[0])+' '+str(x[1])
        current_cid = cid
