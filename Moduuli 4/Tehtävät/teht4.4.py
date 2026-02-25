#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
#kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
#Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

oikea = random.randint(1,10)

while True:
    luku = int(input("Arvaa luku 1 ja 10 väliltä: "))
    if luku == oikea:
        break
    elif luku < oikea:
        print("Liian pieni arvaus")
    elif luku > oikea:
        print("Liian suuri arvaus")

else:
    print("Luvun pitää olla 1 ja 10 väliltä")

print("Oikein!")

