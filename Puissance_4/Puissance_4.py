# g --> grille principale qui va Ã©voluer en fonction de la partie 
# g = [[0 for l in range(7)] for c in range(6)]
g = [
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     ]


# l --> ligne (valeur entre 0 et 5)
# c --> colonne (valeur entre 0 et 6)
# j --> joueur (valeur entre 1 ou 2)
# 0 --> case vide | 1 ou 2 --> joueur correspondant

# 1 --> X
# 2 --> O

# Affiche la grille vide
def grille_vide():
    t_vide = [[0 for l in range(7)] for c in range(6)]
    for c in range(len(t_vide)):
        print(t_vide[c], "\n")
        
def affiche(g):
    # On remplace les valeurs par qqch de plus graphique
    for c in range(len(g)):
        for l in range(7):
            if g[c][l] == 0:
                print(".", end='')
            elif g[c][l] == 1:
                print("X", end='')
            elif g[c][l] == 2:
                print("O", end='')
        print("\n")
        

def coup_possible(g, c):
    if g[0][c-1] == 0:
        return True
    else:
        return False



def jouer(g,j,c): # c doit etre l'index
    max = 0
    if coup_possible(g, c) == True:
        for l in range(len(g)):
            if g[l][c] == 0:
                max = i
        g[max][c] = j


def horiz(g,j,l,c): # c doit etre l'index
    # g[l][c]
    # g[3][2]
    # faut aller à c-3 et c+3
    

    
    
    
        
    
    










        
    
    
            
                


    