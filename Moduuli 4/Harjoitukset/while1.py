"""
kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt < kerrat:
    print("Hyvää huomenta")
    tehdyt = tehdyt + 1
"""
"""
hinta = 5
rahaa_annettu = 0


while rahaa_annettu < kerrat:
while rahaa_annettu < hinta:
    rahaa_annettu += 1
    print("Rahaa annettu", rahaa_annettu )

print("Kahvi maksettu")

#------

while True:
    rahaa_annettu += 1
    print("Rahaa annettu", rahaa_annettu )

    if rahaa_annettu == hinta:
        break

print("Kahvi maksettu")
"""

kasky = input("Annetaanko lisää rahaa? ")

while kasky != "ei":
    print("annettu kolikko lisää.")
    kasky = input("Annetaanko lisää rahaa?")

print("Ohjelma päättyy.")
