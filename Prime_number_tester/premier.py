from math import *

nombre_teste = int(input("Quel nombre souhaitez-vous tester ? "))
racine_nombre_teste = int(round(sqrt(nombre_teste), 2))

print(racine_nombre_teste)

def is_prime():
    for i in range(0, racine_nombre_teste):
        print()

nombres_premiers = [2, 3, 5, 7, 11, 13, 17, 23]