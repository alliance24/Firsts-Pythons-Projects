import random

cb_gen = int(input("Combien de lignes ? \n"))

def random_number():
    composit = str(random.randint(10, 99))
    numero = composit + " " + composit + " " + composit + " " + composit + " " + composit
    return numero

for i in range(0, cb_gen):
    print(f"{random_number()} {random_number()} {random_number()} {random_number()} {random_number()} {random_number()}")

