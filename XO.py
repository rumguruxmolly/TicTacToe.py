from numpy import *
from random import *
def saisie():
    x=0
    while x<2:
        x = int(input('saisie la longueur du jeux'))
    return x
# Done
n = saisie()
T = array([[str()]*n]*n)
def remplir(T,n):
    for L in range(n):
        for C in range(n):
            T[L,C] = "-"
# Done
def show(T,n):
    for L in range(n):
        for C in range(n):
            print(T[L,C] , end="|")
        print()
# done
def XouO():
    x=0
    print("choisir 1: X ou 2: O")
    while x != 1 and x != 2:
        x=int(input("votre choix: "))
    return x
# done
def PcVsHuman():
    x=0
    print("Jouer contre 1: Un humain ou 2: Un pc")
    while x != 1 and x != 2:
        x=int(input("votre choix: "))
    return x
# done
def SaisieX(T,n):
    print("Tour du X")
    L = int(input('ligne: '))
    C = int(input('Colonne: '))
    while not(1<=L<=n) and not(1<=C<=n) or T[L-1,C-1]!='-':
        if T[L-1,C-1]!='-':
            print("erreur! cette place est deja occupe!")
            L = int(input('ligne: '))
            C = int(input('Colonne: '))
        L = int(input('ligne: '))
        C = int(input('Colonne: '))

    T[L-1,C-1] = "X"
# done
def SaisieO(T,n):
    print("Tour du O")
    L = int(input('ligne: '))
    C = int(input('Colonne: '))

    while not(1<=L<=n) and not(1<=C<=n) or T[L-1,C-1]!='-':
        if T[L-1,C-1]!='-':
            print("erreur! cette place est deja occupe!")
            L = int(input('ligne: '))
            C = int(input('Colonne: '))
        L = int(input('ligne: '))
        C = int(input('Colonne: '))
    T[L-1,C-1] = "O"
# done
def PcTurnX(T,n):
    L = randint(0,n-1)
    C = randint(0,n-1)
    while T[L,C]!="-":
        L = randint(0,n-1)
        C = randint(0,n-1)
    T[L,C]="X"
def PcTurnO(T,n):
    L = randint(0,n-1)
    C = randint(0,n-1)
    while T[L,C]!="-":
        L = randint(0,n-1)
        C = randint(0,n-1)
    T[L,C]="O"

def check(T, n):
    # Check rows
    for L in range(n):
        iX = True
        iO = True
        for C in range(n):
            if T[L, C] != "X":
                iX = False
            if T[L, C] != "O":
                iO = False
        if iX:
            print("X a gagné")
            return True
        if iO:
            print("O a gagné")
            return True

    # Check columns
    for C in range(n):
        iX = True
        iO = True
        for L in range(n):
            if T[L, C] != "X":
                iX = False
            if T[L, C] != "O":
                iO = False
        if iX:
            print("X a gagné")
            return True
        if iO:
            print("O a gagné")
            return True

    iX1 = True
    iO1 = True
    iX2 = True
    iO2 = True
    for i in range(n):
        if T[i, i] != "X":
            iX1 = False
        if T[i, i] != "O":
            iO1 = False
        if T[i, n - i - 1] != "X":
            iX2 = False
        if T[i, n - i - 1] != "O":
            iO2 = False
    if iX1 or iX2:
        print("X a gagné")
        return True
    if iO1 or iO2:
        print("O a gagné")
        return True

    # Check for a draw
    for L in range(n):
        for C in range(n):
            if T[L, C] == "-":
                return False

    print("Game Over")
    return True

    
choix1 = XouO()
choix2 = PcVsHuman()
def jeux(choix1, choix2,n,T):
    if choix1 == 1:
        if choix2 == 1:
            while not(check(T,n)):
                SaisieX(T, n)
                show(T, n)
                if check(T, n):
                    break
                SaisieO(T, n)
                show(T, n)
        else:
             while not(check(T,n)):
                SaisieX(T, n)
                show(T, n)
                if check(T, n):
                    break
                PcTurnO(T, n)
                show(T, n)
    else:
        if choix2 == 1:
            while not(check(T,n)):
                PcTurnX(T, n)
                show(T, n)
                if check(T, n):
                    break
                SaisieO(T, n)
                show(T, n)
        else:
            while not(check(T,n)):
                SaisieX(T, n)
                show(T, n)
                if check(T, n):
                    break
                PcTurnO(T, n)
                show(T, n)


remplir(T,n)
jeux(choix1, choix2,n,T)