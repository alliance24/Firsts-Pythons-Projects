from random import randint

def grille_vide():
    return [[0 for x in range(3)] for y in range(3)]


def affiche(g):
    print() # Permet de sauter une ligne (+ propre visuellement parlant)
    # On remplace les valeurs par qqch de plus graphique
    for y in range(len(g)):
        
        for x in range(3):
            if g[y][x] == 0:
                print("   .", end='')
            elif g[y][x] == 1:
                print("   X", end='')
            elif g[y][x] == 2:
                print("   O", end='')
        print("\n")

def explications():
    print("""

    """)



def get_x(coordonnees): 
    
    if coordonnees == 1 or coordonnees == 4 or coordonnees == 7:
        x = 0
    elif coordonnees == 2 or coordonnees == 5 or coordonnees == 8:
        x = 1
    else:
        x = 2
    
    return x


def get_y(coordonnees):
    
    if coordonnees <= 3: 
        y = 0
    elif coordonnees >= 3 and coordonnees <= 6:
        y = 1
    else:
        y = 2
    
    return y

def coup_possible(g, x, y): 
    if g[y][x] == 0:
        return True
    else: 
        return False
    
def jouer(g, j, x, y):
    g[y][x] = j
    
def horiz(g, j, y, x):
    if g[y][x] == j:
        if g[y][x] == g[y-1][x] and g[y][x] == g[y+1][x]:
            return True
        else:
            return False
    else:
        return False

def vert(g, j, y, x):
    if g[y][x] == j:
        if g[y][x] == g[y][x-1] and g[y][x] == g[y][x+1]:
            return True
        else:
            return False
    else:
        return False

def diag(g, j, y, x):
    if g[y][x] == j:
        if g[y][x] == 5:
            if g[y][x] == g[0][0] and g[y][x] == g[2][2]:
                return True
            elif g[y][x] == g[0][2] and g[y][x] == g[2][0]:
                return True
            else:
                return False
    else:
        return False
        
# g[0][0] - g[1][1] - g[2][2]
# g[0][2] - g[1][1] - g[2][0]

def victoire(g, j):
    for y in range(0, 2):
        for x in range(0, 2):
            if horiz(g, j, x, y) or vert(g, j, x, y) or diag(g, j, x, y):
                return True
    return False

def match_nul(g):
    for y in range(3):
        for x in range(3):
            if coup_possible(g, x, y):
                return False
    return True

def coup_aleatoire(g, j):
    coordonnees = randint(1,9)
    x = get_x(coordonnees)
    y = get_y(coordonnees)
    while coup_possible(g, x, y) == False:
        coordonnees = randint(1,9)
        x = get_x(coordonnees)
        y = get_y(coordonnees)       
    jouer(g, j, x, y)

def main():
    g = grille_vide()
    bot = 2
    joueur = 1
    win = joueur
    explications()
    if randint(0, 1) == 0:
        coordonnees = int(input("Dans quelle case souhaitez-vous jouer ? "))
        x = get_x(coordonnees)
        y = get_y(coordonnees)
        while coup_possible(g, x, y) ==  False:
            print("Il semblerait que vous essayez de jouer dans une case indisponible...")
            coordonnees = int(input("Dans quelle case souhaitez-vous jouer ? "))
            x = get_x(coordonnees)
            y = get_y(coordonnees)
        
        jouer(g, joueur, x, y)
        affiche(g)
        win = joueur
        victoire(g, win)
        match_nul(g)
        
    while victoire(g, win) == False and match_nul(g) == False:
        # -----------------------------------------------------------------------------------------------
        coup_aleatoire(g, bot)
        affiche(g)
        win = bot
        victoire(g, win)
        
        # -----------------------------------------------------------------------------------------------
        
        coordonnees = int(input("Dans quelle case souhaitez-vous jouer ? "))
        x = get_x(coordonnees)
        y = get_y(coordonnees)
        while coup_possible(g, x, y) ==  False:
            print("Il semblerait que vous essayez de jouer dans une case indisponible...")
            coordonnees = int(input("Dans quelle case souhaitez-vous jouer ? "))
            x = get_x(coordonnees)
            y = get_y(coordonnees)
        
        jouer(g, joueur, x, y)
        affiche(g)
        win = joueur
        victoire(g, win)
        match_nul(g)
    
    if win == joueur:
        print("Bravo !!! Vous avez gagné !")    
    elif win == bot:
        print("Quel dommage, vous avez perdu... Vous ferez mieux la prochaine fois")  
    else:
        print("Vous avez fait égalité...") 
         
main()