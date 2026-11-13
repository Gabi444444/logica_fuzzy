# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:57:29 2026

@author: User
"""

def Fuzzy_péssima(res,A):
    if res >= 22:
        return 1
    return 0

def Fuzzy_ruim(res,A):
    if res < 10 or res > 16:
        return 0
    if A:
        return (16-res)/16
    return 10/(26-res)

def Fuzzy_boa(res,A):
    if res > 19 or res < 14:
        return 0
    if res < 17 and not A:
        return 13/(res+1)
    return 14/(36-res)

def Fuzzy_moderada(res,A):
    if res > 11 or res < 4:
        return 0
    if res <= 7:
        return 1
    return 8/(26-res)

def Fuzzy_ótima(res,A):
    if res < 18 or res > 21:
        return 0
    if A: 
        return 1
    return 19/(42-res)

def Fuzzy_perfeita(res,A):
    if res == 21:
        return 1
    return 0

As = True
for i in range(4,23):
    conjuntos = [Fuzzy_péssima(i,As), Fuzzy_ruim(i,As), Fuzzy_moderada(i,As), Fuzzy_boa(i,As),Fuzzy_ótima(i,As),Fuzzy_perfeita(i,As)]
    x = conjuntos[0]
    y = 0
    for w in range(len(conjuntos)):
        if conjuntos[w] > x:
            x = conjuntos[w]
            y = w
    print(f"para {i} o melhor conjunto é {y} pelo indice {x}")

def Decide(i,As,bank):
    conjuntos = [Fuzzy_péssima(i,As), Fuzzy_ruim(i,As), Fuzzy_moderada(i,As), Fuzzy_boa(i,As),Fuzzy_ótima(i,As),Fuzzy_perfeita(i,As)]
    x = conjuntos[0]
    y = 0
    for w in range(len(conjuntos)):
        if conjuntos[w] > x:
            x = conjuntos[w]
            y = w
    if y == 0 or y == 1:
        return 1
    if y == 2:
        return bank/10
    if y == 3 or y == 4:
        return int(bank*x)
    return bank

print(Decide(i,As,50))
    


