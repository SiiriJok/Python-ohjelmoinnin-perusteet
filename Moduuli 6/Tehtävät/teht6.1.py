"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton
jälkeen saadun silmäluvun.
"""

import random

def heitto():
    return random.randint(1,6)

print("Heitän noppaa, kunnes saan 6 numeron.")

while True:
    luku = heitto()
    print(luku)

    if luku == 6:
        break

print("Ei tarvitse heittää enään")

