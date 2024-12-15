import os
import random
# grid_test = [[0, 0, 0, 1, 0], 
#              [1, 0, 1, 0, 1],
#              [0, 1, 0, 1, 0], 
#              [0, 0, 1, 0, 0], 
#              [0, 0, 0, 0, 0]]


def gen_grid(n, m): # n lignes * m colonnes
    grid = [[0 for i in range(m)] for i in range(n)]
    return grid

def play(grid, l, c, p):
    grid[l][c] = p

def check_diag(grid, l, c, p, n, m):
    valid = 0
    
    nx_min = c
    ny_min = l
    while 0 < min(nx_min, ny_min):
        nx_min -= 1
        ny_min -= 1
    # print("nx_min: ", nx_min, "ny_min: ", ny_min)
        
    nx_max = c
    ny_max = l
    while max(nx_max, ny_max) < min(m, n) -1:
        nx_max += 1
        ny_max += 1
    # print("nx_max: ", nx_max, "ny_max: ", ny_max)
    
    # print("------- diag 1 ------")
    for i in range(min(nx_max - nx_min, ny_max-ny_min)):
        if i < (nx_max or ny_max):
            # print("Case number ", ny_min + i, nx_min + i)
            if grid[ny_min + i][nx_min + i] == p:
                valid +=1
                # print("valid +1")
                if valid > 2:
                    return True
            else:
                valid = 0
                # print("valid = 0")

    # print("------- diag 2 ------")
    for i in range(min(nx_max - nx_min, ny_max-ny_min)):
        if i < (ny_min or nx_min):
            # print("Case number ", ny_min - i, nx_min + i)
            if grid[ny_min - i][nx_min + i] == p:
                valid +=1
                # print("valid +1")
                if valid > 2:
                    return True
            else:
                valid = 0
                # print("valid = 0")
                                               
    return False


def check_horiz(grid, l, p):
    
    valid = 0
    for i in range(len(grid[l])):
        # print("Case number ", i)
        if grid[l][i] == p:
            valid += 1
            if 2 < valid:
                return True
            # print("valid +1")
        else:
            valid = 0
            # print("valid = 0")
    return False
        
       
def check_verti(grid, c, p):
    
    valid = 0
    for i in range(len(grid)):
        # print("Case number ", i)
        if grid[i][c] == p:
            valid += 1
            if 2 < valid:
                return True
            # print("valid +1")
        else:
            valid = 0
            # print("valid = 0")
    return False

def check(grid, l, c, p, n, m):
    if check_diag(grid, l, c, p, n, m) or check_verti(grid, c, p) or check_horiz(grid, l, p):
        return True, p
    else:
        return False

def affiche(grid):
    count = 0
    print(end="   ")
    for e in grid[0]:
        print(count, end="  ")
        count +=1
    print(end="\n")
    
    count = 0
    for e in grid:
        print(count, e)
        count +=1
    return


def main():
    jouer = False
    while jouer == False: 
        os.system("cls")
        PLAYER = 1
        BOT = 2
        win = False
        taille = 0
        
        while taille < 3:
            taille = int(input("Entrez une taille de plateau (Ex: 55 - 5 lignes / 5 colonnes) \n"))
            grille = gen_grid((taille // 10) % 10, taille % 10)
            n = (taille // 10) % 10
            m = taille % 10
            
        affiche(grille)
        
        if random.randint(0, 1) == 0:
            coup = int(input("Prochain coup (ligne - colonne) ?  "))
            while grille[(coup // 10) % 10][coup % 10] != 0:
                coup = int(input("Prochain coup (ligne - colonne) ?  "))
            
            play(grille, (coup // 10) % 10, coup % 10, 1)
            affiche(grille)
        
        while win == False:
            y = random.randint(0, n-1)
            x = random.randint(0, m-1)
            # print(bot_play)
            while grille[y][x] != 0:
                y = random.randint(0, n-1)
                x = random.randint(0, m-1)
            play(grille, y, x, BOT)
            affiche(grille)
            win = check(grille, y, x, BOT, n, m)
            
            coup = int(input("Prochain coup (ligne - colonne) ?  "))
            while grille[(coup // 10) % 10][coup % 10] != 0:
                coup = int(input("Prochain coup (ligne - colonne) ?  "))
            
            play(grille, (coup // 10) % 10, coup % 10, PLAYER)
            affiche(grille)
            win = check(grille, (coup // 10) % 10, coup % 10, PLAYER, n, m)
        
        if win[1] == PLAYER:
            print("Vous avez gagné !")
        else:
            print("Bot a gagné !")
        jouer = bool(input("Jouer une nouvelle fois ? \n"))
              
       
# affiche(gen_grid(5, 5))
# affiche(grid_test)
# print(check_horiz(grid_test, 0, 1))
# print(check_verti(grid_test, 0, 1))
# print(check_diag(grid_test, 3, 2, 5, 5, 1))

main()
