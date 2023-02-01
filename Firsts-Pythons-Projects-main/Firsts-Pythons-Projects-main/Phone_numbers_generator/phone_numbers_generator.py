import random
import os
import phonenumbers 

def random_number(indicatif):
    numero = indicatif + random.choice(["6", "7"])
    for i in range(4):
        then = random.randint(0, 99)
        # Permet de rajouter un 0 devant le nombre s'il est inférieur à 10
        if then < 10:
            then = "0" + str(then)
        numero = numero + str(then)
    return numero

def test_num(numero):
    phoneNumber = phonenumbers.parse(numero)
    possible = phonenumbers.is_possible_number(phoneNumber)
    valid = phonenumbers.is_valid_number(phoneNumber)
    if possible == True and valid == True:
        return True
    else:
        return False

quantite = int(input("Combien de numéros voulez-vous générer ? "))
indicatif = str(input("Quel est l'indicatif ? Ex: +33\n"))
counter_valid_number = 0
   
file = open("generator_num.txt", "a+")
for i in range(quantite):
    numero = random_number(indicatif)
    if test_num(numero):
        counter_valid_number = counter_valid_number + 1
        file.write( numero + '\n')
        print(numero)
file.close

print("Fin de la génération...")
pourcent = (100*counter_valid_number)/quantite
print(f"Il y a eu {counter_valid_number} numéros valides générés, soit {int(pourcent)}% des numéros totals générés")
