# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:57:29 2026

@author: User
"""

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

#Versão com pesos
def Decide_Weighted(i,As,bank):
    conjuntos = [Fuzzy_péssima(i,As), Fuzzy_ruim(i,As), Fuzzy_moderada(i,As), Fuzzy_boa(i,As),Fuzzy_ótima(i,As),Fuzzy_perfeita(i,As)]
    
    if conjuntos[0] == 1:
        return 0
    if conjuntos[5] == 1:
        return bank
    num = 1 + int(0.5*conjuntos[4]*bank + 0.25*conjuntos[3]*bank + 0.25*conjuntos[2]*bank - 0.25*conjuntos[1]*bank - 0.25*conjuntos[0]*bank)
    if num < 0:
        return 0
    if i == 20:
        return int(num + 0.25*bank)
    return num

if __name__ == "__main__":
    As = True
    for i in range(4, 23):
        conjuntos = [Fuzzy_péssima(i, As), Fuzzy_ruim(i, As), Fuzzy_moderada(i, As), Fuzzy_boa(i, As), Fuzzy_ótima(i, As), Fuzzy_perfeita(i, As)]
        x = conjuntos[0]
        y = 0
        for w in range(len(conjuntos)):
            if conjuntos[w] > x:
                x = conjuntos[w]
                y = w
        print(f"para {i} o melhor conjunto é {y} pelo indice {x}")

print(Decide(18,As,50))
print(Decide_Weighted(18,As,50))
