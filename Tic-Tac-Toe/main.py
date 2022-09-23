import random

PLAYER = "X"
BOT = "O"
case1 = "."
case2 = "."
case3 = "."
case4 = "."
case5 = "."
case6 = "."
case7 = "."
case8 = "."
case9 = "."
liste = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8", "case9"]
game = "run"

def bot_round():
    bot_move = random.choice(liste)
    global BOT
    global case1
    global case2
    global case3
    global case4
    global case5
    global case6
    global case7
    global case8
    global case9
    if bot_move == "case1" and case1 != PLAYER:
        case1 = BOT
    elif bot_move == "case2" and case2 != PLAYER:
        case2 = BOT
    elif bot_move == "case3" and case3 != PLAYER:
        case3 = BOT
    elif bot_move == "case4" and case4 != PLAYER:
        case4 = BOT
    elif bot_move == "case5" and case5 != PLAYER:
        case5 = BOT
    elif bot_move == "case6" and case6 != PLAYER:
        case6 = BOT
    elif bot_move == "case7" and case7 != PLAYER:
        case7 = BOT
    elif bot_move == "case8" and case8 != PLAYER:
        case8 = BOT
    elif bot_move == "case9" and case9 != PLAYER:
        case9 = BOT

def player_move():
    global PLAYER
    global case1
    global case2
    global case3
    global case4
    global case5
    global case6
    global case7
    global case8
    global case9
    move = input("Où souhaitez vous jouer ? (Ex: case1) \n ")
    if move == "case1":
        case1 = PLAYER
    elif move == "case2":
        case2 = PLAYER
    elif move == "case3":
        case3 = PLAYER
    elif move == "case4":
        case4 = PLAYER
    elif move == "case5":
        case5 = PLAYER
    elif move == "case6":
        case6 = PLAYER
    elif move == "case7":
        case7 = PLAYER
    elif move == "case8":
        case8 = PLAYER
    elif move == "case9":
        case9 = PLAYER

def grid_explain():
    print(" case1 | case2 | case3 ")
    print("-------+-------+-------")
    print(" case4 | case5 | case6 ")
    print("-------+-------+-------")
    print(" case7 | case8 | case9 \n")

def grid():
    print()
    print(f" {case1} | {case2} | {case3} ")
    print(f"---+---+---")
    print(f" {case4} | {case5} | {case6} ")
    print(f"---+---+---")
    print(f" {case7} | {case8} | {case9} \n")

liste_true_false = ["False", "True"]

def test_win():
    global game
    if case1 == case2 == case3 == "X":
        game = "end"
        print("Vous avez gagné ! ")
        
    elif case4 == case5 == case6 == "X":
        game = "end"
        print("Vous avez gagné ! ")
       
    elif case7 == case8 == case9 == "X":
        game = "end"
        print("Vous avez gagné ! ")
       
    elif case1 == case5 == case9 == "X":
        game = "end"
        print("Vous avez gagné ! ")
        
    elif case3 == case5 == case7 == "X":
        game = "end"
        print("Vous avez gagné ! ")
        
    elif case1 == case4 == case7 == "X":
        game = "end"
        print("Vous avez gagné ! ")
        
    elif case2 == case5 == case8 == "X":
        game = "end"
        print("Vous avez gagné ! ")
       
    elif case3 == case6 == case9 == "X":
        game = "end"
        print("Vous avez gagné ! ")
        

    if case1 == case2 == case3 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case4 == case5 == case6 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case7 == case8 == case9 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case1 == case5 == case9 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case3 == case5 == case7 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case1 == case4 == case7 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case2 == case5 == case8 == "O":
        game = "end"
        print("Vous avez perdu ! ")
        
    elif case3 == case6 == case9 == "O":
        game = "end"
        print("Vous avez perdu ! ")

def main():
    print("Vous allez jouer au morpion ! \n ")
    grid_explain()
    begin = random.choice(liste_true_false)
    if begin == "True":
        player_move()
        grid()
        bot_round()
        grid()
    else :
        bot_round()
        grid()
    
    global game
    while game != "end":
        player_move()
        test_win()
        grid()
        bot_round()
        test_win()
        grid()

main()

'''
case1 and case2 and case3 == "O"
case4 and case5 and case6 == "O"
case7 and case8 and case9 == "O"
case1 and case5 and case9 == "O"
case3 and case5 and case7 == "O"
case1 and case4 and case7 == "O"
case2 and case5 and case8 == "O"
case3 and case6 and case9 == "O"
'''