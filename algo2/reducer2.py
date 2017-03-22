#!/usr/bin/python

import sys
import ast

current_ids = None
ids = None


#il faut stocker les valeurs avant de faire le produit scalaire

for line in sys.stdin:
    pair = line.strip().split('\t')
    ids = pair[0]


    if ids == current_ids:
        #stockage de la ligne/colonne manquante
        values2 = pair[1].split(' % ')
        #calcul de cij
        cij = 0
        for v1 in values1:
            for v2 in values2:
                if v1.split(' ')[0] == v2.split(' ')[0]:
                    cij += v1.split(' ')[1]*v2.split(' ')[1]

    if current_ids = None:
        values1 = pair[1].split(' % ')
        current_ids = ids

    if ids != current_ids:
        #stockage de la premiere colonne/ligne
        values1 = pair[1].split(' % ')
        current_ids = ids
        #émission
        print cij
