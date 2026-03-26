"""
 Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan. Jokaisen
lisäyksen jälkeen lista tulostetaan kahdella tavalla: lisäysjärjestyksessä ja
pienimmästä suurimpaan järjestettynä. Ohjelma lopettaa, kun käyttäjä syöttää 0.
"""

lista = []

while True:
    luku = int(input("Anna luku (0 lopettaa): "))

    if luku == 0:
        print("Ohjelma päättyy.")
        break

    lista.append(luku)
    print("Lista nyt:", lista)
    print("Lista järjestyksessä:", sorted(lista))

