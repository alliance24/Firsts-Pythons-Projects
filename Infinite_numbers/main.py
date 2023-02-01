import random

cb_gen = int(input("Combien de lignes ? \n"))

def random_number():
    composit = str(random.randint(0, 99))
    for i in range(4):
        then = random.randint(0, 99)
        # Permet de rajouter un 0 devant le nombre s'il est inférieur à 10
        if then < 10:
            then = "0" + str(then)
        composit = composit + str(then)
    return composit

for i in range(0, cb_gen):
    text = ""
    for i in range(6):
        text = text + " " + random_number()
    print(text)

