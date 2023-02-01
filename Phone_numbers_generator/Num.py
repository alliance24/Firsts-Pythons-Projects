import random

def random_number():
    numero = "+33" + random.choice(["6", "7"])
    for i in range(4):
        then = random.randint(0, 99)
        # Permet de rajouter un 0 devant le nombre s'il est inférieur à 10
        if then < 10:
            then = "0" + str(then)
        numero = numero + str(then)
    return numero

random_number()