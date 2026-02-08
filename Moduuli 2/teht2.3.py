import math

print("Mikä on suorakulmion: \n")

kanta = float(input("Kanta = "))
korkeus = float(input("Korkeus = "))

piiri = (kanta * 2) + (korkeus * 2)
pinta_ala = kanta * korkeus

print(f"\nSuorakulmion piiri on {piiri} ja pinta_ala on {pinta_ala}")
