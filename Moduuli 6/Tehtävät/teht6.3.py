"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos
on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen
gallonamäärän.
* Yksi gallona on 3,785 litraa.
"""

def gallonat_litroina(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna gallona määrä: "))
    if gallonat < 0:
        break

    litrat = gallonat_litroina(gallonat)
    print(litrat, "Litraa")
