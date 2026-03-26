"""
Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5
kirjainta.
Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen.
"""

lista = ["sana", "kissa", "hattuhylly", "sika", "muurahainen", "kassi"]

yli_5 = 0

for i in lista:
    if len(i) > 5:
        yli_5 += 1

print("Yli 5 kirjaimisia sanoja on yhteensä listassa", yli_5)