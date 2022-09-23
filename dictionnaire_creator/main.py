import os
import string

CARACTERE_min = list(string.ascii_lowercase)
CARACTERE_maj = list(string.ascii_uppercase)
NOMBRES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
général = (CARACTERE_maj + CARACTERE_min + NOMBRES)

def main(cb_caractères):
    file = open("dictionnaire_creator\\dictionnaire.txt", "a+")
    
    
    file.close





main()