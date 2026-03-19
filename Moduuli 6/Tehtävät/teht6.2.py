"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun
funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan
heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman
suorituksen alussa.
"""

import random

def heitto(tahkot):
    return random.randint(1,tahkot)

tahkot = int(input("Kuinka monta tahkoa nopassa on? "))

while True:
    luku = heitto(tahkot)
    print(luku)

    if luku == tahkot:
        break

print("Ei tarvitse heittää enään")