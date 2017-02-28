#!/usr/bin/python

import sys

for line in sys.stdin:
    pair = line.strip().split('\t')
    s = pair[0]
    l = pair[1]
    #code du reducer
    
    if current_cid == cid:
        lvalues.append(rest)

    else:
        if current_cid:
            # write result to STDOUT
            if 'Customer.txt' in lvalues :
                for x in lvalues :
                    if x != 'Customer.txt' :
                        print '%s\t%s' % (current_cid, x.split(",")[1])

        current_cid = cid
        lvalues=[rest]

if current_cid == cid:
    if 'Customer.txt' in lvalues :
        for x in lvalues :
            if x != 'Customer.csv' :
                    print '%s\t%s' % (cid, x.split(",")[1])


                                     


