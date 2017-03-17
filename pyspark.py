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

output=rdd.reduceByKey(lambda x,y : (x,y))


def mapper(g):
    k,l=g
    As,Bs=[],[]
    d=[]
    toret=[]
    for a in l:
        if len(a)==3:
            d.append(a)
        else:
            for b in a:
                d.append(b)
    for x in d:
        if x[1]=='A':
            As.append(x)
            v1=x[2]
            i=x[0]        
            for b in Bs:
                v2=b[2]
                j=b[0]
                c=v1*v2
                toret.append((str(i)+' '+str(j),c))
        else:
            Bs.append(x)
            v1=x[2]
            j=x[0]        
            for a in As:
                v2=a[2]
                i=a[0]
                c=v1*v2
                toret.append((str(i)+' '+str(j),c))
    return toret


mapped=output.flatMap(lambda x : mapper(x))


last=mapped.reduceByKey(lambda x,y:x+y)


last.collect()





