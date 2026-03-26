"""
Kirjoita funktio nimeltä suurin_arvo, joka saa kolme argumenttia.
Funktion tulee palauttaa näistä kolmesta suurin arvo.
Kysy luvut käyttäjältä input-funktion avulla.
"""

def suurin_arvo(a, b, c):
    return max(a, b, c)

eka = float(input("Ensimmäinen luku: "))
toinen = float(input("Toinen luku: "))
kolmas = float(input("Kolmas luku: "))

suurin = (suurin_arvo(eka, toinen, kolmas))
print(suurin)