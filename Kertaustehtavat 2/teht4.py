"""
Kirjoita funktio nimeltä kuusi, joka ottaa yhden argumentin. Funktio tulostaa tekstin
"Tämä on kuusi!" sekä kuusen, jonka koko määräytyy annetun argumentin
perusteella.
"""

def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko+1):
        valilyonti = " " * (koko - i)
        tahti = "*" * (i * 2 - 1)
        print(valilyonti + tahti)
    print(" " * (koko - 1) + "*")

""" print(" " * (koko - i) + "*" * (2 * i - 1))"""



kuusi(7)
