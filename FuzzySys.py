import Fuzzy_functions as Fuzzy
from random import randint

suits = ["Copas","Ouros","Espadas","Paus"]
Ippei = Fuzzy.Bot(0,0,3,"Paus")

Pos_Karma = int(input("Karma positivo, range de 0-5 "))
Players = int(input("Jogadores, range de 2-19 "))
Allies = int(input("Aliados, range de 0-18 "))
Neg_Karma = int(input("Karma negativo, range de 0-5 "))
your_suit = suits[randint(0,3)]
    
print("Jogo: Prisão solitária, Dificuldade: Valete de copas\n",
      "A cada rodada um naípe aparece no display traseiro dos seus colares, ao final do Round cada jogador deve entrar em uma cela e dizer em voz alta seu naipe. Dizer o Naipe errado resultará em Game Over.\n",
      "é proibido usar qualquer método para ser capaz de ver o próprio simbolo, é proibido a violência, é proibido que dois jogadores estajam na mesma cela durante a resposta, qualquer infração destas regras é Game Over",
      "dentre os jogadores está o Valete de copas, se o Valete for eliminado os jogadores ganham, caso reste somente o Valete e uma outra pessoa ganha o Valete de copas")

print("Você se aproxima de um outro jogador e pergunta seu naipe, o jogador oferece responder somente se você dizer seu naipe")

while True:
    Dica = input("Observar situação de jogo? S/N\n").strip().upper()
    if Dica == "S":
        Suspect = [Fuzzy.Suspicious(Ippei.Ownkarma),Fuzzy.Uncertain(Ippei.Ownkarma),Fuzzy.Not_Suspicious(Ippei.Ownkarma)]
        Ally_Set = [Fuzzy.Few(Ippei.alliances,Players),Fuzzy.Some(Ippei.alliances,Players),Fuzzy.Many(Ippei.alliances,Players)]
        print (f"Esse jogador me parece {Fuzzy.Suspicion(Suspect)}, ele têm {Fuzzy.Allyship(Ally_Set)} aliados, no momento a chance de qualquer um ser o Valete é... {1/Players*100}%")
        
    ação = input("\nMentir (a), Contar a verdade (b), Recusar (c)").strip().lower()
    if ação == "c":
        print("Você recusa a troca")
        break

    print(f"Você olha o simbolo, vendo que é o naipe de {Ippei.Suit}")
    if ação == "a":
        while True:
            i = randint(0,3)
            if suits[i] != Ippei.Suit:
                suit = suits[i]
                break
        print(f"decidindo mentir, você inventa que simbolo é {suit}")
    elif ação == "b":
        print("Você decide dizer a verdade")
        suit = Ippei.Suit
    Decision = Ippei.Trust(Fuzzy.Danger_Trust(Neg_Karma, Players, Pos_Karma),suit)
    
    Tell = Ippei.Lie(Fuzzy.Danger_Lie(Players, Allies), your_suit)
    
    print(f"Ele olha seu colar em retorno, de acordo com o jogador o seu simbolo é {Tell}")
    break
    
if ação == "a" or ação == "b":
    print("Decisão do bot:", Decision)
print("Seu naipe real:", your_suit)
