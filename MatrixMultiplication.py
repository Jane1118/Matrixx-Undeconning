# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:57:54 2017
D'abord on mappe des values de manière à obtenir après shuffle and sort des liste de maximum 2 values :
max une de A d'indice *j et max une de B j*. Après on combine pour emit des produits de ces valeurs, 
les A(i,k)*B(k,j), et le reducer somme ces éléments selon kpour obtenir AB(i,j)

@author: damien
"""
#lit le file A, 
def mapperA(file):
    for line in file:
        i,j,v=list(line)
        v=float(v)
        for k in range(n):
            emit(str(k)+j,[i,v])


def mapperB(file):
    for line in file:
        i,j,v=list(line)
        v=float(v)
        for k in range(n):
            emit(str(k)+i,[j,v])

#s="uv" ou u identifie afin d'obtenir des couples, et
#v est celui retrouve dans A(i,v)*B(v,j)
def combiner(s,l):
    if len(l)<=1:
        c=0
    else:
        v1=l[0][1]
        v2=l[1][1]
        i=l[0][0]
        j=l[1][0]
        c=v1*v2
        emit(str(i)+str(j),c)

def reducer(s,l):
    i,j=list(s)
    v=np.sum(l)
    write(i+','+j+','+str(v))

















