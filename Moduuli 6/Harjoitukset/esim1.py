
def tervehdys(teksti, kerrat):
    for i in range(kerrat):
        print(teksti)
    return

#Pääohjelma
print("Tästä ohjelma akaa")
tervehdys("Hello", 3)
print("Tähän ohjelma päättyy")
tervehdys("Päivää", 5)
tervehdys("Hyvää iltaa", 2)
print("Loppu")

"""
def vaihda_nimi():
    kaupunki = "Vantaa"         #Lokaali muuttuja
    print("Funktion päättyessä kaupunki on", kaupunki)
    return

kaupunki = "Helsinki"           #Globaali muuttuja
print("Ennen funktioa kaupunki on", kaupunki)
vaihda_nimi()
print("Funktion jälkeen kaupunki on", kaupunki)
"""
