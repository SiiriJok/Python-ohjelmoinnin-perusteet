import random

def koodi_1():
    koodi = []
    kierros = 3
    for i in range(kierros):
        koodi.append(random.randint(0, 9))
    return koodi

print ("Kolminumeroinen koodi on: ", koodi_1())

def koodi_2():
    koodi = []
    kierros = 4
    for i in range(kierros):
        koodi.append(random.randint(1, 6))
    return koodi

print ("Nelinumeroinen koodi on: ", koodi_2())


luku_1 = random.randint(0,9)
luku_2 = random.randint(1,6)

