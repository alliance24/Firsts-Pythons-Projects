from operator import index
import random

PLAYER = "X"
BOT = "O"
base = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8", "case9"]
ligne = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8", "case9"]
game = "run"

def grid():
    print()
    print(f" {ligne[0]} | {ligne[1]} | {ligne[2]} \n-------+-------+-------\n {ligne[3]} | {ligne[4]} | {ligne[5]} \n-------+-------+-------\n {ligne[6]} | {ligne[7]} | {ligne[8]} \n")

def player_move(joueur):
    tour_termine = False
    while tour_termine != True:
        move = input("Où souhaitez vous jouer ? (Ex: case1) \n ")
        if move == "stop":
            exit()
        index = ligne.index(move)
        if ligne[index] == base[index]:  
            ligne[index] = joueur
            tour_termine = True

def bot_round(bot):
    tour_termine = False
    while tour_termine != True:
        index = random.randint(0, 8)
        if ligne[index] == base[index]:  
                ligne[index] = bot
                tour_termine = True

def main():
    print("Vous allez jouer au morpion ! \n ")
    grid()
    begin = random.choice([True, False])
    if begin == "True":
        player_move(PLAYER)
        grid()
    else :
        bot_round(BOT)
        grid()
    
    global game
    while game != "end":
        player_move(PLAYER)
        grid()
        test_win()
        bot_round(BOT)
        grid()
        test_win()


def test_win():
    global game
    if ligne[0] == ligne[1] == ligne[2] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[3] == ligne[4] == ligne[5] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[6] == ligne[7] == ligne[8] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[0] == ligne[4] == ligne[8] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[2] == ligne[4] == ligne[6] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[0] == ligne[3] == ligne[6] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[1] == ligne[4] == ligne[7] == "X":
        print("Vous avez gagné ! ")
        game = "end"
    elif ligne[2] == ligne[5] == ligne[8] == "X":
        print("Vous avez gagné ! ")
        game = "end"

    if ligne[0] == ligne[1] == ligne[2] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[3] == ligne[4] == ligne[5] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[6] == ligne[7] == ligne[8] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[0] == ligne[4] == ligne[8] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[2] == ligne[4] == ligne[6] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[0] == ligne[3] == ligne[6] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[1] == ligne[4] == ligne[7] == "O":
        print("Vous avez perdu ! ")
        game = "end"
    elif ligne[2] == ligne[5] == ligne[8] == "O":
        print("Vous avez perdu ! ")
        game = "end"

main()
