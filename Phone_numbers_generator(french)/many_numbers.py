import random
import os
import phonenumbers 

supprime = str(input("Voulez-vous supprimer les précédents résultats ? Oui/Non "))

if supprime == "Oui" or "oui":
    os.remove('generator_num.txt')
    file = open("generator_num.txt", "a+")
    file.close
file.close

quantite = int(input("Combien de numéros voulez-vous générer ? "))
filtre_on = str(input("Souhaitez-vous activer un filtre ? Oui/Non "))
filtre_alone = ""
many_filtres = 0
selection = ""
filtres = []

if filtre_on == "Oui" or "oui":
    many_filtres = int(input("Combien de filtres souhaitez vous utiliser ? "))
    if many_filtres <= 1:
        filtre_alone = str(input("Quel est votre filtre ? "))
    else :
        selection = " "
        filtres = []
        while selection != "":
            selection = str(input("Quelles sont vos filtres ? "))
            filtres.append(selection)

filtres_find = []
counter = 0

def random_number():
    indicatif = ["+33"]
    numero_base = [6, 7]
    number_base = str(random.choice(indicatif))
    number_base_2 = str(random.choice(numero_base))
    composit_1 = str(random.randint(10, 99))
    composit_2 = str(random.randint(10, 99))
    composit_3 = str(random.randint(10, 99))
    composit_4 = str(random.randint(10, 99))
    global numero
    global filtres
    global filtre_alone
    numero = number_base + number_base_2 + composit_1 + composit_2 + composit_3 + composit_4 
    if filtre_alone == numero or numero in filtres:
        filtres_find.append(numero)
    return numero

def test_num(numero):
    phoneNumber = phonenumbers.parse(numero)
    global possible
    global valid
    possible = phonenumbers.is_possible_number(phoneNumber)
    valid = phonenumbers.is_valid_number(phoneNumber)
    if possible == True and valid == True:
        return True
    else:
        return False
   
file = open("generator_num.txt", "a+")

for i in range(quantite):
    random_number()
    if test_num(numero) == True:
        counter = counter + 1
        file.write( numero + '\n')
        print(numero)

file.close
print("Fin de la génération...")
print(f"Il y a eu {counter} numéros valides générés")

for i in filtres_find:
    print(f"Le filtre suivant a bien été trouvé : {i}")