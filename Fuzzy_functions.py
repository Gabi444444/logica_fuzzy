from random import randint

suits = ["Copas", "Ouros", "Espadas", "Paus"]

#player's negative Karma

def Suspicious(x):
    if x > 4:
        return 1
    if x <= 1:
        return 0
    return x/5

def Uncertain(x):
    if x == 3:
        return 1
    if x == 0 or x == 5:
        return 0
    if x == 2:
        return (5-x)/5
    return x/5
    
def Not_Suspicious(x):
    if x <= 1:
        return 1
    if x >= 4:
        return 0
    return (5-x)/6


#Likelyhood that player is the Jack of Hearts

def Very_unlikely(n):
    if n >= 16:
        return 1
    if n <= 0:
        return 0
    return n/19

def Unlikely(n):
    if n >= 12 and n <= 14:
        return 1
    if n <= 6 or n >= 17:
        return 0
    return (n-2)/19

def Neutral(n):
    if n <= 11 and n >= 9:
        return 1
    if n > 16 or n < 3:
        return 0
    if n < 9:
        return (n-2)/7
    if n > 11:
        return (n-1)/19
    
def Likely(n):
    if n >= 5 and n<= 9:
        return 1
    if n >= 13 or n < 3:
        return 0
    return (18-n)/17

def Very_likely(n):
    if n <= 3:
        return 1
    if n >= 8:
        return 0
    return (19-n)/19

#Allyship rating
def Few(a,n):
    if n <= 0:
        return 0
    if a >= 5 and a/n > 0.35:
        return 0
    if a/n <= 0.25:
        return 1
    return (n-a)/n

def Some(a,n):
    if n <= 0:
        return 0
    if a/19 >= 10/19:
        return (n-a)/n
    if a >= 16 or a <= 5:
        return 0
    return a/n

def Many(a,n):
    if n <= 0:
        return 0
    if a <= 3 and a/n > 0.35:
        return 0
    if a/n >= 0.5:
        return 1
    return a/n

def Suspicion(Set):
    y = max(Set)
    for i in range(3):
        if y == Set[i]:
            if i == 0:
                return "Suspeito"
            if i == 1:
                return "Incerto"
            return "Não suspeito"
        
def LikelyHood(Set):
    y = max(Set)
    for i in range(5):
        if y == Set[i]:
            return i + 1

def Allyship(Set):
    y = max(Set)
    for i in range(3):
        if y == Set[i]:
            if i == 0:
                return "Poucos"
            if i == 1:
                return "Alguns"
            return "Muitos"


#Danger levels

def Danger_Trust(Neg_Karma,Players,Pos_Karma):
    Sus_Set = [Suspicious(Neg_Karma),Uncertain(Neg_Karma),Not_Suspicious(Neg_Karma)]
    Likelyhood_Set = [Very_unlikely(Players), Unlikely(Players), Neutral(Players), Likely(Players), Very_likely(Players)]
    
    Likelyhood_inc = LikelyHood(Likelyhood_Set)
    
    if Suspicion(Sus_Set) == "Suspeito" and Likelyhood_inc >= 3:
        return 10
    if Suspicion(Sus_Set) == "Não suspeito" and Likelyhood_inc <= 3:
        return 3 + (Likelyhood_inc/2)
    Suspicion_level = 5 * Sus_Set[0] + Sus_Set[1] - Sus_Set[2]
    return Suspicion_level + Likelyhood_inc - 0.5*(Pos_Karma)


def Danger_Lie(Players,Allies):
    Likelyhood_Set = [Very_unlikely(Players), Unlikely(Players), Neutral(Players), Likely(Players), Very_likely(Players)]
    Ally_Set = [Few(Allies,Players),Some(Allies,Players),Many(Allies,Players)]
    
    Alliances = Allyship(Ally_Set)
    Likelyhood_inc = LikelyHood(Likelyhood_Set)
    
    if Allies == 0:
        return 6-Likelyhood_inc
    if Alliances == "Muitos" and Players <= 10:
        return 10
    
    return int(2 + 2 * abs(3-Likelyhood_inc) + 3*Ally_Set[2] + 2*(Ally_Set[1]) - 3*(Ally_Set[0]))

class Bot():
    def __init__(self,karma,Allies,Trust,Current_suit):
        self.Ownkarma = karma
        self.alliances = Allies
        self.Player_Karma = 0
        self.Trust_meter = Trust
        self.Suit = Current_suit
    def Lie(self,Danger_l,suit):
        if Danger_l >= 7:
            return suit
        Danger_l = Danger_l + self.Trust_meter
        if Danger_l >= 7:
            return suit
        while True:
            i = randint(0,3)
            if suits[i] != suit:
                return suits[i]
    def Trust(self,Danger_t,suit):
        if Danger_t <= 4:
            return suit
        Danger_t = Danger_t - self.Trust_meter
        if Danger_t <= 4:
            return suit
        if self.alliances >= 1:
            chance = randint(1,3)
            if chance <= 2:
                return self.Suit
        while True:
            i = randint(0,3)
            if suits[i] != suit:
                return suits[i]
        
    
    
