import os
import string

CARACTERE_min = list(string.ascii_lowercase)
CARACTERE_maj = list(string.ascii_uppercase)
NOMBRES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
value = (CARACTERE_maj + CARACTERE_min + NOMBRES)


def create_dico(n):
    o = 0
    final = ""
    for i in range(n**len(value)):
        for j in range(len(value)):
            final += value[j]
            o+=1
        print(final)


        

create_dico(1)