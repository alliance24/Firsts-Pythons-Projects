search = input("Quel numéro souhaitez-vous chercher ? \n Sous la forme +33000000000 \n")
file = open("generator_num.txt", "r")
find = False

for ligne in file:
    if ligne == search:
        print("Le numéro cherché a été trouvé !")
        find = True
file.close

if find == False:
    print("Le numéro cherché n'est pas présent dans le fichier...")







