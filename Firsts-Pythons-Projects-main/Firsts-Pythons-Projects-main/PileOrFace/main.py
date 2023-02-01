import random
import os

cb_tirage = int(input("Combien de tirages souhaitez-vous effectuer ? \n"))
pile = 0
face = 0
graph_pile = ""
graph_face = ""
SYMBOLE = "|"

def tirage():
    test = random.randint(1, 2)
    if test == 1:
        global pile
        global graph_pile
        pile = pile + 1
        graph_pile = graph_pile + SYMBOLE
    else:
        global face 
        global graph_face
        face = face + 1
        graph_face = graph_face + SYMBOLE 

for i in range(0, cb_tirage):
    tirage()

pourcent_pile = int((pile/cb_tirage)*100)
pourcent_face = int((face/cb_tirage)*100)

print("Il y a eu : ")
print()
print(f"- {pile} tirages pile soit {pourcent_pile}% des tirages")
print(graph_pile, "\n")
print(f"- {face} tirages face soit {pourcent_face}% des tirages")
print(graph_face)
print()


