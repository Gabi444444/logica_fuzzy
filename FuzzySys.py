# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:20:58 2026

@author: User
"""

import Fuzzy_functions as Fuzzy


Pos_Karma = 0
Players = 19
Allies = 0
Neg_Karma = 0
    
print("Jogo: Prisão solitária, Dificuldade: Valete de copas\n",
      "A cada rodada um naípe aparece no display traseiro dos seus colares, ao final do Round cada jogador deve entrar em uma cela e dizer em voz alta seu naipe. Dizer o Naipe errado resultará em Game Over\n",
      "é proibido usar qualquer método para ser capaz de ver o próprio simbolo, é proibido a violência, é proibido que dois jogadores estajam na mesma cela durante a resposta, qualquer infração destas regras é Game Over",
      "dentre os jogadores está o Valete de copas, se o Valete for eliminado os jogadores ganham, caso reste somente o Valete e uma outra pessoa ganha o Valete de copas")

print("Você se aproxima de um outro jogador e pergunta seu naipe, o jogador oferece responder somente se você dizer seu naipe")

while True:
    Dica = input("Observar situação de jogo? S/N\n").strip().upper()
    if Dica == "S":
        print (f"Esse jogador me parece {Fuzzy.Suspicion([Fuzzy.Suspicious(1),Fuzzy.Uncertain(1),Fuzzy.Not_Suspicious(1)])}, ele têm {Fuzzy.Allyship([Fuzzy.Few(2,Players),Fuzzy.Some(2,Players),Fuzzy.Many(2,Players)])} aliados, no momento a chance de qualquer um ser o Valete é... {1/Players}")
    ação = input("\nMentir (a), Contar a verdade (b), Recusar (c)").strip().lower()
    if ação == "c":
        print("Você vai embora")
        break

    print("Você olha o simbolo, ele é Ouros")
    if ação == "a":
        print("Você diz que é copas")
    elif ação == "b":
        print("Você diz a verdade")
