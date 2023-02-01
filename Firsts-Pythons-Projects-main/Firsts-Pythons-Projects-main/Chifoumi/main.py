from random import *

def choice_user():
    user = input("Choisis ton coup :\nPierre\nPapier\nCiseaux\n")
    while user not in ["Pierre","Papier","Ciseaux"]:
        print("Le coup sélectionné n'est pas correct...Réessayez")
        user = input("Pierre\nPapier\nCiseaux\n")
    return(user)

def choice_bot():
    n = randint(1,3)
    if n == 1:
        ordi = "Pierre"
    elif n == 2:
        ordi = "Papier"
    else:
        ordi = "Ciseaux"
    return(ordi)

def main():

    ordi = choice_bot()
    user = choice_user()

    print("(========================================)")
    print(f"Joueur: {user} VS Ordinateur: {ordi}")

    # Ciseaux > Papier
    # Pierre > Ciseaux
    # Papier > Pierre

    if user == "Ciseaux" and ordi == "Papier":
        print("You win !") 
    elif user == "Pierre" and ordi == "Ciseaux":
        print("You win !")
    elif user == "Papier" and ordi == "Pierre":
        print("You win !")
    elif user == "Papier" and ordi == "Ciseaux":
        print("You lose !")
    elif user == "Ciseaux" and ordi == "Pierre":
        print("You lose !")
    elif user == "Pierre" and ordi == "Papier":
        print("You lose !")
    elif user == ordi:
        print("Partie nulle !")
    
main()

new_game = input("Souhaitez-vous rejouer ? True or False ")
try:
     new_game == "True" or "False"
except:
    new_game = input("Souhaitez-vous rejouer ? True or False ")

while new_game == "True":
    main()
    new_game = input("Souhaitez-vous rejouer ? True or False ")
exit()





