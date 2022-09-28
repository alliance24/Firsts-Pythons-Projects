import string
from class_Password import Password

mdp = str(input("Entrez votre mot de passe...\n"))
key1 = int(input("Entrez la clé de cryptage/décryptage n°1...\n"))
key2 = int(input("Entrez la clé de cryptage/décryptage n°2...\n"))
key3 = int(input("Entrez la clé de cryptage/décryptage n°3...\n"))
password = Password(mdp, key1, key2, key3)
print("Que souhaitez-vous faire ? ")
ask = int(input("Tapez 1 pour crypter et 2 pour décrypter...\n"))
if ask == 1:
    print(password.crypt(mdp, key1, key2, key3))
elif ask == 2:
    print(password.un_crypt(mdp, key1, key2, key3))
else:
    exit()

