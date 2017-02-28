# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:57:54 2017
D'abord on mappe des values de manière à obtenir après shuffle and sort des listes de valeurs provenants de A d'indice *j
et B d'indice j*. Après on combine pour emit des produits de ces valeurs, 
les A(i,k)*B(k,j), et le reducer somme ces éléments selon kpour obtenir AB(i,j)

@author: damien
"""
#lit le file A, 
def mapperA(file):
    for line in file:
        i,j,v=list(line)
        v=float(v)
        emit(j,[i,'A',v])


def mapperB(file):
    for line in file:
        i,j,v=list(line)
        v=float(v)
        emit(i,[j,'B',v])

#s="uv" ou u identifie afin d'obtenir des couples, et
#v est celui retrouve dans A(i,v)*B(v,j)
def combiner(s,l):
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
            emit(str(i)+str(j),c)

def reducer(s,l):
    i,j=list(s)
    v=np.sum(l)
    write(i+','+j+','+str(v))

















