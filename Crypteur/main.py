import os
from class_Password import Password


while True:
    print("Que souhaitez-vous faire ? ")
    ask = int(input("Tapez 1 pour crypter et 2 pour décrypter...\n"))
    mdp = str(input("Entrez votre mot de passe...\n"))
    os.system("cls")
    key = int(input("Entrez votre clé de cryptage (mémorisez la bien) \n"))
    os.system("cls")
    key1 = key//100
    key2 = key//10
    key3 = key//1
    password = Password(mdp, key1, key2, key3)
    if ask == 1:
        print(password.crypt(mdp, key1, key2, key3))
    elif ask == 2:
        print(password.un_crypt(mdp, key1, key2, key3))


