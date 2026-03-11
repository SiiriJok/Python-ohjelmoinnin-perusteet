#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia
#arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpa = int(input("Kuinka monta arpakuutiota on? "))

summa = 0

for heitto in range(arpa):
    heitto = random.randint(1,6)
    summa += heitto

print("Silmälukujen summa on:", summa)