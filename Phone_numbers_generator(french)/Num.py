import random

def random_number():
    liste = ["06", "07"]
    number_base = str(random.choice(liste))
    composit_1 = str(random.randint(10, 99))
    composit_2 = str(random.randint(10, 99))
    composit_3 = str(random.randint(10, 99))
    composit_4 = str(random.randint(10, 99))
    numero = number_base + " " + composit_1 + " " + composit_2 + " " + composit_3 + " " + composit_4
    print(numero)

random_number()