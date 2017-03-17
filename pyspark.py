# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:36:51 2017

@author: damien
"""

A=sc.textFile('file:/home/damien.menigaux/projet/data/smalltables/A.txt')
B=sc.textFile('file:/home/damien.menigaux/projet/data/smalltables/B.txt')

def mapperA(line):
    i,j,v=line.split(' ')
    v=float(v)
    i,j=map(int,[i,j])
    return j,[i,'A',v]

def mapperB(line):
    i,j,v=line.split(' ')
    v=float(v)
    i,j=map(int,[i,j])
    return i,[j,'B',v]


outputA = A.map(lambda line: mapperA(line))

outputB = B.map(lambda line: mapperB(line))

rdd = sc.union([outputA,outputB])


flatten = lambda l: [item for sublist in l for item in sublist]

output=rdd.reduceByKey(lambda x,y : flatten((x,y)))

import numpy as np
def mapper(g):
    k,l=g
    As,Bs=[],[]
    d=[]
    toret=[]
    d=map(list,np.array(l).reshape((len(l)/3,3)))
    for x in d:
        if x[1]=='A':
            As.append(x)
            v1=float(x[2])
            i=int(x[0])
            for b in Bs:
                v2=float(b[2])
                j=int(b[0])
                c=v1*v2
                toret.append((str(i)+' '+str(j),c))
        else:
            Bs.append(x)
            v1=float(x[2])
            j=int(x[0])        
            for a in As:
                v2=float(a[2])
                i=int(a[0])
                c=v1*v2
                toret.append((str(i)+' '+str(j),c))
    return toret


mapped=output.flatMap(lambda x : mapper(x))

last=mapped.reduceByKey(lambda x,y:x+y)


last.collect()




