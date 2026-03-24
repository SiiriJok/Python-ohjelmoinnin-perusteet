"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""

import math

def yksikkohinta(halkaisija, hinta):
    halkaisija_m = halkaisija / 100
    sade = halkaisija_m / 2
    pinta_ala = math.pi * sade ** 2
    hinta_per_neliometri = hinta / pinta_ala
    return hinta_per_neliometri


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta on {yksikkohinta1:.2f} euroa per neliömetri.")
print(f"Toisen pizzan yksikköhinta on {yksikkohinta2:.2f} euroa per neliömetri.")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat samanarvoisia.")