from random import randint

def grille_vide():
    return [[0 for c in range(3)] for l in range(3)]


def affiche(g):
    print() # Permet de sauter une ligne (+ propre visuellement parlant)
    # On remplace les valeurs par qqch de plus graphique
    for l in range(len(g)):
        
        for c in range(3):
            if g[l][c] == 0:
                print("   .", end='')
            elif g[l][c] == 1:
                print("   X", end='')
            elif g[l][c] == 2:
                print("   O", end='')
        print("\n")

def coup_possible(g, c): # c doit etre l'index
    if c >3 or c <0:
        return False
    if g[0][c] == 0: return True
    else: return False

g = grille_vide()
affiche(g)