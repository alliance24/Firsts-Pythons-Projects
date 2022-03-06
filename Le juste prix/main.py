import random
import time

juste_prix = random.randint(0, 100)
prix_testé = int(input("Quel est le prix ? "))
nb_erreurs = 0

if prix_testé not in range(0, 100):
    print("Erreur, la valeur proposé n'est pas comprise entre 0 et 100 !")
    time.sleep(2)
    exit()



while prix_testé != juste_prix:
    if prix_testé > juste_prix:
        print("Le prix est trop grand")
        print("Réessayez encore")
        prix_testé = int(input("Quel est le prix ? "))
        nb_erreurs = nb_erreurs + 1
        
    elif prix_testé < juste_prix:
        print("Le prix est trop petit")
        print("Réessayez encore")
        prix_testé = int(input("Quel est le prix ? "))
        nb_erreurs = nb_erreurs + 1
        
if prix_testé == juste_prix:
    print("C'est le juste prix ! You win ! ", juste_prix)
print(f"Vous avez fait : {nb_erreurs} erreurs")

nb_erreurs = str(nb_erreurs) # Transforme la variable nb_erreurs int --> str
file = open("nb_erreurs.txt", "a+") # File = fichier ouvert
file.write(nb_erreurs + '\n') # On écrit le nb d'erreurs
file.close() # On ferme le fichier











