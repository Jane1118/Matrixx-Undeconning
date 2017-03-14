# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 08:56:21 2017

@author: damien
"""

import numpy.random as rd
import numpy as np


nA,mA,mB=1000,1500,500
nB=mA

inds=np.array([[i,j] for i in range(nA) for j in range(mA)])

ns=rd.choice(mA*nA)
nfill=rd.choice(nA*mA,replace=False,size=ns)


values=rd.normal(0,size=ns,scale=5)

inds=inds[nfill]

f=open('A.txt','wb')
for i in range(ns):
    t=list(inds[i])+[values[i]]
    f.writelines(str(t[0])+' '+str(t[1])+' '+str(t[2])+'\n')

f.close()    

inds=np.array([[i,j] for i in range(nB) for j in range(mB)])

ns=rd.choice(mB*nB)
nfill=rd.choice(nB*mB,replace=False,size=ns)


values=rd.normal(0,size=ns,scale=5)

inds=inds[nfill]

f=open('B.txt','wb')
for i in range(ns):
    t=list(inds[i])+[values[i]]
    f.writelines(str(t[0])+' '+str(t[1])+' '+str(t[2])+'\n')

f.close()    
