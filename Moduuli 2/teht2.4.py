import math

print("Luettele alle kolme kokonaislukua \n")

yksi = int(input("Ensimmäinen: "))
kaksi = int(input("Toinen: "))
kolme = int(input("Kolmas: "))

summa = yksi + kaksi + kolme
tulo = yksi * kaksi * kolme
keskiarvo = (yksi + kaksi + kolme) / 3

print(f"\nLukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}")
