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

def coup_possible(g, l, c): 
    if g[l][c] == 0:
        return True
    else: 
        return False
    
def jouer(g, j, l, c):
    g[l][c]=j
    
def horiz(g,j,l,c):
    i=2
    while c-i<0:
        i-=1
    while i>=0 and c-i<=3:
        if g[l][c-i]==j and g[l][c-i+1]==j and g[l][c-i+2]==j:
            return True
        i-=1
    return False

def vert(g,j,l,c):
    i=2
    while l-i<0:
        i-=1
    while i>=0 and l-i<=2:
        if g[l-i][c]==j and g[l-i+1][c]==j and g[l-i+2][c]==j:
            return True
        i-=1
    return False

def diag(g,j,l,c):
    i=2
    while c-i<0 or l-i<0: #Diagonale SO-NE
        i-=1
    while i>=0 and c-i<=3 and l-i<=2:
        if g[l-i][c-i]==j and g[l-i+1][c-i+1]==j and g[l-i+2][c-i+2]==j:
            return True
        i-=1
    i=2
    while c-i<0 or l+i>5: #Diagonale NO-SE
        i-=1
    while i>=0 and c-i<=3 and l+i>=3:
        if g[l+i][c-i]==j and g[l+i-1][c-i+1]==j and g[l+i-2][c-i+2]==j:
            return True
        i-=1
    return False

def victoire(g,j):
    for a in range(3):
        for b in range(3):
            if horiz(g,j,a,b) or vert(g,j,a,b) or diag(g,j,a,b):
                return True
    return False

def match_nul(g):
    for l in range(3):
        for c in range(3):
            if coup_possible(g,c):
                return False
    return True

def coup_aleatoire(g,j):
    k=False
    while k==False:
        c=randint(0,6)
        k=coup_possible(g,c)
    return jouer(g,j,c)

def main():
    g = grille_vide()
    bot = 0
    joueur = 1
    affiche(g)
    if randint(0, 1) == 0:
        coup_aleatoire(g, bot)
        
        
    
main()